shelf_with_books = input().split("&")

while True:
    user_input = input().split(" | ")
    command = user_input[0]
    if command == "Add Book":
        book_title = user_input[1]
        if book_title not in shelf_with_books:
            shelf_with_books.insert(0, book_title)

    elif command == "Take Book":
        book_title = user_input[1]
        if book_title in shelf_with_books:
            shelf_with_books.remove(book_title)

    elif command == "Swap Books":
        book_title_1 = user_input[1]
        book_title_2 = user_input[2]
        if book_title_1 in shelf_with_books and book_title_2 in shelf_with_books:
            idx1 = shelf_with_books.index(book_title_1)
            idx2 = shelf_with_books.index(book_title_2)
            shelf_with_books[idx1], shelf_with_books[idx2] = shelf_with_books[idx2], shelf_with_books[idx1]

    elif command == "Insert Book":
        book_title = user_input[1]
        if book_title not in shelf_with_books:
            shelf_with_books.append(book_title)

    elif command == "Check Book":
        index = int(user_input[1])
        if index in range(len(shelf_with_books)):
            print(shelf_with_books[index])

    elif command == "Done":
        break

print(", ".join(shelf_with_books))
