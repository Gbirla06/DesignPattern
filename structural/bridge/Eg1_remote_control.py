'''
    The Bridge Pattern is a Structural Design Pattern that decouples abstraction from implementation, allowing them to develop independently.

    📌 Why?

        1.  Avoids a large, rigid inheritance hierarchy.
        2.  Improves code scalability and maintainability.
        3.  Helps if you have multiple dimensions of variations (e.g., different devices + different OS).

        🛠 Key Components of Bridge Pattern
                Component	                            Description
            1.  Abstraction	                            The high-level interface that clients interact with.
            2.  Refined Abstraction	                    A specific version of the abstraction.
            3.  Implementation Interface	            Defines an interface for different implementations.
            4.  Concrete Implementations	            Actual implementations that vary independently.

    
    📌 Steps to Implement Bridge Pattern

        1️⃣ Define the Implementation Interface → Create an interface that defines common operations for implementations.

        2️⃣ Create Concrete Implementations → Implement the interface for different variations (e.g., TV, Radio).

        3️⃣ Define the Abstraction Interface → Create a high-level interface that interacts with the implementation.

        4️⃣ Create Refined Abstractions → Extend the abstraction to add more features without modifying implementations.

        5️⃣ Use Composition → The abstraction holds a reference to an implementation and delegates calls to it.

        6️⃣ Client Code → Instantiate abstraction and pass different implementations to test flexibility.

        ✅ Done! You now have a decoupled system where abstraction and implementation can evolve         


    🎯 Real-Life Example: Remote Controls & Devices

    Imagine you have a remote control that works with different devices (TV, Radio).

        Remote Control → Abstraction (high-level interface).
        TV / Radio → Implementation (low-level details).

    
    Steps :
        🚀 Step 1: Create the Implementation Interface (Device)
        🚀 Step 2: Create Concrete Implementations (TV & Radio)
        🚀 Step 3: Create the Abstraction (Remote Control)
        🚀 Step 4: Create a Refined Abstraction (Advanced Remote)

        
    UML Diagram

         +--------------------+
         |  Abstraction       |
         |--------------------|
         | - device: Device   |  ◀─── HAS-A (Composition)
         |--------------------|
         | + turn_on()        |
         | + turn_off()       |
         | + volume_up()      |
         | + volume_down()    |
         | + channel_up()     |
         | + channel_down()   |
         +--------------------+
                   ▲
                   │
                   │ (inherits)
                   ▼
         +--------------------+
         |  RefinedAbstraction|
         |--------------------|
         | + mute()           |
         +--------------------+

                   🔽 Uses Composition  

+------------------+          +------------------+
|  Device         |◀───(Interface)──▶|  Concrete Device  |
|-----------------|                  |------------------|
| + isEnabled()   |                  | + isEnabled()    |
| + enable()      |                  | + enable()       |
| + disable()     |                  | + disable()      |
| + getVolume()   |                  | + getVolume()    |
| + setVolume()   |                  | + setVolume()    |
| + getChannel()  |                  | + getChannel()   |
| + setChannel()  |                  | + setChannel()   |
+-----------------+                  +------------------+
                                         ▲        ▲
                                         │        │
                                         ▼        ▼
                                 +-----------+  +-----------+
                                 |    TV     |  |   Radio   |
                                 +-----------+  +-----------+  

    



'''



from abc import ABC, abstractmethod

# 1️⃣ Step 1: Create the Implementation Interface (Device)

class Device(ABC) :

    """Implementation Interface: Device"""

    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def get_volume(self):
        pass

    @abstractmethod
    def set_volume(self):
        pass

    @abstractmethod
    def get_channel(self):
        pass

    @abstractmethod
    def set_channel(self):
        pass


# 2️⃣ Step 2: Create Concrete Implementations (TV and Radio)

class TV(Device) :
    
    """Concrete Implementation: TV"""

    def __init__(self) :
        self.enabled = False
        self.volume = 50
        self.channel = 1

    def is_enabled(self) :
        return self.enable
    
    def enable(self) :
        self.enable = True
        print("TV is now ON")
    
    def disable(self) :
        self.enable = False
        print("TV is now OFF")
    
    def get_volume(self) :
        return self.volume
    
    def set_volume(self, val: int) :
        self.volume = max(0, min(100, val))
        print(f"TV Volume is {self.volume}")

    def get_channel(self) :
        return self.channel
    
    def set_channel(self, channel: int) :
        if channel > 0 :
            self.channel = channel
        print(f"TV channel set to {self.channel}")


class Radio(Device) :
    """Concrete Implementation: Radio"""

    def __init__(self) :
        self.enabled = False
        self.volume = 30
        self.channel = 90.1  # FM Frequency
    
    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True
        print("Radio is now ON")

    def disable(self):
        self.enabled = False
        print("Radio is now OFF")

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = max(0, min(volume, 100))
        print(f"Radio volume set to {self.volume}")

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if channel > 0 :
            self.channel = channel
        print(f"Radio frequency set to {self.channel} MHz")


# 3️⃣ Step 3: Create the Abstraction (RemoteControl)

class RemoteControl :
    """Abstraction: Remote Control"""

    def __init__(self, device: Device) :
        self.device = device        # Composition: Remote HAS-A Device

    def turn_on(self) :
        self.device.enable()
    
    def turn_off(self) :
        self.device.disable()
    
    def volume_up(self) :
        self.device.set_volume(self.device.get_volume()+1)
    
    def volume_down(self) :
        self.device.set_volume(self.device.get_volume()-1)

    def channel_up(self) :
        self.device.set_channel(self.device.get_channel()+1)

    def channel_down(self) :
        self.device.set_channel(self.device.get_channel()-1)


# 4️⃣ Step 4: Create Refined Abstraction (AdvancedRemote)
class AdvancedRemote(RemoteControl) :
    """Refined Abstraction: Advanced Remote with Mute"""

    def mute(self) :
        self.device.set_volume(0)
        print(f"{self.device.__class__.__name__} is Muted")


# 5️⃣ Step 5: Client Code
def client_helper(device, is_advanced_remote = False) :

    remote = RemoteControl(device) if is_advanced_remote is False else AdvancedRemote(device)
    remote.turn_on()
    remote.volume_up()
    remote.channel_up()
    if is_advanced_remote is True:
        remote.mute()
    
    remote.turn_off()

    print("\n-------------------------------------\n")


if __name__ == "__main__" :

    device = input("Enter the Device (TV/Radio) : ")
    if device == "TV" :
        tv = TV()
        client_helper(tv)
    elif device == "Radio" :
        radio = Radio()
        client_helper(radio, is_advanced_remote=True)
    else :
        raise ValueError("Invalid Device")
