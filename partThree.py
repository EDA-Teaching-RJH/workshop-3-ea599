def main():
    grade = int(input("What was your score? "))
    print("Your grade is: " + calc(grade))

def calc(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    elif x >= 60:
        return "D"
    else:
        return "F"

main()