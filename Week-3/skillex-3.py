
#program 1:
class MyClass:
    def __init__(self,value):
        self.value=value
    def method1(self):
        print("This is method 1 from MyClass")
print("Class namespace:")
print(MyClass.__dict__)

#program 2:
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        print("Attributes and Values before removing student_name:")
        print(f"student_id: {self.student_id}")
        print(f"student_name: {self.student_name}")
        print(f"student_class: {self.student_class}")

        del self.student_name

        print("\nAll Attributes and Values after removing student_name:")
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")

student_id = input("Enter student ID: ")
student_name = input("Enter student name: ")
student_class = input("Enter student class: ")

student = Student(student_id, student_name, student_class)


#program  3
class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposit of Rs.{amount} successful.")
        else:
            print("Invalid deposit amount")

    def withdrawal(self,amount):
        if 0<amount<=self.balance:
            self.balance -= amount
            print(f"Withdrawal of Rs.{amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def bank_fees(self):
        fees=0.05*self.balance
        self.balance -= fees
        print(f"Bank fees of Rs.{fees} applied.")

    def display(self):
        print(f"Account Number:{self.accountNumber}")
        print(f"Account Holder:{self.name}")
        print(f"Balance: Rs.{self.balance}")

account1 = BankAccount(accountNumber=123456,name="John Doe",balance=1000)
account1.display()

account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()

account1.display()

