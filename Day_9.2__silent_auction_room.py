##########################################################################
##  
##  Prasad R. Bhosale 
##  Tuesday (12/04/2022)
##  
##  Day_9.2__silent_auction_room
##  
##########################################################################


from replit import clear
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''




flag = True
bids = {}

def Maxx_bider(bid_record):
    highest = 0
    name = ""
    for i in bid_record:
        bid_value = bid_record[i]
        if bid_value > highest:
            highest = bid_value
            name = i
    print(f"Highest bid is done by : {name} = {highest}")

print(logo)
while(flag!=False):
    print("Welcome to the silent auction.")
    name = input("Enter Your Name : ")
    price = int(input("Enter your bid $ "))
    bids[name] = price
    # print(bids)              

    ch = input("Do you want to continue ? y/n").lower()
    if ch=="n":
        flag = False
    else:
        flag = True
        clear()
Maxx_bider(bids)
