class Employee: #Create employee class
    def __init__(self, employeeid, employeename): #Define Employee class with self object, employeeid/employeename attributes.
        self.employeeid = employeeid #instantiate employeeid attribute and assign it to employeeid variable
        self.employeename = employeename #instantiate employeename attribute and assign it to employeename variable
        self.employeesalary = None

    def calaculatesalary(self): #Create method for if Employee abstract class is instantiated directly.
        raise NotImplementedError("Subclass has no implemented method") #Raise exception


class Hourly(Employee): #Create Hourly subclass of Employee class.
    def __init__(self, employeeid, employeename): # Define self object and employeeid/employeename attributes
        Employee.__init__(self, employeeid, employeename) # Define constructor for the attributes from base class for subclass
        self.hoursworked = None #Define new attribute hoursworked and set it to null.
        self.payrate = None #Define new attribute payrate and set it to null.

    def calaculatesalary(self): #Create Method for the Hourly Subclass.
        self.hoursworked = input("How many hours did this employee work in a week?: ") # Set hoursworked attribute to user input to ask for this value
        self.payrate = input("Employee pay rate: ") # Set payrate attribute to user input to ask for this value.
        self.employeesalary = int(self.hoursworked)*float(self.payrate)*52 #Set employeesalary to Hourly subclass salary calculation.


class SalarySupervisor(Employee): # Create Salary subclass of Employee class.
    def __init__(self, employeeid, employeename): # Define self object with employeeid/employeename attributes
        Employee.__init__(self, employeeid, employeename) # Define constructor for the attributes from base class for subclass
        self.yearsworked = None #Define null attribute yearsworked for self object in SalarySupervisor subclass.
        self.basesalary = None #define null attribute base salary for self object in SalarySupervisor subclass.

    def calaculatesalary(self): # Define calculatesalary method for SalarySupervisor
        self.yearsworked = int(input("How many years has this employee worked for the company?: "))# Get yearsworked user input for later salaray calculation
        self.basesalary = input("What is this employee's base salary?: ") # Get base salary user input for later salaray calculation
        if self.yearsworked <=5: #Create if statement to determin how to calculate employee salary based on years worked.
            self.employeesalary = int(self.basesalary) #If employee has worked 5 years or less than salary = base salary.
        else:
            self.employeesalary = int(self.basesalary)*1.5 #If employee worked greater than 5 years add 50% base salary bonus.


employee = list() # Create list titled employee to store employees.
employee.append(Hourly(1111, "Alice")) # Add hourly employee to employee list
employee.append(SalarySupervisor(2222, "Betty")) #Add SalarySupervisor epmployee to list.
for empl in employee: # Create for loop
    empl.calaculatesalary() #Use polymorphism to implement calaculatyesalary method for each subclass.
    print(empl.employeename, "has a salary of", empl.employeesalary,"per year.") #Print employee list id ,name, and calculated salary.







