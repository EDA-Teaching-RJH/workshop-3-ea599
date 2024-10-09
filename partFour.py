def main():
    un = input("What is your username: ")
    pw = input("What is your password: ")
    print(userCheck(un, pw))

def userCheck(u, p):
    if u == "admin" and p == "password123":
        return "Username and password correct"
    else:
        return "Username or password incorrect"

main()