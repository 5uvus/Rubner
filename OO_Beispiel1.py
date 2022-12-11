from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2


class Role(Enum):
    EMPLOYEE = 1
    GROUPLEADER = 2


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.persons = []

    def addGroupleader(self, leader):
        self.persons.remove(leader)
        leader.role = Role.GROUPLEADER
        self.persons.append(leader)

    def addEmployee(self, employee):
        self.persons.append(employee)

    def __str__(self):
        return_str = ""
        for p in self.persons:
            return_str += p.firstName + "-" + p.lastName + "-" + "Role: " + str(p.role) + ", "
        return self.department_name + "\tPeople in Department: " + return_str


class Person:
    def __init__(self, firstName, lastName, age, gender: Gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gender = gender

    def __str__(self):
        return "Firstname: " + self.firstName + " Lastname: " + self.lastName + " Age: " + str(self.age) + "Gender: " + \
               str(self.gender)


class Employee(Person):
    def __init__(self, person, persNr, department):
        super().__init__(person.firstName, person.lastName, person.age, person.gender)
        self.role = Role.EMPLOYEE
        self.persNr = persNr
        self.department = department
        self.person = person

    def __str__(self):
        return super().__str__() + " PersNr: " + str(self.persNr) + " Dept: " + self.department + "Role: " + str(self.role)


class Groupleader(Employee):
    def __init__(self, employee, group):
        super().__init__(employee.person, employee.persNr, employee.department)
        self.group = group
        self.role = Role.GROUPLEADER
        self.employee = employee

    def __str__(self):
        return super().__str__() + " Group: " + self.group + "Role: " + str(self.role)


class Company:
    def __init__(self, departments):
        self.departments = departments

    def countEmployees(self):
        sum = 0
        for d in self.departments:
            for e in d.persons:
                if e.role == Role.EMPLOYEE:
                    sum += 1
        return sum

    def countGroupleaders(self):
        sum = 0
        for d in self.departments:
            for e in d.persons:
                if e.role == Role.GROUPLEADER:
                    sum += 1
        return sum

    def countDepartments(self):
        return len(self.departments)

    def biggestDepartment(self):
        sums_employees = []
        for d in self.departments:
            sums_employees.append(len(self.departments.persons))

        sums_employees.sort()
        return sums_employees[len(sums_employees) - 1]

    def MaleFemaleStats(self):
        males = 0
        females = 0
        for d in self.departments:
            for e in d.persons:
                if e.gender == Gender.MALE:
                    males += 1
                else:
                    females += 1

        return "Males: " + str(round(males / self.countEmployees() * 100, 2)) + "% Females: " + str(round(
            females / self.countEmployees() * 100, 2)) + "% "


if __name__ == '__main__':
    p1 = Person("Personi", "Kroni", 25, Gender.MALE)
    p2 = Person("Persi", "Chersi", 30, Gender.FEMALE)
    p3 = Person("Perso", "Kerso", 45, Gender.MALE)

    e1 = Employee(p1, 1, "IT")
    e2 = Employee(p2, 2, "HR")
    e3 = Employee(p3, 3, "FI")

    g1 = Groupleader(e1, "Planning Group")
    print(g1.role)

    d1 = Department("Sector A")
    d2 = Department("Sector B")

    d1.addEmployee(e1)
    d1.addEmployee(e2)
    d1.addGroupleader(e1)
    d2.addEmployee(e3)

    deps = [d1, d2]

    c = Company(deps)

    print("Number of employees: ", c.countEmployees())
    print("Number of groupleaders: ", c.countGroupleaders())
    print("Number of departments: ", c.countDepartments())
    print("Biggest Department:  ")
    print("Statistics: ")
    print(c.MaleFemaleStats())

    print(d1)