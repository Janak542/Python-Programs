# ATM Process 
class atm():
    def balance(self):
        b = int(input("Enter Your Balance : "))
        self.b = b
        return self.b


    def withdraw(self):
        w = int(input("Enter Withdraw Amount : "))
        self.w = w
        if self.b >= self.w:
            self.b -= self.w
        else:
            print("Insufficient Balance!")
            exit()
        return self.b


    def deposit(self):
        d = int(input("Enter Deposite Amount : "))
        self.d = d
        self.b += d
        return self.b 


    def choice(self):
        while True:
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Exit")
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                print(o.withdraw())
            elif ch == 2:
                print(o.deposit())
            elif ch == 3:
                print(self.b)
            elif ch == 4:
                exit()
                
            
            
def main():
    o.balance()
    o.choice()

# Password Function or PIN Authentication
def password():
    a = 1234
    i = 1
    attempt = 3
    id = int(input("Enter pin : "))
    if id == a:
        main()
    else:
        while i<=attempt:
            sid = int(input("Invalid.. Re-enter : "))
            i = i + 1
            if sid == a:
                main()
                exit()
            elif i == attempt+1:
                print("Sorry Your Card is Blocked.. Please contact branch manager")
            else:
                continue

o = atm()
password()