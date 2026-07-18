# BUILD BY MUHAMMAD TAHIR
# Import library
import random

while True:
    try:                                                 # Error handling
        title1 = "== PASSWORD GENERATOR ==\n"   
        print(title1.center(60))

        print("1 - Generate pass")      
        print("2 - Exit\n")

        choice1  = int(input("Enter choice(1-2): "))

        if choice1 == 1:                                 # if-else conditions
            num = random.randint(1,999)
    
            name = input("\nEnter your name (5-digits): ").lower()      # 5-digits name conditon
    
            if len(name) <= 5:
                pass
            else:
                print("Name must be of 5 digits or less!")
                break
    
            short_pass = input("Enter password length (At least 3 characters): ").upper()    # 3-digits pass condition
    
            if len(short_pass) <= 4:
                pass
    
            else:
                print("Password must be of 4 digits or less!")
                break
        
            symbol = input("Enter any 3 symbols (@/#/%): ")               # 3-digits symbol condition
    
            if len(symbol) <= 3:
                pass
    
            else:
                print("symbol must be of 3 digits or less!")
                break
        
            all =  short_pass + symbol + name            
            reverse = all[::-1]                          # reverse string
    
            work = str(num)                # convert int to string
    
            done = reverse + work          # concatenate
            
            print(f"Generated password: {done}")       # password generation complete

        elif choice1 == 2:
            print("Thanks for using this program:)")        # Exiting program

        else:
            print("Invalid option!")      # non-valid condition
            break
        
    except Exception as e:              
        print(f"Error occurred: {e}")
        break
