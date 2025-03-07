'''
    The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.
    When to Use Abstract Factory?

        When you need to create objects that belong to multiple related families.
        When you want to enforce consistency among created objects.
        When your system should be independent of how objects are created.

    Structure

        Abstract Factory: Declares creation methods for different product types.
        Concrete Factories: Implement the creation methods for specific families of products.
        Abstract Product: Declares an interface for a product type.
        Concrete Product: Implements the product interface.
        Client: Uses the factory to create products without knowing their concrete classes.

'''

############################################################################################################################################

from abc import ABC, abstractmethod

# Step 1 :  Create Abstract Product
# Abstract Product 1
class Button(ABC):

    @abstractmethod
    def render(self) :
        pass

# Abstract Product 2
class CheckBox(ABC):

    @abstractmethod
    def render(self):
        pass


# Step 2 : Create Concrete Product
# Concrete Product A1
class MacButton(Button) :

    def render(self) :
        print("Rendering Mac Button")

# Concrete Product A2
class WindowsButton(Button) :

    def render(self) :
        print("Rendering Windows Button")

# Concrete Product B1
class MacCheckBox(CheckBox):

    def render(self) :
        print("Rendering Mac Check Box")

# Concrete Product B2
class WindowsCheckBox(CheckBox):

    def render(self):
        print("Rendering Windows Check Box")

############################################################################################################################################



# Step 3 : Create Abstract Factory
# Abstract Factory
class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button :
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox :
        pass



# Step 4 : Create Concrete Factory
# Concrete Factory 1
class MacFactory(GUIFactory) :

    def create_button(self) -> Button :
        return MacButton()

    def create_checkbox(self) -> CheckBox :
        return MacCheckBox()
    
# Concrete Factory 2
class WindowsFactory(GUIFactory) :

    def create_button(self) -> Button :
        return WindowsButton()
    
    def create_checkbox(self) -> CheckBox :
        return WindowsCheckBox()
    


# Step 5 : Client Code 
def render_ui(factory: GUIFactory) :
    
    button = factory.create_button()
    checkbox = factory.create_checkbox()


    button.render()
    checkbox.render()


if __name__ == "__main__" :

    platform = "mac"

    factory : GUIFactory

    if platform == "windows" :
        factory = WindowsFactory()
    else :
        factory = MacFactory()

    render_ui(factory)