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

@firstname.setter
def firstname(self, fName):
    self._firstname = fName