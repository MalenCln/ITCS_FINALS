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
    pass

def act24():
    pass

def act25():
    pass