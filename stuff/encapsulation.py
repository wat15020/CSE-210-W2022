class Student:
    def __init__(self, fName, lName):
        self._fName = fName
        self._lName = lName

    def display_name(self):
        return f'{self._fName} {self._lName}'

david = Student('David', 'Watkins')
print(david.display_name())

@property
def firstname(self):
    return self._fName

@property
def lastname(self):
    return self._lName

@firstname.setter
def firstname(self, fName):
    self._firstname = fName

@lastname.setter
def lastname(self, lName):
    self._lastname = lName