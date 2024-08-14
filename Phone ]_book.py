import re
class Phone_book:
    def __init__(self):
        pass

    def add_contact(self,name,email,phone):
        file = open('contacts.txt','a')
        if len(phone) != 11 :
            raise ValueError('There is a problem with the phone number')
        if not (re.match(r'^[A-Za-z0-9_]+@[a-zA-Z]+\.com',email)) :
            raise ValueError('There is a problem with the email address')
        file.write(f"""{
                    'name' : {name},
                    'email' : {email},
                    'phone' : {phone},
                     }
                    """)
        file.close()

    def update_contact(self,*args):
        pass

    def delete_contact(self,*args):
        pass

    def show_contacts(self):
        pass

    def sort_contacts(self):
        pass

    def save_contact(self):
        pass


