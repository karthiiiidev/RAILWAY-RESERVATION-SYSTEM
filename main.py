# Hierarchical Inheritance

# Base class

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class 1
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")

# # Derived class 2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")

# # Driver code
# object1 = Child1()
# object2 = Child2()

# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


#hybrid inheritance


# Base class

# class School:
#     def func1(self):
#         print("This function is in school.")

# # Derived class 1 (Single Inheritance)
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1.")

# # Derived class 2 (Another Single Inheritance)
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")

# # Derived class 3 (Multiple Inheritance)
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")

# # Driver code
# obj = Student3()
# obj.func1()
# obj.func2()


#1

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, roll_number):
#         super().__init__(name, age)
#         self.roll_number = roll_number

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Roll Number: {self.roll_number}")

# student = Student("Alice", 20, 101)
# student.display_details()


#2 Multiple Inheritance

# class Sports:
#     def __init__(self, sports_marks):
#         self.sports_marks = sports_marks

# class Academics:
#     def __init__(self, academic_marks):
#         self.academic_marks = academic_marks

# class Result(Sports, Academics):
#     def __init__(self, sports_marks, academic_marks):
#         Sports.__init__(self, sports_marks)
#         Academics.__init__(self, academic_marks)

#     def display_total(self):
#         total = self.sports_marks + self.academic_marks
#         print(f"Sports Marks: {self.sports_marks}")
#         print(f"Academic Marks: {self.academic_marks}")
#         print(f"Total Marks: {total}")

# result = Result(85, 92)
# result.display_total()


#3 Multilevel Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id

# class Manager(Employee):
#     def __init__(self, name, employee_id, department):
#         super().__init__(name, employee_id)
#         self.department = department

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Department: {self.department}")

# manager = Manager("John Doe", "E104", "Engineering")
# manager.display_details()


#4 Hierarchical Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, roll_number):
#         super().__init__(name)
#         self.roll_number = roll_number

#     def display_student(self):
#         print(f"Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")

# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject

#     def display_teacher(self):
#         print(f"Name: {self.name}")
#         print(f"Subject: {self.subject}")

# student = Student("Alice", 101)
# teacher = Teacher("Mr. Smith", "Physics")

# print("--- Student Details ---")
# student.display_student()

# print("\n--- Teacher Details ---")
# teacher.display_teacher()


#5 Hybrid Inheritance

# class Employee:
#     def __init__(self, name, **kwargs):

#         super().__init__() 
#         self.name = name

# class Developer(Employee):
#     def __init__(self, programming_language, **kwargs):

#         super().__init__(**kwargs)
#         self.programming_language = programming_language

# class Tester(Employee):
#     def __init__(self, testing_tool, **kwargs):

#         super().__init__(**kwargs)
#         self.testing_tool = testing_tool

# class TeamLead(Developer, Tester):
#     def __init__(self, name, programming_language, testing_tool):

#         super().__init__(
#             name=name, 
#             programming_language=programming_language, 
#             testing_tool=testing_tool
#         )

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Programming Language: {self.programming_language}")
#         print(f"Testing Tool: {self.testing_tool}")


# lead = TeamLead("Alex", "Python", "Sandbox")
# lead.display_details()


#RAILWAY RESERVATION SYSTEM

class Passenger:
    def __init__(self, passenger_id, name, age, gender, mobile):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

    def display_passenger(self):
        print(f"Passenger Name : {self.name}")
        print(f"Age            : {self.age}")
        print(f"Gender         : {self.gender}")


class Train:
    def __init__(self, train_num, train_name, source, destination, total_seats, fare):
        self.train_num = train_num
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_ticket = fare

    def display_train_details(self):
        print(f"Train No: {self.train_num} | Name: {self.train_name} | Route: {self.source} -> {self.destination} | Fare: ₹{self.fare_per_ticket} | Available Seats: {self.available_seats}/{self.total_seats}")

    def check_availability(self, seats):
        return self.available_seats >= seats

    def book_seats(self, seats):
        if self.check_availability(seats):
            self.available_seats -= seats
            return True
        return False

    def cancel_seats(self, seats):
        self.available_seats += seats


class Ticket:
    def __init__(self, passenger, train, seats_booked):
        self.passenger = passenger
        self.train = train
        self.seats_booked = seats_booked
        self.ticket_number = f"{passenger.name}{passenger.passenger_id}"
        self.total_fare = self.calculate_fare()
        self.status = "Booked"

    def calculate_fare(self):
        return self.seats_booked * self.train.fare_per_ticket

    def cancel_ticket(self):
        if self.status == "Booked":
            self.status = "Cancelled"
            self.train.cancel_seats(self.seats_booked)
            return True
        return False

    def display_ticket_details(self):
        print("-" * 34)
        print(f"Ticket Number : {self.ticket_number}\n")
        self.passenger.display_passenger()
        print(f"\nTrain Number   : {self.train.train_num}")
        print(f"Train Name     : {self.train.train_name}")
        print(f"\nSeats Booked   : {self.seats_booked}")
        print(f"Total Fare     : ₹{self.total_fare}")
        print(f"\nStatus         : {self.status}")
        print("-" * 34)


class RailwaySystem:
    def __init__(self):

        self.trains = {
            "12627": Train("12627", "Kerala Express", "New Delhi", "Trivandrum", 200, 450),
            "12952": Train("12952", "Mumbai Rajdhani", "New Delhi", "Mumbai", 150, 700),
            "12002": Train("12002", "Bhopal Express", "New Delhi", "Bhopal", 100, 350)
        }
        self.tickets = {} 

    def book_ticket_flow(self):
        print("\n--- Step 1: Enter Passenger Details ---")
        pid = input("Enter Passenger ID: ")
        name = input("Enter Passenger Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        mobile = input("Enter Mobile Number: ")
        
        passenger = Passenger(pid, name, age, gender, mobile)

        print("\n--- Step 2: Available Trains ---")
        for train in self.trains.values():
            train.display_train_details()

        print("\n--- Step 3 & 4: Select Train & Seats ---")
        train_num = input("Enter the train number for reservation: ")
        
        if train_num not in self.trains:
            print("Invalid Train Number!")
            return

        selected_train = self.trains[train_num]
        
        try:
            seats = int(input("Enter number of seats required: "))
        except ValueError:
            print("Invalid number of seats!")
            return


        if selected_train.book_seats(seats):
            new_ticket = Ticket(passenger, selected_train, seats)
            self.tickets[new_ticket.ticket_number] = new_ticket
            print("\nBooking Confirmation:")
            new_ticket.display_ticket_details()
        else:
            print("\nSeats Not Available!")

    def cancel_ticket_flow(self):
        ticket_num = input("Enter the ticket number to cancel: ")
        if ticket_num in self.tickets:
            ticket = self.tickets[ticket_num]
            if ticket.status == "Cancelled":
                print("Ticket is already cancelled.")
            elif ticket.cancel_ticket():
                print("\nCancellation confirmation successfully processed!")
        else:
            print("Ticket Number Not Found!")

    def check_seat_availability_flow(self):
        print("\n--- Seat Availability ---")
        for train in self.trains.values():
            print(f"Train No        : {train.train_num}")
            print(f"Train Name      : {train.train_name}")
            print(f"Total Seats     : {train.total_seats}")
            print(f"Available Seats : {train.available_seats}")
            print("-" * 30)

    def display_ticket_flow(self):
        ticket_num = input("Enter ticket number: ")
        if ticket_num in self.tickets:
            self.tickets[ticket_num].display_ticket_details()
        else:
            print("Ticket Number Not Found!")



system = RailwaySystem()
    
while True:
        print("\n===== Railway Reservation System =====")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Check Seat Availability")
        print("4. Display Ticket Details")
        print("5. Exit")
        
        choice = input("\nEnter Your Choice : ")
        
        if choice == "1":
            system.book_ticket_flow()
        elif choice == "2":
            system.cancel_ticket_flow()
        elif choice == "3":
            system.check_seat_availability_flow()
        elif choice == "4":
            system.display_ticket_flow()
        elif choice == "5":
            print("Thank you for using the Railway Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-5).")