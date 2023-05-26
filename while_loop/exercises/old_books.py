book_name = input()
current_book = input()

books_counter = 0
flag = False

while current_book != "No More Books":
    if current_book == book_name:
        flag = True
        print(f"You checked {books_counter} books and found it.")
        break

    books_counter += 1
    current_book = input()

if not flag:
    print(f"The book you search is not here!\nYou checked {books_counter} books.")