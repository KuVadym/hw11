from collections import UserDict
from datetime import datetime, timedelta
import re

class Field():
    pass

class AddressBook(UserDict):

    def add_record (self,k, v):
        super().__setitem__(k, v)
    
    def iterator (self):
        pass

class Name(Field):
    def __init__(self, n, s=None):
        self.name = n
        self.surname = s

    def __repr__(self):
        return f"{self.name}"

class Phone():

    def __init__(self, phone = None):
        self.__phone = phone

    @property
    def phone (self):
        return self.__phone

    @phone.setter
    def phone(self, p):
        if p != None:
            regex_phone = re.compile(r"(\(\d{3}\))-(\d{3}-\d{4})")
            
            if bool(regex_phone.search(p)) == True:
                self.__phone = p
            else:
                print('Only numbers phones like (415)-555-4242 is appropriate')


    def __repr__(self):
        return f"{self.phone}"
        
class Record():
    
    def __init__ (self, name, phone = None, birthday = None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)

    def add_phone (self, phone):
        self.phones.append(phone)
        print (f"for {self.name} add new phone {phone}." )
        
    def del_phone (self, phone):
        for p in self.phones:
            if p == phone:
                self.phones.remove(p)
                print (f"Phone {p} successfully deleted")

    def change_phone (self, phone_one, phone_two):
        i = 0                                                          # Лічильник для проходження і заміни елемента в списку
        for p in self.phones:
            
            if p == phone_one:
                self.phones[i] = phone_two
                print ("Phone successfully updated")
            i += 1
        else:
            print (f"Phone {phone_one} is not found!")

    def print_all_phones(self):
        for p in self.phones:
            print (f"{p}")

    def days_to_birthday (self, bd):
        if self.birthday != None:
            if bd != None:
                current_datetime = datetime.now()             # Знаходимо нинішню дату
                bd = bd.birthday                                       # Задаємо дату народження
                if current_datetime > bd:               
                    difference = (current_datetime  - bd).days
                    i= 0
                    old = ((current_datetime  - bd).days)//365
                    years = []
                    z = bd.year
                    for el in range (old):
                        years.append(z)
                        z +=1
                    for y in years:
                        if (y % 4) == 0:
                            i+=1
                    day_to_bd = timedelta(days = 365).days - difference % 365 + i
                    print (f"Days to the next birthday: {day_to_bd}")
        else:
            print("Haven't information")
            

            



class Birthday ():
    def __init__ (self, birthday = None):
        self.birthday = birthday


user = Phone ("06655")
user_name = Name ("Vadym")
vadym_r = Record (user_name, user)
phone = Phone ("063-710-61-94")
vadym_r.add_phone (phone)
actual_phone = Phone ("050-352-352-3")
vadym_r.change_phone (user, actual_phone)
new_phone = Phone ("0-800-000-0000")
vadym_r.change_phone (new_phone, actual_phone)
vadym_r.print_all_phones()
vadym_r.add_phone (user)
vadym_r.print_all_phones()
vadym_r.del_phone (user)
vadym_r.print_all_phones()
vadym_page = AddressBook ()
vadym_page.add_record (vadym_r.name, vadym_r.phones)
print (vadym_page)
v = Birthday ()
vadym_r.days_to_birthday (v)