import re
class A ():
    def pr(self):
        pass

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

user = Phone ("06655")
phone = Phone ()
phone.phone = "06655"
c = Phone ()
c.phone = "(063)-710-6194"
#print (phone.phone)
print (c.phone)