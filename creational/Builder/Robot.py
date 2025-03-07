'''
    Builder Pattern Structure

    1️⃣ Builder Interface 🏗

        Declares common construction steps (set_engine(), set_seats(), etc.).
        Ensures consistency across different builders.

    2️⃣ Concrete Builders 🔨

        Implement the Builder interface in different ways.
        Each concrete builder produces a different type of product.

    3️⃣ Product 🎁

        The object being built step by step.
        Different builders may produce different types of products.

    4️⃣ Director 🎬Step 1: Define the Product (Robot)

        Defines the order in which the builder methods are called.
        Helps create specific, reusable configurations.

    5️⃣ Client 👤

        Assigns a Concrete Builder to the Director.
        Calls the director’s method to construct a product.


'''

from abc import ABC, abstractmethod


# Example 1:  🛠 Practical Example: Robot Builder

# Step 1: Define the Product (Robot)

class Robot :

    def __init__(self):
        self.head = None
        self.arms = None
        self.legs = None
        self.ai_enable = None
    
    def __str__(self):
        return f"🤖 Robot [Head : {self.head}, Arms : {self.arms}, Legs : {self.legs}, AI : {self.ai_enable}]"

# Step 2: Create the Builder Interface

class RobotBuilder(ABC) :

    @abstractmethod
    def set_head(self, head) :
        pass

    @abstractmethod
    def set_arms(self, arms) :
        pass

    @abstractmethod
    def set_legs(self, legs) :
        pass

    @abstractmethod
    def enable_ai(self) :
        pass

    @abstractmethod
    def build(self) :
        pass


# Step 3: Create Concrete Builders

class BasicRobotBuilder(RobotBuilder) :

    def __init__(self) :
        self.robot = Robot()

    def set_head(self, head) :
        self.robot.head = head
        return self

    def set_arms(self, arms) :
        self.robot.arms = arms
        return self
    
    def set_legs(self, legs) :
        self.robot.legs = legs
        return self

    def enable_ai(self) :
        self.robot.ai_enable = True
        return self

    def build(self) :
        return self.robot
    
# Step 4: Create the Director
class RobotDirector:

    def __init__(self, builder : RobotBuilder) :
        self.builder = builder

    def build_simple_robot(self) :
        self.builder.set_head("Metal Head")
        self.builder.set_arms("Basic Arms")
        self.builder.set_legs("Wheels")
        return self.builder.build()
    
    def build_ai_robot(self):
        self.builder.set_head("Advanced Head")
        self.builder.set_arms("Strong Arms")
        self.builder.set_legs("Bipedal Legs")
        self.builder.enable_ai()
        return self.builder.build()


# Step 5: Client Code
def client_code(robot_type: str) -> Robot :
    builder = BasicRobotBuilder()
    director = RobotDirector(builder=builder)

    if robot_type == "simple" :
        return director.build_simple_robot()
    elif robot_type == "ai_robot" :
        return director.build_ai_robot()
    else :
        raise ValueError("Unknown robot type given")
    

if __name__ == "__main__" :

    robot_type = input("Enter the robot type (simpe/ai_robot) : ")

    robot = client_code(robot_type)
    print(robot)


