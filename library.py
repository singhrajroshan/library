#Library Management System using dictionary
#manu, add  book, show  book, issue  book, return book, records, exit

#database
books = {}
issued_books = {}

#add function
def add_book():
    name = input('Enter Book Name : ')
    if name in books:
        print(name,'is Already Available')
    else:
        books[name] = True
        print(name,'is Added Successfully')

def show_book():
    if books:
        print('Available Books : ')
        for i in books:
            print()
    else:
        print('No Books Available')

def issue_book():
    name = input('Enter Book Name : ')
    if name in books:
        if books[name]:
            books[name] = False
            issued_books[name] = True
            print(name,'is Issued Successfully')
        else:
            print(name,'is Already Issued')
    else:
        print(name,'is Not Available')

def return_book():
    name = input('Enter Book Name : ')
    if name in issued_books:
        if issued_books[name]:
            issued_books[name] = False
            books[name] = True
            print(name,'is Returned Successfully')
        else:
            print(name,'is Already Returned')
    else:
        print(name,'is Not Issued')

def records():
    print('Available Books : ')
    for book in books:
        if books[book]:
            print(book)
    print('Issued Books : ')
    for book in issued_books:
        if issued_books[book]:
            print(book)

def exit():
    print('Thank You for Using Library Management System')
    exit()

while True:
    print('Menu')
    print('1. Add Book')
    print('2. Show Book')
    print('3. Issue Book')
    print('4. Return Book')
    print('5. Records')
    print('6. Exit')
    choice = int(input('Enter Your Choice : '))
    if choice == 1:
        add_book()
    elif choice == 2:
        show_book()
    elif choice == 3:
        issue_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        records()
    elif choice == 6:
        exit()
    else:
        print('Invalid Choice')


#books = {'Python':True,'Java':True,'C++':True}
#issued_books = {'Python':False,'Java':False,'C++':False}
