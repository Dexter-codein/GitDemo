class emp:
    def __init__(self, name, company):
        self.name1 = name
        self.comp1 = company

    def display(self):
        print('My name is '  + str(self.name1))
        print('My company is '  + str(self.comp1))

obj = emp('ken', 'Nokia')
obj.display()


