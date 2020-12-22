print("       WELCOME TO TABLE MAKER")
print("------------------------------------")

while (True):
    inp1 = int(input("Enter the number that you want table: "))
    cal = (inp1 * 10 + 1)
    list1 = []

    for i in range(1, cal):
        if i%inp1==0:
            list1.append(i)
    print(list1, "\n")

    inp2 = input("Enter r for reuse & e for exit: ")
    if inp2 == "e":
        print("\n      Thankyou!\nfor using Table Maker")
        break
