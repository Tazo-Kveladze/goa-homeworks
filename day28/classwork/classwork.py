asaki = int(input("ჩაწერე ასაკი: "))

if asaki < 18:
    if asaki < 14:
        print("Discount 20%")
    else:
        print("Discount 10%")
else:
    print("No discount")
    