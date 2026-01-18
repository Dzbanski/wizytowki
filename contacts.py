class BaseContact():
    def __init__(self, first_name, last_name, private_phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email = email

class BussinessContact(BaseContact):
    def __init__(self, first_name, last_name, private_phone, email, job, company, work_phone):
        super().__init__(first_name, last_name, private_phone, email)
        self.job = job
        self.company = company
        self.work_phone = work_phone