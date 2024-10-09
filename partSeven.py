def main():
    loop = True
    while loop == True:
        n1 = int(input("What is the first number: "))
        n2 = int(input("What is the second number: "))
        sy = input("What is the operation: ")
        print(str(n1) + str(sy) + str(n2) + "=" + str(answer(n1, n2, sy)))
        loop = check()

def check():
    ans = input("Do you want to do maths: ")
    if ans == "yes":
        return True
    else:
        return False
        
    
def answer(x, y, z):
    match z:
        case "+":
            return x+y
        case "-":
            return x-y
        case "*":
            return x*y
        case "/":
            return x/y
        case "^":
            return pow(x, y)
        case "%":
            return x%y
        case _:
            return "ERROR"
        
main()