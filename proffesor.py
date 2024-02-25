class LectureError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
class Proffesor(Person):
    def __init__(self, firstname, lastname, lecture):
        self.firstname = firstname
        self.lastname = lastname
        self.lecture = lecture

    def limit(self):
        #print(self.grade)
        if len(self.lecture) > 3:
            return False
        return True

lecture = {1: 'math', 2: 'physic', 3: 'oloom'}
professor = Proffesor('ali', 'alavi', lecture)

try:
    if professor.limit() == True:
        print("He/She can choose lectures")
    else:
        raise LectureError("He/She can't choose more than 3 lectures")

except LectureError as LE:
    print(LE)