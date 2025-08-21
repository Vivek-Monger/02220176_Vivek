import json

# File path for the JSON data
FILE_PATH = "/Users/macbook/Desktop/4th Year/CTE 412/Practical/02220176_Vivek/Lab 2/books.json"

# Load data from JSON file
def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": [], "total_books": 0, "last_updated": ""}

# Save data to JSON file
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

# Display all books
def read_books(data):
    if not data["books"]:
        print("\nNo books available.\n")
    else:
        for book in data["books"]:
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Available: {book['available']}")

# Add a new book
def create_book(data):
    new_id = max([book["id"] for book in data["books"]], default=0) + 1
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    published_year = int(input("Enter published year: "))
    pages = int(input("Enter number of pages: "))
    isbn = input("Enter ISBN: ")
    available = input("Is the book available? (yes/no): ").strip().lower() == "yes"
    rating = float(input("Enter rating: "))

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "genre": genre,
        "published_year": published_year,
        "pages": pages,
        "isbn": isbn,
        "available": available,
        "rating": rating
    }
    data["books"].append(new_book)
    data["total_books"] += 1
    print("\nBook added successfully!\n")

# Update book details
def update_book(data):
    book_id = int(input("Enter the ID of the book to update: "))
    for book in data["books"]:
        if book["id"] == book_id:
            print(f"Updating book: {book['title']}")
            book["title"] = input("Enter new title (leave blank to keep same): ") or book["title"]
            book["author"] = input("Enter new author (leave blank to keep same): ") or book["author"]
            book["genre"] = input("Enter new genre (leave blank to keep same): ") or book["genre"]
            year = input("Enter new published year (leave blank to keep same): ")
            book["published_year"] = int(year) if year else book["published_year"]
            pages = input("Enter new number of pages (leave blank to keep same): ")
            book["pages"] = int(pages) if pages else book["pages"]
            book["isbn"] = input("Enter new ISBN (leave blank to keep same): ") or book["isbn"]
            avail = input("Is the book available? (yes/no or blank to keep same): ").strip().lower()
            if avail in ["yes", "no"]:
                book["available"] = (avail == "yes")
            rating = input("Enter new rating (leave blank to keep same): ")
            book["rating"] = float(rating) if rating else book["rating"]
            print("\nBook updated successfully!\n")
            return
    print("\nBook not found!\n")

# Delete a book
def delete_book(data):
    book_id = int(input("Enter the ID of the book to delete: "))
    for book in data["books"]:
        if book["id"] == book_id:
            data["books"].remove(book)
            data["total_books"] -= 1
            print("\nBook deleted successfully!\n")
            return
    print("\nBook not found!\n")

# Main menu
def menu():
    data = load_data()
    while True:
        print("\n--- Book Management System ---")
        print("1. View all books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            read_books(data)
        elif choice == "2":
            create_book(data)
            save_data(data)
        elif choice == "3":
            update_book(data)
            save_data(data)
        elif choice == "4":
            delete_book(data)
            save_data(data)
        elif choice == "5":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()