def main():
    age = int(input("What is your age: "))
    stu = input("Are you a student: ")
    print("£" + str(price(age,stu)))

def price(x,y):
    if x < 12 or x >= 65:
        return 5
    elif y == "yes":
        return 8
    else:
        10

main()
