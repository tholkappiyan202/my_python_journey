
## using the updates version with the option to view balance
class BANK:
    def __init__(self, balance):
        self.__balance =balance #double __ makes it unaccessable outside the class , i.e encapsultion
    def __check(self,amount):
        if amount<0 :
            raise ValueError("money must be positive number")
    def deposit(self,amount):
        self.__check(amount)  # using self to call a method inside another method , both of the same class
        self.__balance += amount
    def withdraw(self,amount):
        self.__check(amount)
        if amount > self.__balance:
            raise ValueError("INSUFFICIENT BALANCE !")
        self.__balance -= amount
    def view_balance(self):
        return self.__balance
user2 = BANK(500)
user2.deposit(200)
print(user2.view_balance())
user2.withdraw(300)
print(user2.view_balance())
user2.deposit(-10) # RAISES VALUE ERROR



class BANK:
    def __init__(self, balance):
        self.__balance =balance #double __ makes it unaccessable outside the class , i.e encapsultion
    def deposit(self,amount):
        self.amount =amount
        if amount>0:
            self.__balance += amount
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance -= amount
            
user1 = BANK(500)    
user1.deposit(200)
print(user1.__balance) # it gives attribute error becasue __balance is not supposed to be used outside the class
