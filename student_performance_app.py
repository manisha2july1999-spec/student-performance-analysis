import gradio as gr
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ============================================================
# LOAD DATASET
# ============================================================

file_path = r"C:\Users\USER\OneDrive\Documents\datasets\student_performance_updated_1000.csv"

try:
    data = pd.read_csv(file_path)

except FileNotFoundError:
    raise FileNotFoundError(
        f"Dataset not found.\nPlease check this path:\n{file_path}"
    )

except Exception as e:
    raise Exception(f"Error loading dataset: {e}")


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

data.columns = data.columns.str.strip()


# ============================================================
# REQUIRED COLUMNS
# ============================================================

required_columns = [
    "StudentID",
    "AttendanceRate",
    "StudyHoursPerWeek",
    "PreviousGrade",
    "ExtracurricularActivities",
    "ParentalSupport",
    "FinalGrade"
]

missing_columns = [
    column for column in required_columns
    if column not in data.columns
]

if missing_columns:
    raise ValueError(
        f"Required columns are missing: {missing_columns}\n\n"
        f"Available columns:\n{data.columns.tolist()}"
    )


# ============================================================
# DATA CLEANING
# ============================================================

data = data.drop_duplicates()

data = data.dropna(
    subset=["FinalGrade"]
)

numeric_columns = [
    "AttendanceRate",
    "StudyHoursPerWeek",
    "PreviousGrade",
    "FinalGrade"
]

for column in numeric_columns:
    data[column] = pd.to_numeric(
        data[column],
        errors="coerce"
    )

data = data.dropna(
    subset=numeric_columns
)


# ============================================================
# FEATURES AND TARGET
# ============================================================

features = [
    "AttendanceRate",
    "StudyHoursPerWeek",
    "PreviousGrade",
    "ExtracurricularActivities",
    "ParentalSupport"
]

target = "FinalGrade"

X = data[features]
y = data[target]


# ============================================================
# NUMERICAL AND CATEGORICAL FEATURES
# ============================================================

numeric_features = [
    "AttendanceRate",
    "StudyHoursPerWeek",
    "PreviousGrade"
]

categorical_features = [
    "ExtracurricularActivities",
    "ParentalSupport"
]


# ============================================================
# PREPROCESSING
# ============================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)


# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# MODEL
# ============================================================

model = Pipeline(
    steps=[
        (
            "preprocessor",
            preprocessor
        ),
        (
            "regressor",
            LinearRegression()
        )
    ]
)


# ============================================================
# TRAIN MODEL
# ============================================================

model.fit(
    X_train,
    y_train
)


# ============================================================
# MODEL PREDICTION
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# MODEL METRICS
# ============================================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)


# ============================================================
# ACTUAL VS PREDICTED
# ============================================================

comparison = pd.DataFrame({
    "Actual Final Grade": y_test.values,
    "Predicted Final Grade": y_pred
})

comparison["Difference"] = (
    comparison["Actual Final Grade"]
    - comparison["Predicted Final Grade"]
)

comparison = comparison.reset_index(drop=True)


# ============================================================
# DROPDOWN VALUES
# ============================================================

extracurricular_choices = sorted(
    data["ExtracurricularActivities"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)

parental_support_choices = sorted(
    data["ParentalSupport"]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_student(
    attendance,
    study_hours,
    previous_grade,
    extracurricular,
    parental_support
):

    # --------------------------------------------------------
    # INPUT DATA
    # --------------------------------------------------------

    input_data = pd.DataFrame({
        "AttendanceRate": [attendance],
        "StudyHoursPerWeek": [study_hours],
        "PreviousGrade": [previous_grade],
        "ExtracurricularActivities": [extracurricular],
        "ParentalSupport": [parental_support]
    })


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]

    prediction = float(
        np.clip(
            prediction,
            0,
            100
        )
    )


    # --------------------------------------------------------
    # PERFORMANCE CATEGORY
    # --------------------------------------------------------

    if prediction >= 85:

        performance = "🌟 Excellent Performance"

    elif prediction >= 70:

        performance = "👍 Good Performance"

    elif prediction >= 50:

        performance = "⚠️ Average Performance"

    else:

        performance = "❌ Poor Performance"


    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    recommendations = []


    if attendance < 75:

        recommendations.append(
            "📝 Improve attendance to at least 75%."
        )


    if study_hours < 10:

        recommendations.append(
            "📚 Increase weekly study hours."
        )


    if previous_grade < 60:

        recommendations.append(
            "🎯 Focus on improving your previous academic grade."
        )


    if str(extracurricular).lower() in [
        "no",
        "none"
    ]:

        recommendations.append(
            "🏆 Consider participating in extracurricular activities."
        )


    if str(parental_support).lower() in [
        "low",
        "none"
    ]:

        recommendations.append(
            "👨‍👩‍👧 Seek additional academic support and guidance."
        )


    if len(recommendations) == 0:

        recommendations_text = (
            "🎉 Great! Your academic indicators look good."
        )

    else:

        recommendations_text = "\n".join(
            "👉 " + recommendation
            for recommendation in recommendations
        )


    # --------------------------------------------------------
    # SUMMARY
    # --------------------------------------------------------

    summary = pd.DataFrame({
        "Parameter": [
            "Attendance Rate",
            "Study Hours Per Week",
            "Previous Grade",
            "Extracurricular Activities",
            "Parental Support",
            "Predicted Final Grade",
            "Performance"
        ],

        "Value": [
            f"{attendance}%",
            f"{study_hours} hours",
            f"{previous_grade}",
            extracurricular,
            parental_support,
            f"{prediction:.2f}/100",
            performance
        ]
    })


    return (
        f"{prediction:.2f}/100",
        performance,
        recommendations_text,
        summary
    )


# ============================================================
# GRADIO INTERFACE
# ============================================================

with gr.Blocks(
    title="Student Performance Checker"
) as demo:

    gr.Markdown(
        """
        # 🎓 Student Performance Checker

        ### Predict student Final Grade using Machine Learning

        This application uses **Multiple Linear Regression**
        with academic and lifestyle parameters.
        """
    )


    # ========================================================
    # MODEL INFORMATION
    # ========================================================

    with gr.Row():

        gr.Markdown(
            f"""
            ### 📊 Model Information

            **Algorithm:** Multiple Linear Regression

            **Training Records:** {len(X_train)}

            **Testing Records:** {len(X_test)}

            **Features:** {len(features)}

            **Target:** FinalGrade
            """
        )

        gr.Markdown(
            f"""
            ### 📈 Model Performance

            **R² Score:** {r2:.2f}

            **MAE:** {mae:.2f}

            **RMSE:** {rmse:.2f}
            """
        )


    # ========================================================
    # DATASET
    # ========================================================

    gr.Markdown("## 📋 Student Dataset")

    dataset_table = gr.Dataframe(
        value=data,
        interactive=False
    )


    # ========================================================
    # ACTUAL VS PREDICTED
    # ========================================================

    gr.Markdown("## 📊 Actual vs Predicted Final Grade")

    comparison_table = gr.Dataframe(
        value=comparison,
        interactive=False
    )


    # ========================================================
    # STUDENT INPUT
    # ========================================================

    gr.Markdown(
        """
        ## 👨‍🎓 Check Student Performance

        Enter the student's information below.
        """
    )


    with gr.Row():

        with gr.Column():

            attendance = gr.Slider(
                minimum=0,
                maximum=100,
                value=75,
                step=1,
                label="📝 Attendance Rate (%)"
            )

            study_hours = gr.Slider(
                minimum=0,
                maximum=100,
                value=15,
                step=1,
                label="📚 Study Hours Per Week"
            )

            previous_grade = gr.Slider(
                minimum=0,
                maximum=100,
                value=70,
                step=1,
                label="🎯 Previous Grade"
            )


        with gr.Column():

            extracurricular = gr.Dropdown(
                choices=extracurricular_choices,
                value=extracurricular_choices[0],
                label="🏆 Extracurricular Activities"
            )

            parental_support = gr.Dropdown(
                choices=parental_support_choices,
                value=parental_support_choices[0],
                label="👨‍👩‍👧 Parental Support"
            )


    # ========================================================
    # BUTTON
    # ========================================================

    predict_button = gr.Button(
        "🔮 Check Student Performance",
        variant="primary"
    )


    # ========================================================
    # RESULT
    # ========================================================

    gr.Markdown("## 🎯 Prediction Result")

    with gr.Row():

        prediction_output = gr.Textbox(
            label="Predicted Final Grade",
            interactive=False
        )

        performance_output = gr.Textbox(
            label="Performance",
            interactive=False
        )


    recommendations_output = gr.Textbox(
        label="💡 Personalized Recommendations",
        lines=6,
        interactive=False
    )


    summary_output = gr.Dataframe(
        label="📋 Student Input Summary",
        interactive=False
    )


    # ========================================================
    # BUTTON ACTION
    # ========================================================

    predict_button.click(
        fn=predict_student,

        inputs=[
            attendance,
            study_hours,
            previous_grade,
            extracurricular,
            parental_support
        ],

        outputs=[
            prediction_output,
            performance_output,
            recommendations_output,
            summary_output
        ]
    )


    # ========================================================
    # FOOTER
    # ========================================================

    gr.Markdown(
        """
        ---
        🎓 **Student Performance Checker**

        Built with **Python + Pandas + NumPy + Scikit-learn + Gradio**
        """
    )


# ============================================================
# LAUNCH APPLICATION
# ============================================================

if __name__ == "__main__":

    demo.launch()