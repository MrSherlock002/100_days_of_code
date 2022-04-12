##########################################################################
##  
##  Prasad R. Bhosale  (328M_Prasad)
##  Tuesday (12/04/2022)
##  
##  Day_10.1__Numeric_Calculator
##  
##########################################################################

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def Addition(a,b):
    return (a+b)

def Subtraction(a,b):
    return (a-b)

def Multiplication(a,b):
    return (a*b)

def Dividation(a,b):
    return (a/b)



def main():
    operations = {'+':Addition, '-':Subtraction,'*': Multiplication, '/': Dividation}
    flag = True
    print(logo)
    while(flag!=False):
        print("Enter which operation do you want to perform \n + for addition \n - for subtraction \n * for Multiplication \n / for dividation")
        ch = input("Enter your choice : ")
        input_1 = float(input("Enter First element : "))
        input_2 = float(input("Enter Second element : "))

        for operation in operations:
            if operation==f"{ch}":
                ans=(operations[operation])(input_1,input_2)
                
                print(f"Your answer is : {ans}")
        print("Enter which operation do you want to perform \n + for addition \n - for subtraction \n * for Multiplication \n / for dividation")
        ch = input("Enter your choice : ")
        input_3 = float(input("Enter third element : "))

        for operation in operations:
            if operation==f"{ch}":
                ans=(operations[operation])(ans,input_3)
                
                print(f"Your answer is : {ans}")
        
        x= input("Do you want to repeat ? (y/n)").lower()
        if x=="n":
            flag=False
        else:
            flag=True
if __name__ == "__main__":
    main()
