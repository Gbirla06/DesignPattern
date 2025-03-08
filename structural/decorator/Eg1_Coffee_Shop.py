'''
    The Decorator Pattern is a Structural Design Pattern that allows behavior to be added to an individual object, dynamically and without modifying the original class. 
    This pattern is widely used in scenarios where extending functionality at runtime is needed, without modifying existing code.

    🔹 Why Do We Need the Decorator Pattern?

        Avoids Subclass Explosion – Instead of creating multiple subclasses for different combinations, we use composition.
        Follows Open/Closed Principle (OCP) – We can add new behaviors without modifying existing code.
        Improves Maintainability – Each feature (or behavior) is encapsulated in a separate class, making it easier to modify or extend.

    
    🚫 Bad Approach (Without Decorator)

    Imagine a coffee shop where we offer different types of coffee:

        Plain Coffee
        Coffee with Milk
        Coffee with Sugar
        Coffee with Milk and Sugar
        Coffee with Caramel

    We could try to create subclasses for each combination, but this would lead to exponential subclass growth: This is not scalable and violates the Open/Closed Principle.

    ✅ Better Approach (With Decorator)

        Instead of modifying the original Coffee class or creating multiple subclasses, we wrap the object dynamically with decorators.
        This allows us to add features at runtime, making our code flexible and modular.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    🔹 Structure of the Decorator Pattern

        The Decorator Pattern follows a layered structure, where each decorator extends the functionality of an existing object.
        📌 Components of the Decorator Pattern

            1.  Component (Interface/Abstract Class)
                    * Defines the common behavior that will be implemented by both the base class and decorators.
            2.  Concrete Component (Base Class)
                    * The original class that we want to extend dynamically.
            3.  Decorator (Abstract Class)
                    * Wraps the Component and delegates the behavior.
            4.  Concrete Decorators (Feature Add-ons)
                    * Modify behavior dynamically by extending the Decorator.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
    🔹 How the Decorator Pattern Works
        Step-by-Step Execution

            The client creates a base object (e.g., Coffee).
            The base object is wrapped by a decorator (e.g., Milk).
            The decorator modifies the behavior dynamically (e.g., adds Milk cost and description).
            Multiple decorators can be stacked, each modifying the object dynamically.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    🔹 Advantages of the Decorator Pattern

        ✅ Flexible and Extensible – Easily add new behaviors without modifying existing code.
        ✅ Runtime Modification – Behaviors can be added or removed dynamically.
        ✅ Avoids Inheritance Explosion – Eliminates the need for multiple subclasses.
        ✅ Follows SOLID Principles – Specifically OCP (Open/Closed Principle) and SRP (Single Responsibility Principle).

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    🔹 Real-World Use Cases of the Decorator Pattern
            Use Case	How Decorator Helps
        1.  Graphical UI Frameworks	                        -> Adding scrollbars, borders, themes, etc., dynamically.
        2.  Text Processing (IDE, Word Processors)	        -> Adding bold, italic, underline styles dynamically.
        3.  Middleware in Web Frameworks	                -> Adding authentication, logging, caching dynamically.
        4.  Java I/O Streams	                            -> Wrapping FileReader inside BufferedReader, DataInputStream, etc.
        5.  Notification Systems	                        -> Sending notifications via Email, SMS, Push using decorators.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''


'''
    1.  Real-World Example: Coffee Shop ☕
            Step 1: Create Abstract Component (Beverage)
            Step 2: Create Concrete Component (Coffee)
            Step 3: Create Abstract Decorator (AddonDecorator)
            Step 4: Create Concrete Decorators (Milk, Sugar, Caramel)
            Step 5: Client Code (Ordering Custom Coffee)

            

    2.  UML Diagram

               ┌───────────────┐
               │  Beverage     │  <--- Abstract Component
               │  + cost()     │
               │  + description() │
               └───────┬───────┘
                       │
       ┌───────────────┴──────────────┐
       │                               │
┌───────────────┐               ┌────────────────────┐
│  Coffee       │               │  AddonDecorator    │  <--- Abstract Decorator
│  + cost()     │               │  + cost()          │
│  + desc()     │               │  + desc()          │
└───────────────┘               └────────────────────┘
                                       │
          ┌────────────────────────────┴─────────────────────┐
          │                           │                      │
 ┌───────────────┐       ┌────────────────────┐    ┌─────────────────┐
 │  Milk         │       │  Sugar             │    │  Caramel        │
 │  + cost()     │       │  + cost()          │    │  + cost()       │
 │  + desc()     │       │  + desc()          │    │  + desc()       │
 └───────────────┘       └────────────────────┘    └─────────────────┘


'''



from abc import ABC, abstractmethod

# Step 1: Create Abstract Component (Beverage)

class Beverage(ABC) :

    @abstractmethod
    def cost(self) :
        pass

    @abstractmethod
    def description(self) :
        pass


# Step 2: Create Concrete Component (Coffee)

class Coffee(Beverage) :
    
    def cost(self) :
        return 50   # Base price of Coffee
    
    def description(self) :
        return "Plain Coffee"


# Step 3: Create Abstract Decorator (AddonDecorator)

class AddonDecorator(Beverage, ABC) :

    def __init__(self, beverage : Beverage) :
        self.beverage = beverage

    def cost(self) :
        return self.beverage.cost()

    def description(self) :
        return self.beverage.description()
    

# Step 4: Create Concrete Decorators (Milk, Sugar, Caramel)

class Milk(AddonDecorator) :
    
    def cost(self) :
        return self.beverage.cost() + 10    # Adding milk costs 10
    
    def description(self) :
        return self.beverage.description() + " + Milk"

class Sugar(AddonDecorator) :
    
    def cost(self) :
        return self.beverage.cost() + 5     #Adding sugar costs 5
    
    def description(self) :
        return self.beverage.description() + " + Sugar"
    
class Caramel(AddonDecorator) :
    
    def cost(self) :
        return self.beverage.cost() + 20    # Adding caramel costs 20

    def description(self) :
        return self.beverage.description() + " + Caramel"
    


# Step 5: Client Code (Ordering Custom Coffee)

if __name__ == "__main__" :

    # Order a plain coffee

    coffee = Coffee()
    print(f"{coffee.description()} : ₹{coffee.cost()}")


    # Order Coffee with Milk
    coffee_with_milk = Milk(coffee)
    print(f"{coffee_with_milk.description()} : ₹{coffee_with_milk.cost()}")


    # Order Coffee with Milk and Sugar
    coffee_with_milk_sugar = Sugar(coffee_with_milk)
    print(f"{coffee_with_milk_sugar.description()} : ₹{coffee_with_milk_sugar.cost()}")


    # Order Coffee with all add-ons
    deluxe_coffee = Caramel(coffee_with_milk_sugar)
    print(f"{deluxe_coffee.description()} : ₹{deluxe_coffee.cost()}")






