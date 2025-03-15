# Second program
print("program")
# Task 1 - Part 1: Data Structure

# 1. Create an empty dictionary
books_dict = {}

# Example of adding books to the dictionary:
# 2. Each key should be a book's ISBN (a string).
# 3. Each value should be a tuple containing the following details:
#    * Title (String)
#    * Author (String)
#    * Price (number)
#    * Genres (a set of strings, e.g ({'fiction', 'adventure'}))

# Adding a sample book entry
isbn = "978-3-16-148410-0"
books_dict[isbn] = ("The Great Adventure", "John Doe", 29.99, {"fiction", "adventure"})

# Adding another book entry
isbn2 = "978-1-23-456789-7"
books_dict[isbn2] = ("Python Programming", "Jane Smith", 19.99, {"education", "programming"})

# Displaying the books dictionary
print(books_dict)
# Task 1 - Part 2: Search Books by Author

# Example inventory (Dictionary containing book details)
books_dict = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 29.99, {"fiction", "adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 19.99, {"education", "programming"}),
    "978-0-12-345678-9": ("Learning Python", "John Doe", 25.50, {"education", "programming"}),
    "978-9-87-654321-0": ("Advanced Algorithms", "Jane Smith", 35.00, {"education", "algorithms"})
}

# Function to search books by author
def search_by_author(author):
    # List to store the results (ISBN and Title of books by the author)
    result = []
    
    # Loop through the inventory dictionary
    for isbn, book_details in books_dict.items():
        # If the author matches, add the tuple (ISBN, Title) to the result list
        if book_details[1] == author:
            result.append((isbn, book_details[0]))  # (ISBN, Title)
    
    return result

# Example usage:
author_to_search = "John Doe"
books_by_author = search_by_author(author_to_search)

# Display the result
print(f"Books written by {author_to_search}:")
for isbn, title in books_by_author:
    print(f"ISBN: {isbn}, Title: {title}")
# Task 1 - Part 3: Update Price of a Book

# Example inventory (Dictionary containing book details)
books_dict = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 29.99, {"fiction", "adventure"}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 19.99, {"education", "programming"}),
    "978-0-12-345678-9": ("Learning Python", "John Doe", 25.50, {"education", "programming"}),
    "978-9-87-654321-0": ("Advanced Algorithms", "Jane Smith", 35.00, {"education", "algorithms"})
}

# Function to update price of a book
def update_price(isbn, new_price):
    # Check if the ISBN exists in the inventory
    if isbn in books_dict:
        # Get the current details of the book (Title, Author, Price, Genres)
        book_details = books_dict[isbn]
        
        # Create a new tuple with the updated price
        updated_book_details = (book_details[0], book_details[1], new_price, book_details[3])
        
        # Update the dictionary with the new tuple
        books_dict[isbn] = updated_book_details
        
        print(f"Price for the book with ISBN {isbn} has been updated to {new_price}.")
    else:
        print(f"ISBN {isbn} not found in the inventory.")

# Example usage:
isbn_to_update = "978-3-16-148410-0"
new_price = 34.99
update_price(isbn_to_update, new_price)

# Display updated inventory
print("\nUpdated Inventory:")
for isbn, details in books_dict.items():
    print(f"ISBN: {isbn}, Title: {details[0]}, Price: {details[2]}")
# Task 3 - Part 4: Standardize Book Genres

# Example inventory (Dictionary containing book details)
books_dict = {
    "978-3-16-148410-0": ("The Great Adventure", "John Doe", 29.99, {"fiction", "  adventure "}),
    "978-1-23-456789-7": ("Python Programming", "Jane Smith", 19.99, {"education", " programming "}),
    "978-0-12-345678-9": ("Learning Python", "John Doe", 25.50, {" education ", "programming"}),
    "978-9-87-654321-0": ("Advanced Algorithms", "Jane Smith", 35.00, {"education", "algorithms "})
}

# Function to standardize genres
def standardize_genres():
    # Iterate over each book in the inventory
    for isbn, book_details in books_dict.items():
        # Clean the genres set by converting each genre to lowercase and trimming spaces
        cleaned_genres = {genre.strip().lower() for genre in book_details[3]}
        
        # Create a new tuple with the updated genres set
        updated_book_details = (book_details[0], book_details[1], book_details[2], cleaned_genres)
        
        # Update the dictionary with the new tuple
        books_dict[isbn] = updated_book_details
    
    print("Genres have been standardized.")

# Example usage:
standardize_genres()

# Display the updated inventory with standardized genres
print("\nUpdated Inventory with Standardized Genres:")
for isbn, details in books_dict.items():
    print(f"ISBN: {isbn}, Title: {details[0]}, Genres: {details[3]}")
# Task 1 - Part 5 - Display Inventory

# Create an empty dictionary
books = {}

# Add books to the dictionary
books['978-1-234-56789-0'] = ('Harry Potter', 'J.K. Rowling', 10.99, {'Fantasy', 'Adventure'})
books['978-2-345-67890-1'] = ('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 9.99, {'Fantasy', 'Children'})
books['978-3-456-78901-2'] = ('The Cat in the Hat', 'Dr. Seuss', 7.99, {'Children', 'Humor'})

# Function to display inventory
def display_inventory():
    print("Book Inventory:")
    print("--------------------")
    print("| ISBN          | Title                            | Author            | Price  | Genres         |")
    print("--------------------")
    for isbn, details in books.items():
        title, author, price, genres = details
        print(f"| {isbn} | {title:<30} | {author:<15} | ${price:.2f} | {', '.join(genres):<15} |")
    print("--------------------")

# Call the function
display_inventory()

# Task 1 - Part 6 - List All Book Titles

# Create an empty dictionary
books = {}

# Add books to the dictionary
books['978-1-234-56789-0'] = ('Harry Potter', 'J.K. Rowling', 10.99, {'Fantasy', 'Adventure'})
books['978-2-345-67890-1'] = ('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 9.99, {'Fantasy', 'Children'})
books['978-3-456-78901-2'] = ('The Cat in the Hat', 'Dr. Seuss', 7.99, {'Children', 'Humor'})

# Function to list all book titles
def list_all_books():
    titles = [details[0] for details in books.values()]
    return sorted(titles)

# Call the function
all_books = list_all_books()
print("All Book Titles:")
for title in all_books:
    print(title)