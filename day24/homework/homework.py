saidumlo_ricxvi= 7
cdebi = 3

while cdebi > 0:
    num = int(input("გამოიცანი რიცხვი (1-10): "))
    if num == saidumlo_ricxvi :
        print("გილოცავ მოიგე")
    else:
        cdebi -= 1
        if cdebi > 0:
            print("შეგეშალა. დაგრჩა ცდები:", )
        else:
            print("You lose")
                  
