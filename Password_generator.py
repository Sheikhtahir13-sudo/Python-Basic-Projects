# BUILD BY MUHAMMAD TAHIR
# Import
import random

while True:
    try:   #error handling
        a = "== PASSWORD GENERATOR ==\n"
        print(a.center(60))
        name = input("Enter your name: ").lower()
        password = str(input("Enter password length (At least 6 characters): ")).upper()
    
        symbol = input("Enter any symbols: ")
        num = input("Enter any numbers: ")
    
        all = password + name + symbol + num
        reverse = all[::-1]
    
        print(f"Generated password: {reverse}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
        break