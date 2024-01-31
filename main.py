from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and int(value):
            self.value = value
        else:
            raise ValueError('Number must hace 10 symbols')
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value   


        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                self.phones.remove(ph)


    def edit_phone(self, old_phone, new_phone):
        check = False
        for ph in self.phones:
            if ph.value == old_phone:
                check = True
                try:
                    ph.value = new_phone
                except ValueError as e:
                    return e  
        if not check:
            raise ValueError('Number is not ixisting') 


    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: Record):
        if name in self.data:
            return self.data[name]

    def delete(self, name: Record):
        if name in self.data:
            del self.data[name]
    
    
    