class Student:
    def __init__(self, name, admission_number, subjects, grade):
        self.name = name
        self.admission_number=admission_number
        self.subjects=subjects
        self.grade = grade

    def print_details(self):
        print(f"Name: {self.name}\nAdm. No: {self.admission_number}\nSubjects: {self.subjects}\nGrade: {self.grade}")


student_1 =Student("Andrew Omwenga", "9973","Maths\nEnglish\nKiswahili", "A \nA-\nC+")
student_2 =Student("Kevin Ongwani", "8976","\nMaths\nEnglish\nKiswahili", "A, B, C")

student_1.print_details()
student_2.print_details()