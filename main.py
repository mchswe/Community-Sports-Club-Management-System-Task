class Person:
    def __init__(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def set_details(self, name, age, contact_number):
        self.name = name
        self.age = age
        self.contact_number = contact_number

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Contact Number: {self.contact_number}")

class Member(Person):
    def __init__(self, name, age, contact_number, membership_id, sport):
        super().__init__(name, age, contact_number)
        self.membership_id = membership_id
        self.sport = sport
        self.performance_scores = []

    def set_member_details(self, membership_id, sport):
        self.membership_id = membership_id
        self.sport = sport

    def add_performance_score(self, score):
        self.performance_scores.append(score)

    def calculate_average_score(self):
        print(sum(self.performance_scores) / len(self.performance_scores))

    def get_member_summary(self):
        avg_score = self.calculate_average_score()
        print(f"{self.get_details()}, Membership ID: {self.membership_id}, Sport: {self.sport}, Average Score: {avg_score}.")

class Coach(Person):
    def __init__(self, name, age, contact_number, coach_id, specialisation, salary):
        super().__init__(name, age, contact_number)
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary
        self.mentees = []

    def set_coach_details(self, coach_id, specialisation, salary):
        self.coach_id = coach_id
        self.specialisation = specialisation
        self.salary = salary

    def assign_mentee(self, member):
        self.mentees.append(member)
        print(f"Coach {self.name} is now mentoring {member.name} in {member.sport}.")

    def get_mentees(self):
        print([(mentee.name, mentee.sport) for mentee in self.mentees])

    def increase_salary(self, percentage):
        self.salary = self.salary * (percentage / 100)

    def get_details(self):
        print(f"{super().get_details()}, Coach ID: {self.coach_id}, Specialisation: {self.specialisation}, Salary: {self.salary}.")


# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, contact_number, staff_id, position, years_of_service):
        super().__init__(name, age, contact_number)
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service

    def set_staff_details(self, staff_id, position, years_of_service):
        self.staff_id = staff_id
        self.position = position
        self.years_of_service = years_of_service

    def increment_years_of_service(self):
        self.years_of_service += 1

    def assist_member(self, member):
        print(f"Staff {self.name} assisted {member.name} in resolving an issue.")

    def get_staff_summary(self):
        print(f"{self.get_details()}, Staff ID: {self.staff_id}, Position: {self.position}, Years of Service: {self.years_of_service}")


member1 = Member("Jacob", 25, "133-556-7320", "M1234", "Football")
member2 = Member("Bob", 22, "987-654-3210", "M5678", "Basketball")
coach1 = Coach("Charlie", 40, "555-666-7777", "C101", "Football", 50000)
coach2 = Coach("Diana", 35, "444-333-2222", "C202", "Basketball", 55000)
staff1 = Staff("Eve", 30, "101-434-3123", "S303", "Club Secretary", 5)

coach1.assign_mentee(member1)

member1.add_performance_score(85)
member1.add_performance_score(90)

staff1.assist_member(member2)

