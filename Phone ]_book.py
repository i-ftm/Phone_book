import re
import os

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
                     }\n
                    """)
        file.close()

    def update_contact(self,name,email,phone):
        my_file =open('contacts.txt','r')
        file = list(my_file)
        my_file.close()
        contact = {
            'name':name,
            'email':email,
            'phone':phone,
        }

        if contact in file :
            file.remove(contact)
            update_item=input("Which item do you want to edit? for name write 'n' , for email address write 'e' , for phonenumber write 'p'")
            for i in range(len(update_item)):
                if update_item[i] == 'n':
                    contact['name']=input("Enter the name")
                elif update_item[i] == 'e':
                    email = input("Enter the email address")
                    if not (re.match(r'^[A-Za-z0-9_]+@[a-zA-Z]+\.com', )):
                        raise ValueError('There is a problem with the email address')
                    contact['email'] = email
                elif update_item[i] == 'p':
                    phone = input("Enter the phone number")
                    if len(phone) != 11:
                        raise ValueError('There is a problem with the phone number')
                    contact['phone'] = phone
                else:
                    raise ValueError('does not exist')
                file.append(contact)

                save_item = input("Would you like to save it? if yes write 'y' and if no write 'n' ")
                if save_item == 'n':
                    pass
                elif save_item == 'y':
                    os.remove('contacts.txt')
                    new_file=open('contacts.txt','a')  #This file has been updated
                    for i in range(len(file)):
                        new_file.write(f'{file[i]}\n')
                    new_file.close()

                else:
                    raise ValueError('There is a problem with the email address')


    def delete_contact(self,name,email,phone):
        my_file = open('contacts.txt', 'r')
        file = list(my_file)
        my_file.close()
        contact = {
            'name': name,
            'email': email,
            'phone': phone,
        }

        if contact in file:
            file.remove(contact)

        save_item = input("Would you like to save it? if yes write 'y' and if no write 'n' ")
        if save_item == 'n':
            pass
        elif save_item == 'y':
            os.remove('contacts.txt')
            new_file = open('contacts.txt', 'a')  # This file has been updated
            for i in range(len(file)):
                new_file.write(f'{file[i]}\n')
            new_file.close()

        else:
            raise ValueError('There is a problem with the email address')

    def show_contacts(self):
        file = open('contacts.txt', 'r')
        print(file.read())

    def sort_contacts(self):
        pass



