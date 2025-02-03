from datetime import datetime, date


class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.gender = gender

        # Convert dob to a full date if it's provided as an integer (e.g., 1999 becomes "1999-01-01")
        if isinstance(dob, int):
            dob = f"{dob}-01-01"

        # Parse date and handle potential errors
        try:
            date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
            self.dob = dob
            self.age = date.today().year - date_of_birth.year
        except ValueError:
            print(f"Error: Date of birth '{dob}' is not in the correct format 'YYYY-MM-DD'")
            self.dob = None
            self.age = None

    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}\nAge: {self.age}")


class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender)
        self.salary = salary

    # Override to include salary
    def print_salary(self):
        super().print_details()
        print(f"Salary: {self.salary}")


class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay

        # Parse end_date and handle potential errors
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
            self.end_date = end_date
        except ValueError:
            print(f"Error: End date '{end_date}' is not in the correct format 'YYYY-MM-DD'")
            self.end_date = None

    def print_hourly_pay(self):
        print(f"Hourly payment: {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date: {self.end_date}")


# Testing the classes
p1 = PermanentEmployee("Jane Smith", 24455645, 1999, "F", 10000)
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee("Jin", "22165734", "1995-03-05", "M", 1000, "2024-12-24")
t1.print_details()
t1.print_hourly_pay()
t1.print_end_date()
