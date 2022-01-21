class Account:

    def __init__(self, filepath):
        # path of file goes to the filepath parameter, then you create an instance variable with the self.filepath which is equal to the path 
        # by doing this though, we are able to use the file path variable wherever
        self.filepath = filepath
        with open(filepath, 'r') as file:
            # self is the object, balance is the instance variable
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    # this function lets us to commit to our txt file
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
# the initiation takes in one param, the file path, so we pass balance to it
account = Account("/balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()