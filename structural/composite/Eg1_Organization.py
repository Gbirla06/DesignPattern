'''
    The Composite Pattern is a structural design pattern that lets you compose objects into tree structures to represent part-whole hierarchies. 
    It treats individual objects and compositions of objects uniformly.

    ----------------------------------------------------------------------------------------------------------------------------------------------
    
    🔹 Why Use the Composite Pattern?

        ✅ When you need to treat individual objects and groups of objects the same way.
        ✅ When dealing with tree-like structures (e.g., file systems, UI components, organization hierarchies).
        ✅ When applying the Open/Closed Principle (you can add new components without modifying existing code).

    ----------------------------------------------------------------------------------------------------------------------------------------------
        
    🔹 Real-World Analogy

        Think about a company’s organizational hierarchy:

            A CEO can have Managers under them.
            Each Manager can have employees or more Managers under them.
            But at every level, we should be able to call the same function (e.g., showDetails()) to get the hierarchy.

        This is where Composite Pattern helps! ✅

    ----------------------------------------------------------------------------------------------------------------------------------------------

    UML Diagram For Organization

                        ┌───────────────┐
                        │  Component    │  <--- Abstract Class (Employee)
                        │  + showDetails() │
                        └───────┬───────┘
                                │
            ┌─────────────────────────┐
            │                         │
        ┌───────────────┐     ┌─────────────────┐
        │   Leaf        │     │ Composite        │
        │   (Employee)  │     │ (Manager)        │
        │ + showDetails() │     │ + addEmployee() │
        └───────────────┘     │ + removeEmployee() │
                            │ + showDetails()   │
                            └─────────────────┘

        Component (Abstract Class) → Defines common methods for showDetails().
        Leaf (Employee Class) → Represents individual objects.
        Composite (Manager Class) → Holds multiple Leaf and Composite objects.

    ----------------------------------------------------------------------------------------------------------------------------------------------
    
    We will implement the Company Employee Hierarchy using Python and Composite Pattern.
    
    Steps :

        Step 1: Create an Abstract Component (Base Class)
        Step 2: Create Leaf (Individual Employees)
        Step 3: Create Composite Class (Managers)
        Step 4: Client Code (Build Hierarchy)
        
    ----------------------------------------------------------------------------------------------------------------------------------------------

'''

from abc import ABC, abstractmethod


# Step 1: Create an Abstract Component (Base Class)
# # Abstract Component

class Employee(ABC) :
    
    @abstractmethod
    def showDetails(self) :
        pass

# Step 2: Create Leaf (Individual Employees)
# Leaf class (Individual Employees)

class Developer(Employee) :

    def __init__(self, name, position) :
        self.name = name
        self.position = position
    
    def showDetails(self) :
        print(f"{self.position} : {self.name}")
    

class Designer(Employee) :

    def __init__(self, name , position) :
        self.name = name
        self.position = position
    
    def showDetails(self) :
        print(f"{self.position} : {self.name}")
        
        
# Step 3: Create Composite Class (Managers)
# Composite class (Managers)

class Manager(Employee) :

    def __init__(self, name, position) :
        self.name = name
        self.position = position
        self.subordinates = []          # Holds Employees
    
    def addEmployee(self, employee) :
        self.subordinates.append(employee)
    
    def removeEmployee(self, employee) :
        self.subordinates.remove(employee)
    
    def showDetails(self) :
        print(f"\n{self.position} : {self.name}")
        print("Subordinates:")
        
        for emp in self.subordinates :
            emp.showDetails()    # Calls showDetails() recursively



# Step 4: Client Code (Build Hierarchy)
# Client Code

if __name__ == "__main__" :

    # Creating Individual Employees (Leaves)

    dev1 = Developer("Alice", "Software Engineer")
    dev2 = Developer("Alice", "Senior Software Engineer")
    designer1 = Designer("Charlie", "UI/UX Designer")

    # Creating Manger (Composite)
    manager1 = Manager("David", "Engineering Manager")
    manager1.addEmployee(dev1)
    manager1.addEmployee(designer1)

    # Creating a Higher-Level Manger
    ceo = Manager("Ganesh", "CEO")
    ceo.addEmployee(dev2)
    ceo.addEmployee(manager1)

    # Display the hierarchy
    ceo.showDetails()