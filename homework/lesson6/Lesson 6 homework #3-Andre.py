user1 = "Billy Bob Joe III"
user2 = "Jhonny Didn't Eat Sugar"
user3 = "Shotgun Hacker"
userlogin = input("What is your username? ")
if userlogin == "Billy Bob Joe III":
    print("Welcome Billy.")
    Retirement_Savings = dict({1776 : 999999999})
    Vacation_Budget = dict({1917 : 500000})
    Gaming_Budget = dict({2012 : 1000000})
    user1accountnames = {00 : "Retirement_Savings" , 0o01 : "Vacation_Budget" , 0o02 : "Gaming_Budget"}
    user1accounts = {00 : Retirement_Savings , 0o01 : Vacation_Budget , 0o02 : Gaming_Budget}
    user1input = input("What is the ID of the account you want to open? ")
    print("Account: " + user1accountnames.get(int(user1input)))
    user1accounts = user1accounts.get(int(user1input))
    accountbalance1 = user1accounts.get(int(input("What is your password? ")))
    if accountbalance1 == None:
        while accountbalance1 == None:
            print("The password you entered is incorrect. Please try again.")
            accountbalance1 = user1accounts.get(int(input("What is your password? ")))
            print("$" + str(accountbalance1))
    else:
        print("$" + str(accountbalance1))
   
elif userlogin == "Johnny Didn't Eat Sugar":
    print("Welcome Johnny.")
    Stocking_Sugar_Budget = dict({19217117 : 100000000000000000000})
    Bribe_Papa_Budget = dict({1415 : 999999999})
    Taxi_Escape_Budget = dict({172114 : 999})
    user2accountnames = {0o03 : "Stocking_Sugar_Budget" , 0o04 : "Bribe_Papa_Budget" , 0o05 : "Taxi_Escape_Budget"}
    user2accounts = {0o03 : Stocking_Sugar_Budget , 0o04 : Bribe_Papa_Budget, 0o05 : Taxi_Escape_Budget}
    user2input = input("What is the ID of the account you want to open? ")
    print("Account: " + user2accountnames.get(int(user2input)))
    user2accounts = user2accounts.get(int(user2input))
    accountbalance2 = user2accounts.get(int(input("What is your password? ")))
    if accountbalance2 == None:
        while accountbalance2 == None:
            print("The password you entered is incorrect. Please try again.")
            accountbalance2 = user2accounts.get(int(input("What is your password? ")))
            print("$" + str(accountbalance2))
    else:
        print("$" + str(accountbalance2))

elif userlogin == "Shotgun Hacker":
    Hacking_For_Sore_Losers_Income = {1112 : 25}
    Google_Job_Income = {133214 : 121512}
    New_PCs_For_Development_Team = {131319 : 7500}
    user3accountnames = {0o06 : "Hacking_For_Sore_Losers_Income" , 0o07 : "Google_Job_Income" , 10 : "New_PCs_For_Development_Team"}
    user3accounts = {0o06 : Hacking_For_Sore_Losers_Income , 0o07 : Google_Job_Income , 10 : New_PCs_For_Development_Team}
    user3input = input("What is the ID of the account you want to open? ")
    print("Account: " + str(user3accountnames.get(int(user3input))))
    user3accounts = user3accounts.get(int(user3input))
    accountbalance3 = user3accounts.get(int(input("What is your password? ")))
    if accountbalance3 == None:
        while accountbalance3 == None:
            print("The password you entered is incorrect. Please try again.")
            accountbalance3 = user3accounts.get(int(input("What is your password? ")))
            print("$" + str(accountbalance3))
    else:
        print("$" + str(accountbalance3))


else:
    print("This account does not exist at this time.")
   









#P.S. Jhonny's SugarSpending Budget's password is the numerical version of sugar if a = 1, b = 2, c = 3, etc. (19 = s, 21 = u, 7 = g, 1 = a, 17 = r). His other passwords are words too. 
#(Also, the other passwords have hidden meanings too, but are not necessarily words)