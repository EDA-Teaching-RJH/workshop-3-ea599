def main():
    day = input("What day of the week is it: ")
    print(check(day))

def check(x):
    match x:
        case "Saturday" | "Sunday":
            return "It is the weekend"
        case _:
            return "It is the weekday"

main()