'''
    The Prototype Pattern is used when you need to create new objects by copying (cloning) an existing object instead of building from scratch. 
    It helps in cases where object creation is expensive (e.g., deep-copying large objects).

    📍 Key Idea: Instead of creating an object from scratch, clone an existing one.


    🛠 When to Use Prototype Pattern?

        ✅ When object creation is costly (e.g., deep copies of complex objects).
        ✅ When we need different configurations of the same object.
        ✅ When we want to avoid calling the constructor repeatedly.


    All Steps :
        Step 1: Define the Prototype Interface 
            -> The Prototype interface declares the cloning methods. In most cases, it’s a single clone method.
        
        Step 2: Create a Concrete Prototype (Game Character)
            -> The Concrete Prototype class implements the cloning method. In addition to copying the original object’s data to the clone, 
               this method may also handle some edge cases of the cloning process related to cloning linked objects, untangling recursive dependencies, etc.

        Step 3: Client Code (Cloning Characters)
            -> The Client can produce a copy of any object that follows the prototype interface.

'''




from abc import ABC, abstractmethod
import copy


# Step 1: Define the Prototype Interface 
class Prototype(ABC) :

    @abstractmethod
    def clone(self) :
        pass


# Step 2: Create a Concrete Prototype (Game Character)
class GameCharacter(Prototype) :

    def __init__(self, name, weapon, health) :
        self.name = name
        self.weapon = weapon
        self.health = health
    
    def clone(self) :
        return copy.deepcopy(self)
    
    def __str__(self) :
        return f"👾 {self.name} | Weapon: {self.weapon} | Health: {self.health}"


# Step 3: Client Code (Cloning Characters)

def client_helper(name, weapon, health) :
    
    player = GameCharacter(name, weapon, health)

    return player


if __name__ == "__main__" :
    player_name = input("Enter player name : ")
    
    player1 = client_helper(player_name, "Axe", 100)

    print(player1)

    player2 = player1.clone()
    player2.name = "Copied Player"
    player2.weapon = "Bow"

    print(player2)
    