# BUILD BY MUHAMMAD TAHIR
# Import library
import time

Username = "Tahir_17"            # Store data into variables for admin verification
Password = "786125"

Customer_info = []          # Empty lists to store info
sells = []

Books = [                         # Five books info store in list
    {
        "Book_ID": 101,
        "Title": "Python",
        "Author": "Ali",
        "Category": "Programming",
        "Price": 1400,
        "Quantity": 10
    },
    {
        "Book_ID": 102,
        "Title": "Java",
        "Author": "Ahmed",
        "Category": "Programming",
        "Price": 1500,
        "Quantity": 13
    },
    {
        "Book_ID": 103,
        "Title": "Python Programming",
        "Author": "John Zelle",
        "Category": "Programming",
        "Price": 1800,
        "Quantity": 15
    },
    {
        "Book_ID": 104,
        "Title": "Data Structures",
        "Author": "Mark Allen Weiss",
        "Category": "Computer Science",
        "Price": 2200,
        "Quantity": 8
    },
    {
        "Book_ID": 105,
        "Title": "Machine Learning Basics",
        "Author": "Aurélien Géron",
        "Category": "Artificial Intelligence",
        "Price": 3500,
        "Quantity": 9
    }
]

def Admin():                        # Admin function
    while True:
        try:
            username = input("\nEnter username: ")
            password = input("Enter password: ")

            print("\n Verification Loading... \n")
            time.sleep(3)

            if username == Username and password == Password:            # Password verification
                print("Login Successfully:)\n")
                break

            elif username != Username and password == Password:
                print("Invalid Username try again please...\n")

            elif username == Username and password != Password:
                print("Invalid Password try again please...\n")

            else:
                print("Invalid Username and Password try again please...\n")

        except Exception as e:
            print(f"Error occured: {e}.")

def Add_Books():                                  # New books for adding into stock
    try:
        title3 = "== ADD Books ==\n"
        print(title3.center(50))

        book_id = int(input("Enter book_id: "))
                
        new_book = {
            "Book_ID": book_id,             # Take input to store in the list
            "Title": input("Enter Title: "),
            "Auther": input("Enter Auther: "),
            "Category": input("Enter Category: "),
            "Price": int(input("Enter Price: ")),
            "Quantity": int(input("Enter Quantity:"))
        }

        for book in Books:
            if book["Book_ID"] == book_id:
                print("\nBook already in the stock\n")
                break

        else:
            print("\n Loading... \n")
            time.sleep(3)

            Books.append(new_book)                # Append in the list
            print("Book added succesfully:)\n")

    except Exception as e:
        print(f"Error occured: {e}.")

def All_Books():
    try:
        title3 = "== Display All Books ==\n"
        print(title3.center(50))

        print("\n Loading... \n")
        time.sleep(3)

        for i in Books:     # loop for print each book info step by step
            print("------------------------------------------------------------------------------------------------------------------------------")
            print(i)
            print("------------------------------------------------------------------------------------------------------------------------------\n")
            
    except Exception as e:
        print(f"Error occured: {e}.")

def Remove_Books():                                  # Removing specific book record
    try:
        title4 = "== Delete Books Record ==\n"
        print(title4.center(50))

        book_id = int(input("\nEnter book id: "))

        print("\n Loading... \n")
        time.sleep(3)

        for book in Books:
            if book["Book_ID"] == book_id:            # Checking  book id to remove that record
                Books.remove(book)
                print("Book deleted succesfully:)\n")
                break
        else:
            print("Book not found")

    except Exception as e:
            print(f"Error occured: {e}.")

def Buy_Books():                                            # Buying a book 
    while True:
        try:
            title5 = "== Purchase Books ==\n"
            print(title5.center(50))

            title = input("Enter book title: ")

            purchase = {
                "Buyer_Name": input("Enter Buyer Name: "),      # input to store buyer info into list
                "Phone": input("Enter Phone Number: "),
                "Book_title": title
            }

            Customer_info.append(purchase)      # append input data into list

            print("\n Loading... \n")
            time.sleep(3)

            for book in Books:
                if book["Title"] == title:    # loop to check book title in the list

                    if book["Quantity"] > 0:
                        book["Quantity"] -= 1
                        sells.append(book["Price"])

                        print("------------------------------------------")     # Final bill info
                        print(book)
                        date1 = time.strftime("%d-%m-%Y")
                        print(f"\nToday date = {date1}")
                        print("\nBook purchased successfully :)")
                        print("------------------------------------------\n")

                    else:
                        print("Book is out of stock!")
                    return

            print("Book not found")
            return

        except Exception as e:
            print(f"Error occurred: {e}")

def Sells():                                            # sum of all book amount that sells today
    try: 
        title6 = "== Selling Amount ==\n"                                  
        print(title6.center(50))
    
        Total = sum(sells)         
        print(f"Total selling amount = {Total}\n")

    except Exception as e:
        print(f"Error occured: {e}.")

def customer_info():                          
    try:
        title7 = "== Customer Info ==\n"
        print(title7.center(50))

        for i in Customer_info:                                       # loop for print each customer info that buy the books
            print("---------------------------------------------------------------------")
            print(i)
            print("---------------------------------------------------------------------\n")

    except Exception as e:
        print(f"Error occured: {e}.")
            
def main():               
    while True:
        try:
            print("=" * 50)
            title1 = "LIBRARY MANAGEMENT SYSTEM"
            print(title1.center(50))
            print("=" * 50)

            title2 = "== ADMIN LOGIN ==\n"
            print(title2.center(50))

            date2 = time.strftime("%d-%m-%Y")                     # show today date
            print(f"Date = {date2}")

            day = time.strftime("%A")
            print(f"Day = {day}")

            current_time = time.strftime("%H:%M:%S")           # show the current time
            print(f"Current time = {current_time}\n")  

            print("1 - Admin login")
            print("2 - Logout\n")

            choice1 = int(input("Enter choice(1-2): "))

            if choice1 == 1:
                Admin()
                while True:
                    title3 = "== Library System Menu ==\n"
                    print(title3.center(50))

                    print("1 - Add new books record")       # Categories
                    print("2 - Display all books")
                    print("3 - Delete books record")
                    print("4 - Purchase books")
                    print("5 - View total amount")
                    print("6 - Customer info")
                    print("7 - Exit\n")

                    choice2 = int(input("Enter choice(1-6): "))
                                                                        # if-else condition
                    if choice2 == 1:
                        Add_Books()

                    elif choice2 == 2:
                        All_Books()

                    elif choice2 == 3:
                        Remove_Books()

                    elif choice2 == 4:
                        Buy_Books()

                    elif choice2 == 5:
                        Sells()

                    elif choice2 == 6:
                        customer_info()

                    elif choice2 == 7:
                        print("\nThanks for using Library managemnt system:)\n")
                        break

                    else:
                        print("\nInvalid option.\n")
                        break

            elif choice1 == 2:
                print("\nThanks for using this program:)\n")
                break

            else:
                print("\nInvalid option.\n")
                break 

        except Exception as e:
            print(f"Error occured: {e}.")
            break
                       # main engine
main()
