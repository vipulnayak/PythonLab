class Student:
    def __init__(self):
        self.name=" "
        self.usn=" "
        self.sem=0
        self.br=" "
    def read(self,name,usn,sem,br):
        self.name=name
        self.usn=usn
        self.sem=sem
        self.br=br
    def display(self):
        print("student name: ",self.name)
        print("usn: ",self.usn)
        print("semester: ",self.sem)
        print("branch: ",self.br)
class Faculty(Student):
    def __init__(self):
        self.name=" "
        self.idd=" "
        self.email=" "
        self.br=" "
    def read1(self,name,idd,email,br):
        self.name=name
        self.idd=idd
        self.email=email
        self.br=br
    def display1(self):
        print("student name: ",self.name)
        print("usn: ",self.idd)
        print("email: ",self.email)
        print("branch: ",self.br)
class Subject(Faculty):
    def __init__(self):
        self.sub1=" "
        self.sub2=" "
        self.sub3=" "
        self.sub4=" "
    def read2(self,sub1,sub2,sub3,sub4):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
    def display2(self):
        print("Subject 1: ",self.sub1)
        print("Subject 2: ",self.sub2)
        print("Subject 3: ",self.sub3)
        print("Subject 4: ",self.sub4)
s1=Subject()
s1.read1("crazy","cs321","crazy@gmail.com","cs")
s1.display1()
