class Workers:
    all = []
    #  class attribute
    salary = 0

    def __init__(self, name: str, sex: str, age: int, role: str):
        # instance attributes
        self.name = name
        self.sex = sex
        self.age = age
        self.role = role
        # self.salary = salary

    # method

    def information(self):
        print(f'Name:  {self.name}')
        print(f'Sex:  {self.sex}')
        print(f'Age:  {self.age}')
        print(f'Role: {self.role}')
        self.payments()
        print(f'Salary:  {self.salary}')

    def payments(self):
        if self.role == 'teacher':
            self.salary = 1000000
        elif self.role == 'cleaner':
            self.salary = 2000
        elif self.role == 'director':
            self.salary = 2000000
        else:
            self.salary = 40000


name1 = input('Enter your name: ')
sex1 = input('Enter your sex: ')
age1 = int(input('Enter your age: '))
role1 = input('Enter your role: ')

# Instances
worker1 = Workers(name1, sex1, age1, role1)
# worker2 = Workers('NABASA APOPHIA', 'M', 23, '1000')
# worker3 = Workers('AMOIT RONALD', 'M', 15, 10000)
# worker4 = Workers('ARTHUR LYN JOY', 'F', 20, 9000)


worker1.information()
# worker2.information()
# worker3.information()
# worker4.information()

# for

