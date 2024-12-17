import os
def act1():
    print("Hello world")

def act2():
    name = input("Hi "+"Malen")

def act3():
    fullname = input("Please input your full name : ")
    gender = input("Input your Gender : ")
    age = input("Input your Age : ")
    status = input("Input your Status : ")
    BirthMonth = input("Input your Birth Month : ")
    BirthDay = input("Input your Birth Day : ")
    BirthYear = input("Input your Birth Year : ")
    religion = input("Input your Religion : ")
    nationality = input("Input your Nationality : ")
    fname = input("Input your Father's Name : ")
    mname = input("Input your Mother's Name : ")
    EmailAddress = input("Input your Email Address : ")
    address = input("Input your Address : ")

    print("\nHi, My name is",fullname,"\b, an",age,"year old",gender,"\b,",status,"\b, born on",BirthMonth, BirthDay, BirthYear,"\b, living in",address,"\b.\nI am a",nationality,"citizen and a",religion,"\b.\nMy father's name is",fname,"and my mother's name is",mname,"\b.\nYou can reach me through gmail at",EmailAddress)

def act4():
    number1 = eval(input("Enter a number ---> "))
    number2 = eval(input("Enter another number ---> "))
    answer = number1 + number2
    print("The sum of", number1, "and", number2, "is", answer)

def act5():
    print("Fahrenheit to Celsius Converter Program")
    F = eval(input("Enter temperature in Fahrenheit : "))

    C = (F-32) * 5 / 9
    print("The conversion of", F, "degrees Fahrenheit is", C, "degrees Celsius.")


    print(f"The conversion of {F} degrees Fahrenheit is {round(C,2)} degrees Celsius.")

def act6():
    x = 5
    print(x)
    x = x + 10
    print(x)

    #simplified version
    x += 20
    print(x)

    x-= 15
    print(x)

def act7():
    #conditional statements
    gold = 0
    miner = input("Hi, Please enter your name ---> ")
    #answerable by yes or no
    hasMine = input("Did you mine gold today? ")

    if hasMine.lower()== "yes":
        gold += 1
        print(f"Hi {miner}, Today you have total of {gold} gold")
    elif hasMine.lower() == "no":
        gold -= 1
        print(f"Hi {miner}, Today you have total of {gold} gold")
    else:
        print(f"Hi {miner}, Today you have total of {gold} gold, try again")

def act8():
    password = input("Enter your password: ")
    if password == "malen21" :
        print("bomba na!")
        print("galing mo")
    elif password == "ateganda" :
        print("perfect!")
    else:
        print("try again")
    print("Thank you!")

def act9():
    age = eval(input("Enter your age: "))

    if 1 <= age <= 7:
        print("The age you enter is considered as Toddler")
    elif 8<= age <= 13:
        print("The age you enter is considered as Pre teen")
    elif 14<= age <= 18:
        print("The age you enter is considered as Teenager")
    elif 19 <= age <=31:
        print("The age you enter is considered as Early Adulthood")
    elif 32 <= age <= 45:
        print("The age you enter is considered as Mid Adulthood")
    elif 46 <= age <=59:
        print("The age you enter is considered as Post Adulthood")
    elif 60 <= age <= 100:
        print("The age you enter is considered as Senior")
    else:
        print("Invalid Age")

def act10():
    DLL = input("Are you a current student of DLL (yes/no): ")
    if DLL.lower() == "yes":
        print("Welcome to DLL scholarship form")
        CC = input("Are you from Brgy. Cotta? (yes/no): ")
        if CC.lower() == "yes":
            print("Please fill up the next form")
            level = input("What is your current year level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer: ")
            if level.lower() == 'f' :
                print("Hi, Freshmen")
            elif level.lower() == 's' :
                print("Hi, Sophomore")
            elif level.lower() == 'j' :
                print("Hi, Junior")
            elif level.lower() == 'r' :
                print("Hi, Senior")
            else:
                print("Invalid Answer")
            scho = input("Do you need this scholarship (yes/no) : ")
            if scho.lower() == "yes":
                print("Scholarship Granted")
            else:
                print("Thank you for stopping by")
        else:
            print("Sorry, this scholarship is available only for residents of Cotta")
    else:
        print("Thank you for stopping by")

def act11():
    #print hello world 10 times
    for ovo in range (1,11):
        print(ovo,"hello world")

def act12():
    #starting point 10
    #ending point 1

    for cycle in range (10,0,-1):
        print(f"Input #{cycle}")

def act13():
    #factorial
    x = 1
    num = eval(input("Enter a number: "))
    for fm in range(num,0,-1): 
        x *= fm
    print(f"The factorial of {num} is {x}")

def act14():
    for x in range(0,11):
        print(x, end=" ")
        for y in range(0,11):
            print("<3", end=" ")
        print()

def act15():
    # num = eval(input("Enter a number: "))
    for x in range(6,0,-1):
        for y in range(1, x + 1):
            print(" ", end=" ")
        for x in range(6,y ,- 1):
            print("*", end=" ")
        print()

def act16():
    for x in range (1,6):
        for y in range(1, x + 1):
            print(" ", end = " ")
        for z in range(6,x,-1):
            print(" * ", end=" ")
        print()

def act17():
    col = eval(input("Enter the number of columns: "))
    for x in range(1,11):
        for y in range(1, col + 1):
            print(f"{x} x {y} = {x*y}", end="\t")
        print()

def act18():
    tri = eval(input("Enter numbers of triangles: "))

    for x in range(1,6):
        for r in range(1,tri +1):
            for y in range(1, x + 1):
                print("*", end = " ")
            for z in range(5, x, -1):
                print(" ", end=" ")
        print()

def act19():
    go = True

    while go == True:
        name = input("Enter your name here --->")
        if name.lower() == "stop":
            print("Program terminated")
            break
        else:
            continue

def act20():
    import os
    isContinue = True 
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle? (yes/no)---> ")
        
        if ask.lower() == "no":
            print("Program stopped")
            break
            iscontinue = False
        elif ask.lower() == "yes":
            os.system("cls")
            no += 1
            for x in range(1,6):
                for r in range(1,no +1):
                    for y in range(1, x + 1):
                        print("*", end = " ")
                    for z in range(5, x, -1):
                        print(" ", end=" ")
                print()
            continue

def act21():
    def pang_hello():
        print("Hello BSIT-1C")
    pang_hello()

    #with paraneter

    def pang_hello2(name):
        print(f"Hello {name}!")
    pang_hello2("malen")


    tuloy = True
    while tuloy == True:
        ask = input("Please input your name ---> ")
        if ask.lower() == "stop":
            print("Program stopped")
            print("Thank you!")
            break
        else:
            pang_hello2(ask)

def act22():
    import os
    act = True
    while act == True:
        ask = input("Would you like to see activity 5? (yes/no)---> ")
        if ask.lower() == "yes":
            os.system("cls")
            number1 = eval(input("Enter a number ---> "))
            number2 = eval(input("Enter another number ---> "))
            answer = number1 + number2
            print("The sum of", number1, "and", number2, "is", answer)
            continue
        else:
            print("Program stopped")
            break

def act23():
    def factorial(number):
        fact = 1
        for x in range(number, 0, -1):
            fact *= x

        return fact

    print(f"The factorial of 5 is {factorial(5)}")

def act24():
    from activity23_sample import factorial

    print(f"the factorial of 7 is {factorial(7)} ")

def act25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

def code1():
    print ("\t\t\t\t\t\t\t\t\t   * \n\t\t\t\t\t\t\t\t\t  *** \n\t\t\t\t\t\t\t\t\t ***** \n\t\t\t\t\t\t\t\t\t******* \n\t\t\t\t\t\t\t\t\t ***** \n\t\t\t\t\t\t\t\t\t  *** \n\t\t\t\t\t\t\t\t\t   *")

def code2():
    name = input("Please enter a name -----> ")

    print("Hi", name)
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t*\t\t    ","Hi", name,"\t\t\t*\t\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t\t*\n\n")

def code3():
    fullname = input("Please input your full name : ")
    gender = input("Input your Gender : ")
    age = input("Input your Age : ")
    status = input("Input your Status : ")
    BirthMonth = input("Input your Birth Month : ")
    BirthDay = input("Input your Birth Day : ")
    BirthYear = input("Input your Birth Year : ")
    religion = input("Input your Religion : ")
    nationality = input("Input your Nationality : ")
    fname = input("Input your Father's Name : ")
    mname = input("Input your Mother's Name : ")
    EmailAddress = input("Input your Email Address : ")
    address = input("Input your Address : ")

    print("\nHi, My name is",fullname,"\b, an",age,"year old",gender,"\b,",status,"\b, born on",BirthMonth, BirthDay, BirthYear,"\b, living in",address,"\b.\nI am a",nationality,"citizen and a",religion,"\b.\nMy father's name is",fname,"and my mother's name is",mname,"\b.\nYou can reach me through gmail at",EmailAddress)

def code4():
    num1 = eval(input("Enter a number ---> "))
    num2 = eval(input("Enter another number ---> "))
    sum = num1 + num2
    diff = num1 - num2
    prod = num1 * num2
    quo =  num1 / num2
    expo = num1 ** num2
    rem = num1 % num2
    floordiv = num1 // num2

    print("The sum of" , num1 , "and" , num2 , "is" ,sum)
    print("The difference of" , num1 , "and" , num2 , "is" ,diff)
    print("The product of" , num1 , "and" , num2 , "is" ,prod)
    print("The quotient of" , num1 , "and" , num2 , "is",quo)
    print("The exponent of", num1, "and", num2, "is" ,expo)
    print("The reminder of" , num1 , "and" , num2 , "is" ,rem)
    print("The floor division of" , num1 , "and" , num2 , "is" ,floordiv)

def code5():
    pera = eval(input("Enter amount to deposit ---> "))
    name = input("Enter your name: ")

    libo = pera // 1000
    lsukli = pera % 1000
    fh = lsukli // 500
    fhsukli = lsukli % 500
    th = fhsukli//200
    thsukli = fhsukli % 200
    oh = thsukli//100
    ohsukli = thsukli % 100
    fif = ohsukli//50
    fifsukli = ohsukli % 50
    tw = fifsukli//20
    twsukli = fifsukli % 20
    t = twsukli//10
    tsukli = twsukli % 10
    f = tsukli//5
    fsukli = tsukli % 5
    o = fsukli//1
    osukli = fsukli % 1

    print(f"Hi {name} the breakdown of your deposit is")
    print(libo, " - 1000")
    print(fh, " - 500")
    print(th, " - 200")
    print(oh," - 100")
    print(fif," - 50")
    print(tw," - 20")
    print(t," - 10")
    print(f," - 5")
    print(o," - 1")

def code6():
    prelims = eval(input("Enter your Prelims score: "))
    midterm = eval(input("Enter your Midterm score: "))
    semi = eval(input("Enter your Semifinal score: "))
    final  = eval(input("Enter your Finals score: "))
    quiz = eval(input("Enter your Quiz scores: "))
    project = eval(input("Enter your Project scores: "))

    FG = (prelims * 0.15) + (midterm * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)
    print("Your Final Grades is", round(FG, 2))


    if 65 <= FG <= 100:
        print("You've passed")
        print("great job!")
    elif FG >= 64:
        print("Failed")
        print("Better luck next time")
    else:
        print("Invalid grades")

def code7():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gro = input("Do you want to buy? (yes or no): ")
    if gro.lower() == "yes":
        print("\nHERE IS THE LIST OF OUR PRODUCTS: \n\tEggs - ₱220 \n\tChicken Meat - ₱200 \n\tRice - ₱190 \n\tButter - ₱55 \n\tMilk - ₱165 \n\tBread - ₱90 \n\tCereal - ₱192")
        item = input("What item would you like to buy? ")
        price = input("Input the price of the item: ")
        amount = input("Enter the amount you'd like to pay: ")

        if age >= 60:
            taxed = price + (price * 0.123)
            total = taxed
            change = amount - total
            disc = taxed * 0.052
            total_disc = total - disc
            change = amount - total_disc 
            print("You can have senior discount of 5.2% from the total price." )

        elif age < 60:
            print

    else:
        print("Thanks for stopping buy!")

def code8():
    x = 0
    odd = 0
    even = 0
    for fm in range (1,11):
        num = eval(input(f"Input #{fm}: "))
        x += num
        if num % 2 == 0:
            even += num
        else:
            odd += num

    print(f"The summation of the numbers is: {x}")
    print(f"The summation of the even numbers is: {even}")
    print(f"The summation of the odd numbers is: {odd}")

def code9():
    for x in range(0,10):
        print(" ",end=" ")
        for y in range(0,x):
            print(" ",end=" ")
        for z in range(x,10):
            print("*",end=" ")
        print()

def code10():
    for x in range(1,6):
        for y in range(6, x, -1):
            print(" ", end = " ")
        for z in range(1, x +1):
            print("*", end=" ")
        for a in range(1, x +1):
            print("*", end =" ")
        print()

    for x in range(1,6):
        for y in range(1, x + 1):
            print(" ", end = " ")
        for z in range(6, x,-1):
            print("*", end=" ")
        for a in range(6, x, -1):
            print("*", end =" ")
        print()

def code11():
    #arrow up
    for x in range (1, 5):
        for y in range(5, x, -1):
            print(" ", end=" ")
        for z in range (1, x):
            print("*", end=" ")
        for a in range (0, x):
            print("*", end=" ")
        print()

    #arrow down
    for x in range (1, 6):
        for y in range (1, x):
            print(" ", end=" ")
        for z in range (6, x, -1):
            print("*", end=" ")
        for a in range (5, x, -1):
            print("*", end=" ")    
        print()

def code12():
    for x in range (1,6):
        for y in range(6, x, -1):
            print(" ", end=" ")
        for z in range (1, x):
            print("*", end=" ")
        for a in range (0, x):
            print("*", end=" ")
        print()

    for i in range(6,1-1):
        for j in range(1,i):
            print(" ",end=" ")
        for k in range(7,i -1):
            print("*",end=" ")
        for l in range(6,i -1):
            print("*",end=" ")
        print()

    for i in range(1,7):
        for j in range(1,5):
            print(" ",end=" ")
        for k in range(1,4):
            print("*",end=" ")
        print()
def code13():
    for i in range(1,6):
        for j in range(6,i,-1):
            print(" ",end= " " )

        for k in range(i,1,-1):
            print(k, end= " ")

        for l in range(1,i+1):
            print(l, end= " ")
        print()

    for i in range(4,0,-1):
        for j in range(6,i,-1):
            print(" ",end= " " )

        for k in range(i,1,-1):
            print(k, end= " ")

        for l in range(1,i +1):
            print(l, end= " ")
        print()

def code14():
    cycle = True
    sum = 0

    while cycle == True:
        num = eval(input("Enter a number:   "))

        if num == 0:
            print("Program has been terminated")
            print(f"The sum of all numbers is {sum}")
            break
            
        else:
            sum += num
            continue

def code15():
    import os
    isContinue = True 
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle? (yes/no)---> ")
        
        if ask.lower() == "no":
            os.system("cls")
            print("Program stopped")
            break
            iscontinue = False
        elif ask.lower() == "yes":
            os.system("cls")
            no += 1
            for x in range(1,6):
                for r in range(1,no +1):
                    for y in range(1, x + 1):
                        print("*", end = " ")
                    for z in range(5, x, -1):
                        print(" ", end=" ")
                print()
            continue

def code16():
    def denomination(amount):
        print("\nDenomination Breakdown:")
        A = amount // 1000
        AA = amount % 1000

        B = AA // 500
        BB = AA % 500

        C = BB // 200
        CC = BB % 200

        D = CC // 100
        DD = CC % 100

        E = DD // 50
        EE = DD % 50

        F = EE // 20
        FF = EE % 20

        G = FF // 10
        GG = FF % 10

        H = GG // 5
        HH = GG % 5

        I = HH // 1

        print("1000---", A)
        print("500----", B)
        print("200----", C)
        print("100----", D)
        print("50-----", E)
        print("20-----", F)
        print("10-----", G)
        print("5------", H)
        print("1------", I)


    accounts = {}

    def account():
        x = input("Enter an account name: ")
        if x in accounts:
            print("Account already exists!")
        else:
            accounts[x] = 0
            print(f"Account created successfully for {x}.")


    def deposit():
        x = input("Enter your account name: ")
        if x in accounts:
            try:
                amount = int(input("Enter amount to deposit : "))
                if amount > 0:
                    accounts[x] += amount
                    print(f"Deposited {amount} successfully. New balance: {accounts[x]}")
                    denomination(amount)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        x = input("Enter your account name: ")
        if x in accounts:
            try:
                amount = int(input("Enter amount to withdraw : "))
                if 0 < amount <= accounts[x]:
                    accounts[x] -= amount
                    print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[x]}")
                    denomination(amount)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        x = input("Enter your username: ")
        if x in accounts:
            print(f"Your balance: {accounts[x]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("\n+++++++++++++++++++++++++++++")
            print("Welcome to my Simulation Bank")
            print("+++++++++++++++++++++++++++++")
            print()
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            print()
            y = input("Choose an option: ")
            print()

            if y == '1':
                account()
            elif y == '2':
                deposit()
            elif y == '3':
                withdrawal()
            elif y == '4':
                check_balance()
            elif y == '5' or "Exit":
                print("Transaction ended ")
                break
            else:
                print("Invalid option. Please try again.")

    options()

def main():
    tuloy = True
    while tuloy == True:
        #This is a compilation of activities and code challenges
        print("\n\t+++++++++++++++++ WELCOME TO MY FINALS PROJECT +++++++++++++++++++++++")
        print("\n\t\t\t\tCODE CONTENT")
        print("\n\tAct - Activities\t\t\t\tCC - Code_Challenges")
        print("\n\t0 - Exit")
        print("\n\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        
        x = input("\n\tEnter what would you like to open: ")
        if x == "exit" or x == "0":
            break
            tuloy == False
        elif x != "exit" or x != "0":
            os.system("cls")
            if x.lower() == "act":
                while True:
                    print("\n\n\t\t\t+++++++++++++ ACTIVITY +++++++++++++++")
                    print("\n\t\t|a1 - Activity 1          |        a16 - Activity 16|")
                    print("\t\t|a2 - Activity 2          |        a17 - Activity 17|")
                    print("\t\t|a3 - Activity 3          |        a18 - Activity 18|")
                    print("\t\t|a4 - Activity 4          |        a19 - Activity 19|")
                    print("\t\t|a5 - Activity 5          |        a20 - Activity 20|")
                    print("\t\t|a6 - Activity 6          |        a21 - Activity 21|")
                    print("\t\t|a7 - Activity 7          |        a22 - Activity 22|")
                    print("\t\t|a8 - Activity 8          |        a23 - Activity 23|")
                    print("\t\t|a9 - Activity 9          |        a24 - Activity 24|")
                    print("\t\t|a10 - Activity 10        |        a25 - Activity 25|")
                    print("\t\t|a11 - Activity 11        |                         |")
                    print("\t\t|a12 - Activity 12        |                         |")
                    print("\t\t|a13 - Activity 13        |                         |")
                    print("\t\t|a14 - Activity 14        |                         |")
                    print("\t\t|a15 - Activity 15        |                         |")
                    print("\t\t|0   - BACK               |                         |")
            
                    com = input("\n\tWhich activity would you like to open: ")    
                    if com == "0" or com == "exit":
                        os.system("cls")
                        break
                        
                    elif com != "0" or com != "exit":
                        if com.lower() == "a1":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 1\n")
                            act1()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a2":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 2\n")
                            act2()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a3":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 3\n")
                            act3()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a4":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 4\n")
                            act4()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a5":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 5\n")
                            act5()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a6":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 6\n")
                            act6()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a7":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 7\n")
                            act7()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a8":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 8\n")
                            act8()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a9":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 9\n")
                            act9()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a10":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 10\n")
                            act10()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a11":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 11\n")
                            act11()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a12":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 12\n")
                            act12()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a13":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 13\n")
                            act13()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a14":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 14\n")
                            act14()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a15":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 15\n")
                            act15()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a16":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 16\n")
                            act16()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a17":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 17\n")
                            act17()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a18":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 18\n")
                            act18()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a19":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 19\n")
                            act19()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a20":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 20\n")
                            act20()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a21":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 21\n")
                            act21()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a22":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 22\n")
                            act22()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a23":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 23\n")
                            act23()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a24":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 24\n")
                            act24()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif com.lower() == "a25":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("ACTIVITY 25\n")
                            act25()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                            continue       

                        else:
                            print("INVALID COMMAND")    
                            
            elif x.lower() == "cc":
                while True:
                    print("\n\n\t\t+++++++++++++ CODE CHALLENGE +++++++++++++++")
                    print("\n\t\t|cc1 - Code Challenge 1      |")
                    print("\t\t|cc2 - Code Challenge 2      |")
                    print("\t\t|cc3 - Code Challenge 3      |")
                    print("\t\t|cc4 - Code Challenge 4      |")
                    print("\t\t|cc5 - Code Challenge 5      |")
                    print("\t\t|cc6 - Code Challenge 6      |")
                    print("\t\t|cc7 - Code Challenge 7      |")
                    print("\t\t|cc8 - Code Challenge 8      |")
                    print("\t\t|cc9 - Code Challenge 9      |")
                    print("\t\t|cc10 - Code Challenge 10    |")
                    print("\t\t|cc11 - Code Challenge 11    |")
                    print("\t\t|cc12 - Code Challenge 12    |")
                    print("\t\t|cc13 - Code Challenge 13    |")
                    print("\t\t|cc14 - Code Challenge 14    |")
                    print("\t\t|cc15 - Code Challenge 15    |")
                    print("\t\t|cc16 - Code Challenge 16    |")
                    print("\t\t|0    - BACK                 |")

                    mand = input("Which Code Challenge would you like to open: ")
                    if mand == "0" or mand == "exit":
                        os.system("cls")
                        break

                    elif mand != "0" or mand != "exit":
                        if mand.lower() == "cc1":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 1")
                            code1()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc2":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 2\n")
                            code2()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc3":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 3\n")
                            code3()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc4":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 4\n")
                            code4()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc5":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 5\n")
                            code5()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc6":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 6\n")
                            code6()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc7":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 7\n")
                            code7()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc8":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 8\n")
                            code8()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc9":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 9\n")
                            code9()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc10":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 10\n")
                            code10()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc11":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 11\n")
                            code11()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc12":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 12\n")
                            code12()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc13":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 13\n")
                            code13()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc14":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 14\n")
                            code14()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc15":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 15\n")
                            code15()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue
                        elif mand.lower() == "cc16":
                            os.system("cls")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("CODE CHALLENGE 16\n")
                            code16()
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
                            continue

                        else:
                            print("INVALID COMMAND")  

main()