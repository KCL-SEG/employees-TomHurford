"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

# create a subclass of Employee called HourlyEmployee that overrides the get_pay method to calculate pay based on hours worked and hourly rate plus commission

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate, commission):
        super().__init__(name)
        self.hours = hours
        self.rate = rate
        self.commission = commission

    def get_pay(self):
        return self.hours * self.rate + self.commission

# create a subclass of Employee called SalariedEmployee that overrides the get_pay method to calculate pay based on salary plus commission

class SalariedEmployee(Employee):
    def __init__(self, name, commission_rate, commission_sales, salary):
        super().__init__(name)
        self.salary = salary
        self.commission_rate = commission_rate
        self.commission_sales = commission_sales

    def get_pay(self):
        return self.salary + self.commission_rate * self.commission_sales

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalariedEmployee('Billie',0,0,4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie',0,0,25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalariedEmployee('Renee',200,4,3000)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee('Jan',220,3,25,150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalariedEmployee('Robbie',1500,1,2000)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee('Ariel',600,1,30,120)
