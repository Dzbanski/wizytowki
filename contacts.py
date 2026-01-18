from faker import Faker

fake = Faker('pl_PL')

class BaseContact():
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email

    def contact(self):
        print(f'Wybieram numer {self.private_phone} i dzwonię do {self.first_name} {self.last_name}')

    def __str__(self):
         return f'{self.first_name} {self.last_name} | {self.email}'
    

class BussinessContact(BaseContact):
    def __init__(self, first_name, last_name, private_phone, email, job, company, work_phone):
        super().__init__(first_name, last_name, private_phone, email)
        self.job = job
        self.company = company
        self.work_phone = work_phone

    def __str__(self):
        return f'{self.first_name} {self.last_name} \n{self.company} \n{self.job} \n{self.email}'

    def contact(self):
        print(f'Wybieram numer {self.work_phone} i dzwonię do {self.first_name} {self.last_name}')