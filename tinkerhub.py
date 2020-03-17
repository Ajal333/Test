from datetime import datetime

class tech :

    def __init__(self,name) :
        self.name = name
    
    def addStacks(self,inter) :
        self.interest = inter
    
    def setMentorOrLearner(self,designation) :
        if designation == 'mentor' or designation == 'learner':
            self.desig = designation
        else :
            self.desig = None
    
    def setAvailableTime(self) :
        if self.desig == 'mentor' :
            self.time = str(datetime.now()) #in days
            self.timeStamp =   datetime.strptime(self.time[:-7],'%Y-%m-%d %H:%M:%S')
    
    def getMentor(self) :
            if self.desig == 'mentor':
                print("Name: {0},   Designation: {1},   Interest: {2}.".format(self.name,self.desig,self.interest))

emp1 = tech('test1')
emp2 = tech('test2')
emp3 = tech('test3')
emp = [emp1,emp2,emp3]

emp1.addStacks('Python')
emp2.addStacks('Web')
emp3.addStacks('Data Science')

emp1.setMentorOrLearner('learner')
emp2.setMentorOrLearner('mentor')
emp3.setMentorOrLearner('mentor')

emp2.setAvailableTime()

print('Enter 1 to see the list of available mentors: ')
choice = input()

if choice == '1' : 
    for i in range (0,3) :
        emp[i].getMentor()
else :
    print('Wrong Input')






        

