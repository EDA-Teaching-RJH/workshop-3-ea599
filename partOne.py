def main():
    age = int(input("What is your age? "))
    print("You are an " + adultCheck(age))

def adultCheck(age):
    if age >= 18:
        return "adult"
    else:
        return "child"
    
main()
