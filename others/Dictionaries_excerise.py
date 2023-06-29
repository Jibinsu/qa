#dictionary of books with authors
books = {
    'J.K Rowling': ['Harry Potter and the Chamber of Secrets', 'Harry Potter and the Order of the Phoenix', 'Harry Potter and the Cursed Child', 'Harry Potter and the Philosophers Stone', 'Harry Potter and the Prisoner of Azkaban'],
    'Shakespeare': ['Hamlet', 'A Midsummer Nights Dream', 'Romeo and Juliet', 'Macbeth', 'Othello'],
    'Roald Dahl': ['The Witches', 'Danny the Champion of the World', 'James and the Giant Peach', 'Matilda', 'Charlie and the Chocolate Factory'],
    'Stephen King': ['IT', 'The Shining', 'The Green Mile', 'Misery', 'The Stand']
}

# Asking for the author's name
author_name = input("Enter the author's name: ")

# Getting the list of books written by authors name
books_by_author = books.get(author_name)

# Printing the list of books as a string using the .join() method
book_list = '\n'.join(books_by_author)
print(f"Books by {author_name}:\n{book_list}")