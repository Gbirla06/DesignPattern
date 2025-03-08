'''
    🚀 Another Real-World Example: File System (Folders & Files)

    A File System is a perfect example of the Composite Pattern.

        A Folder can contain Files or other Folders (which can contain more files and folders).
        The client should be able to treat both Files and Folders the same way using a common interface.

-------------------------------------------------------------------------------------------------------------------------------------------------

    🔹 UML Diagram for File System

                 ┌───────────────┐
                 │  FileSystem   │  <--- Abstract Class (Component)
                 │  + showDetails() │
                 └───────┬───────┘
                         │
    ┌─────────────────────────┐
    │                         │
┌───────────────┐     ┌─────────────────┐
│   Leaf        │     │ Composite       │
│   (File)      │     │ (Folder)        │
│ + showDetails()│     │ + add()        │
└───────────────┘     │ + remove()      │
                      │ + showDetails() │
                      └─────────────────┘


        Components :                      
            FileSystem (Component) → Defines a common method showDetails()
            File (Leaf Class) → Represents an individual file
            Folder (Composite Class) → Can hold multiple Files and Folders



-------------------------------------------------------------------------------------------------------------------------------------------------


        Steps :
            Step 1: Create an Abstract Component
            Step 2: Create Leaf Class (File)
            Step 3: Create Composite Class (Folder)
            Step 4: Client Code (Build File System Hierarchy)
'''

from abc import ABC, abstractmethod


# Step 1: Create an Abstract Component

class FileSystem(ABC) :

    @abstractmethod
    def showDetails(self) :
        pass


# Step 2: Create Leaf Class (File)

class File(FileSystem) :

    def __init__(self, name) :
        self.name = name
    
    def showDetails(self, indent=0) :
        print(" " * indent + f"📄 {self.name}")
    

# Step 3: Create Composite Class (Folder)

class Folder(FileSystem) :
    
    def __init__(self, name) :
        self.name = name
        self.children = []
    
    def add(self, item : FileSystem) :
        self.children.append(item)
    
    def remove(self, item : FileSystem) :
        self.children.remove(item)

    def showDetails(self, indent = 0) :
        print(" " * indent + f"📁 {self.name}")  # Print folder name

        for child in self.children :
            child.showDetails(indent+4)   #Indent child items



# Step 4: Client Code (Build File System Hierarchy)

if __name__ == "__main__" :
    
    # Creating Files

    file1 = File("resume.pdf")
    file2 = File("project.docx")
    file3 = File("photo.jpg")
    file4 = File("meriduniya.mp3")

    # Creating Folders
    downloads = Folder("Downloads")
    documents = Folder("Documents")

    downloads.add(file4)
    documents.add(file1)
    documents.add(file2)
    documents.add(file3)


    # Creating Root Folder
    root = Folder("Root")
    root.add(downloads)
    root.add(documents)

    # Display File System Hierarchy
    root.showDetails()
