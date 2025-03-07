import threading


class Singleton :
    _instance = None
    _lock = threading.Lock()

    def __new__(cls) :
        with cls._lock:
            if cls._instance is None :
                cls._instance  = super().__new__(cls)
            return cls._instance
        

obj1 = Singleton()
obj2 = Singleton()

print(id(obj1))
print(id(obj2))

print(id(obj1) == id(obj2))
