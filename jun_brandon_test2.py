
# Brandon Jun // COMSC 078 // Test #2 - Program

from datetime import datetime, date

class Person(object):

    def __init__(self, firstName, lastName):

        self.firstName = firstName
        self.lastName = lastName
        self.birthdate = None

    def getFirstName(self):

        return self.firstName

    def getLastName(self):

        return self.lastName

    def setBirthday(self, birthdate):

        self.birthdate = birthdate

    def getAge(self):

        today = date.today()
        age = today.year - self.birthdate.year

        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def __str__(self):
        return f"{self.fullName()} is {self.getAge()} years old."

    def fullName(self):

        return f"{self.firstName} {self.lastName}".strip()


class Student(Person):
    nextId = 1

    def __init__(self, firstName, lastName, gender):
        super().__init__(firstName, lastName)
        self.gender = gender
        self.idNumber = Student.nextId
        Student.nextId += 1

    def getidNumber(self):
        return self.idNumber

    def __str__(self):
        pronoun = "his" if self.gender.lower() in ("m", "male") else "her"
        return (f"{self.fullName()} is {self.getAge()} years old, "
                f"and {pronoun} student ID is {self.idNumber}.")


def main():
    obama = Person("Barack", "Obama")
    obama.setBirthday(datetime(1961, 8, 4))

    madonna = Person("Madonna", "")
    madonna.setBirthday(datetime(1958, 8, 16))

    abel = Student("Abel", "Baker", "male")
    abel.setBirthday(datetime(2005, 2, 1))

    claudette = Student("Claudette", "Davis", "female")
    claudette.setBirthday(datetime(2006, 5, 27))

    for person in (obama, madonna, abel, claudette):
        print(person)


main()