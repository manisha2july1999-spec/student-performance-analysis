# import os

# filename = "library.txt"

# # Create file if it does not exist
# if not os.path.exists(filename):
#     open(filename, "w").close()

# def add_book():
#     try:
#         book = input("Enter book name: ")
#         with open(filename, "a") as f:
#             f.write(book + "\n")
#         print("Book added successfully.")
#     except Exception as e:
#         print("Error:", e)

# def view_books():
#     try:
#         with open(filename, "r") as f:
#             books = f.readlines()

#         if len(books) == 0:
#             print("No books available.")
#         else:
#             print("\nAvailable Books:")
#             for i, book in enumerate(books, start=1):
#                 print(i, ".", book.strip())
#     except FileNotFoundError:
#         print("Library file not found.")
#     except Exception as e:
#         print("Error:", e)

# def issue_book():
#     try:
#         book_name = input("Enter book name to issue: ")

#         with open(filename, "r") as f:
#             books = f.readlines()

#         found = False
#         with open(filename, "w") as f:
#             for book in books:
#                 if book.strip().lower() == book_name.lower() and not found:
#                     found = True
#                 else:
#                     f.write(book)

#         if found:
#             print("Book issued successfully.")
#         else:
#             print("Book not found.")

#     except Exception as e:
#         print("Error:", e)

# def return_book():
#     try:
#         book_name = input("Enter book name to return: ")

#         with open(filename, "a") as f:
#             f.write(book_name + "\n")

#         print("Book returned successfully.")

#     except Exception as e:
#         print("Error:", e)

# while True:
#     print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
#     print("1. Add Book")
#     print("2. View Books")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Exit")

#     try:
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             add_book()

#         elif choice == 2:
#             view_books()

#         elif choice == 3:
#             issue_book()

#         elif choice == 4:
#             return_book()

#         elif choice == 5:
#             print("Thank You!")
#             break

#         else:
#             print("Invalid choice.")

#     except ValueError:
#         print("Please enter a valid number.")


# def library():
#     print("""
#            1 -> Add Book
#            2 -> View Books
#            3 -> Search Book
#            4 -> Issue Book
#            5 -> update
#            6 -> Exit
#           """)
#     try:
#         ch = int(input("Enter your choice: "))
#         return ch
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         return None

# choice = library()

# if choice == 1:
#     print("Add Book Selected")
# elif choice == 2:
#     print("View Books Selected")
# elif choice == 3:
#     print("Search Book Selected")
# elif choice == 4:
#     print("Issue Book Selected")
# elif choice == 5:
#     print("update")
# elif choice == 6:
#     print("Exiting Program")
# elif choice is not None:
#     print("Invalid Choice")

# def add_book():
#     try:
#         book = input("Enter book name: ")

#         with open("library.txt", "a") as f:
#             f.write(book + "\n")

#         print("Book added successfully.")

#     except Exception as e:
#         print("Error:", e)


# def view_books():
#     try:
#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         if len(books) == 0:
#             print("No books available.")
#         else:
#             print("\nAvailable Books:")
#             for i, book in enumerate(books, start=1):
#                 print(i, ".", book.strip())

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)


# def search_book():
#     try:
#         name = input("Enter book name to search: ")

#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         found = False

#         for book in books:
#             if name.lower() == book.strip().lower():
#                 found = True
#                 break

#         if found:
#             print("Book found.")
#         else:
#             print("Book not found.")

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)


# def issue_book():
#     try:
#         name = input("Enter book name to issue: ")

#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         found = False

#         with open("library.txt", "w") as f:
#             for book in books:
#                 if book.strip().lower() != name.lower():
#                     f.write(book)
#                 else:
#                     found = True

#         if found:
#             print("Book issued successfully.")
#         else:
#             print("Book not found.")

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)




# def add_book():
#     try:
#         book = input("Enter book name: ")

#         with open("library.txt", "a") as f:
#             f.write(book + "\n")

#         print("Book added successfully.")

#     except Exception as e:
#         print("Error:", e)


# def view_books():
#     try:
#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         if len(books) == 0:
#             print("No books available.")
#         else:
#             print("\nAvailable Books:")
#             for i, book in enumerate(books, start=1):
#                 print(i, ".", book.strip())

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)


# def search_book():
#     try:
#         name = input("Enter book name to search: ")

#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         found = False

#         for book in books:
#             if name.lower() == book.strip().lower():
#                 found = True
#                 breakw3w

#         if found:
#             print("Book found.")
#         else:
#             print("Book not found.")

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)


# def issue_book():
#     try:
#         name = input("Enter book name to issue: ")

#         with open("library.txt", "r") as f:
#             books = f.readlines()

#         found = False

#         with open("library.txt", "w") as f:
#             for book in books:
#                 if book.strip().lower() != name.lower():
#                     f.write(book)
#                 else:
#                     found = True

#         if found:
#             print("Book issued successfully.")
#         else:
#             print("Book not found.")

#     except FileNotFoundError:
#         print("Library file does not exist.")

#     except Exception as e:
#         print("Error:", e)


# def library():
#     print("""
#            1 -> Add Book
#            2 -> View Books
#            3 -> Search Book
#            4 -> Issue Book
#            5 -> Update
#            6 -> Exit
#           """)

#     try:
#         ch = int(input("Enter your choice: "))
#         return ch

#     except ValueError:
#         print("Invalid input! Please enter a number.")
#         return None


# choice = library()

# if choice == 1:
#     add_book()

# elif choice == 2:
#     view_books()

# elif choice == 3:
#     search_book()

# elif choice == 4:
#     issue_book()

# elif choice == 5:
#     print("Update Function Coming Soon")

# elif choice == 6:
#     print("Exiting Program")

# elif choice is not None:
#     print("Invalid Choice")


# import tkinter as tk
# from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

# Add Book
def add_book():
    try:
        book = entry_book.get()

        if book == "":
            raise ValueError("Book name cannot be empty!")

        with open("library.txt", "a") as file:
            file.write(book + "\n")

        messagebox.showinfo("Success", "Book Added Successfully")
        entry_book.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# View Books
def view_books():
    try:
        listbox.delete(0, tk.END)

        with open("library.txt", "r") as file:
            books = file.readlines()

        if not books:
            messagebox.showinfo("Info", "No Books Available")
        else:
            for book in books:
                listbox.insert(tk.END, book.strip())

    except FileNotFoundError:
        messagebox.showwarning("Warning", "Library File Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Search Book
def search_book():
    try:
        book_name = entry_book.get()

        with open("library.txt", "r") as file:
            books = file.readlines()

        found = False

        for book in books:
            if book_name.lower() == book.strip().lower():
                found = True
                break

        if found:
            messagebox.showinfo("Found", "Book Available in Library")
        else:
            messagebox.showinfo("Not Found", "Book Not Available")

    except FileNotFoundError:
        messagebox.showwarning("Warning", "Library File Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Delete Book
def delete_book():
    try:
        book_name = entry_book.get()

        with open("library.txt", "r") as file:
            books = file.readlines()

        found = False

        with open("library.txt", "w") as file:
            for book in books:
                if book.strip().lower() != book_name.lower():
                    file.write(book)
                else:
                    found = True

        if found:
            messagebox.showinfo("Success", "Book Deleted Successfully")
        else:
            messagebox.showinfo("Info", "Book Not Found")

        entry_book.delete(0, tk.END)

    except FileNotFoundError:
        messagebox.showwarning("Warning", "Library File Not Found")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Window
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x500")
root.configure(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=10)

# Label
lbl = tk.Label(
    root,
    text="Enter Book Name",
    font=("Arial", 14),
    bg="lightblue"
)
lbl.pack()

# Entry Box
entry_book = tk.Entry(root, font=("Arial", 14), width=30)
entry_book.pack(pady=10)

# Buttons
btn_add = tk.Button(root, text="Add Book", font=("Arial", 12),
                    width=15, command=add_book)
btn_add.pack(pady=5)

btn_view = tk.Button(root, text="View Books", font=("Arial", 12),
                     width=15, command=view_books)
btn_view.pack(pady=5)

btn_search = tk.Button(root, text="Search Book", font=("Arial", 12),
                       width=15, command=search_book)
btn_search.pack(pady=5)

btn_delete = tk.Button(root, text="Delete Book", font=("Arial", 12),
                       width=15, command=delete_book)
btn_delete.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)

root.mainloop()