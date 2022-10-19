class Person:
    def _init_(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print("Full Name: " + self.first_name, self.last_name)


class Student(Person):
    def _init_(self, first_name, last_name, age):
        Person._init_(self, first_name, last_name, age)
        self.lectures = []

    def listing_of_lectures(self):
        print("Listing all the lectures :")
        for lect in self.lectures:
            print(lect)

    def adding_lectures(self, lect):
        print("Adding new lecture:" + lect)
        self.lectures.append(lect)

    def removing_lectures(self, lect):
        print("Removing lecture:" + lect)
        self.lectures.remove(lect)


class Professor(Person):
    def _init_(self, first_name, last_name, age):
        Person._init_(self, first_name, last_name, age)
        self.subjects = []

    def listing_of_subjects(self):
        print("Listing all the subjects:")
        for sub in self.subjects:
            print(sub)

    def adding_subjects(self, sub):
        print("Adding new subjects:" + sub)
        self.subjects.append(sub)

    def removing_subjects(self, sub):
        print("Removing subjects:" + sub)
        self.subjects.remove(sub)


class Lectures:
    def _init_(self, name, max_students, duration):
        self.name = name
        self.max_students = max_students
        self.duration = duration
        self.professor = []

    def listing_of_professors(self):
        print("Listing all the professors:")
        for p in self.professor:
            print(p)

    def lect_info(self):
        print("Name of the lecture:" + self.name)
        print("During of the lecture:" + str(self.duration))

    def adding_professors(self, p):
        print("Adding professor to the list of professsors:" + p)
        self.professor.append(p)


