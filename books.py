import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('/Users/macbook/Desktop/4th Year/CTE 412/Practical/02220176_Vivek/books.xml')
root = tree.getroot()

# Add a new book
def add_book(title, author, year, isbn):
    book = ET.SubElement(root, 'book')
    ET.SubElement(book, 'title').text = title
    ET.SubElement(book, 'author').text = author
    ET.SubElement(book, 'year').text = year
    ET.SubElement(book, 'isbn').text = isbn

def add_info():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    isbn = input("Enter isbn: ")
    add_book(title, author, year, isbn)
    
# Delete a book by title
def delete_book_by_title(title_to_delete):
    found = False
    for book in root.findall('book'):
        title = book.find('title').text
        if title.strip().lower() == title_to_delete.strip().lower():
            root.remove(book)
            found = True
            print(f"✅ Book titled '{title_to_delete}' deleted.")
            break
    if not found:
        print(f"❌ Book titled '{title_to_delete}' not found.")

# User options
while True:
    print("\nChoose an action:")
    print("1. Add a new book")
    print("2. Delete a book by title")
    print("3. Exit and save")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    
    if choice == '1':
       add_info()
    elif choice == '2':
        title_to_delete = input("Enter the title of the book to delete: ")
        delete_book_by_title(title_to_delete)
    elif choice == '3':
        break
    else:
        print("❗ Invalid choice. Try again.")

# Save XML
xml_file = '/Users/macbook/Desktop/4th Year/CTE 412/Practical/02220176_Vivek/books.xml'
tree.write(xml_file, encoding="utf-8", xml_declaration=True)

# Print final book list
print("\n📚 Final Book List:")
for book in root.findall('book'):
    print(f"Title: {book.find('title').text}")
    print(f"Author: {book.find('author').text}")
    print(f"Year: {book.find('year').text}")
    print(f"isbn: ${book.find('isbn').text}")
    print("-" * 30)