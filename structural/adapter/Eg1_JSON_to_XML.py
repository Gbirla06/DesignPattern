'''
    The Adapter Pattern is a Structural Design Pattern that allows two incompatible interfaces to work together without modifying their code.

    🛠 Why Do We Need an Adapter?

    Imagine you're trying to connect two different systems, but they have different interfaces. The adapter acts as a translator, making them compatible.

    📌 Example Problems Where Adapter Helps:

        🛑 Your new application expects XML, but the data provider sends JSON.
        🛑 You want to use an old library, but its interface doesn’t match your new system.
        🛑 You integrate a third-party payment gateway, but it requires different API calls than your system uses.

    🛠 Key Components of Adapter Pattern
        1.  Target :	The expected interface by the system.
        2.  Adaptee :	The existing class with an incompatible interface.
        3.  Adapter :	Converts Adaptee’s interface into Target’s interface.
        4.  Client :	Uses the Adapter to communicate with Adaptee.

    
    🔍 Real-Life Example: Power Adapter

        Imagine you have a laptop charger with a US plug, but you're in Europe with only European sockets. You need an adapter that allows you to plug in the US charger into a European socket.

            🔌 Target: European socket (expected interface).
            🔌 Adaptee: US charger plug (incompatible interface).
            🔌 Adapter: Power adapter that converts US plug → European socket.
            🔌 Client: You (using the laptop with the adapter).
'''

'''
    📖 Example 1: Converting JSON API to XML API

    Let’s say our system expects XML data, but we receive JSON data from a third-party API.

    Steps :
        🚀 Step 1: Define the Existing Class (Incompatible API)
        🚀 Step 2: Define the Expected Interface (Target)
        🚀 Step 3: Create the Adapter
        🚀 Step 4: Client Uses Adapter
'''


import json
from abc import ABC, abstractmethod

# 🚀 Step 1: Define the Existing Class (Incompatible API)
class JSONData :
    """Adaptee : Provides data in JSON format """

    def get_data(self) :
        return json.dumps({"name" : "Ganesh", "age" : 24})



# 🚀 Step 2: Define the Expected Interface (Target)
class XMLTarget(ABC) :
    """ Target Interface : Epected XML format """

    @abstractmethod
    def get_data(self) :
        pass


# 🚀 Step 3: Create the Adapter
class JSONtoXMLAdapter(XMLTarget) :
    """ Adapter : Converts JSON to XML """

    def __init__(self, json_provider : JSONData) :
        self.json_provider = json_provider

    def get_data(self) :
        json_data = self.json_provider.get_data()
        data_dict = json.loads(json_data)
        xml_data = f"<person><name>{data_dict['name']}</name><age>{data_dict['age']}</age></person>"
        return xml_data
    

# 🚀 Step 4: Client Uses Adapter

if __name__ == "__main__" :
    
    json_provider = JSONData()
    adapter = JSONtoXMLAdapter(json_provider)
    print(adapter.get_data())