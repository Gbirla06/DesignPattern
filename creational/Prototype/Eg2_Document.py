'''
    Imagine you're working with a document editor, and you want to allow users to duplicate a document while modifying some parts (e.g., title, author). 
    Instead of creating a new document from scratch, we clone an existing one.

    Steps Required:
        Step 1: Define the Prototype Interface         
        Step 2: Create a Concrete Prototype (Document)
        Step 3: Client Code (Cloning Characters)

'''

from abc import ABC, abstractmethod
import copy
from typing import Optional

# Step 1: Define the Prototype Interface

class Prototype(ABC) :
    
    @abstractmethod
    def clone(self) :
        pass


# Step 2: Create a Concrete Prototype (Document)
class Document(Prototype) :

    def __init__(self, title, author, content) :
        self.title = title
        self.author = author
        self.content = content
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self) :
        return f"📄 Title: {self.title} | Author: {self.author}\nContent: {self.content[:30]}..."
    

# Step 3: Client Code (Cloning Documents)
def client_helper(original_document: Document, new_title : str, new_author : Optional[str] = None, new_content : Optional[str] = None) -> Document:
    
    new_document = original_document.clone()
    new_document.title = new_title

    if new_author is not None :
        new_document.author = new_author
    
    if new_content is not None :
        new_document.content = new_content

    return new_document


if __name__ == "__main__" :
    
    title = input("Enter Document Title : ")
    author = input("Enter Document author : ")
    content = input("Enter Document content : ")

    first_document = Document(title, author, content)
    print(first_document)

    second_document = client_helper(first_document, "Second Book", "Priyanshu")
    print(second_document)

    
