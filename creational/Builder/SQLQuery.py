'''
    This example will implement a Builder Pattern to construct SQL queries dynamically. 
    Instead of manually concatenating strings, we’ll use a builder to create queries step by step.

    🛠 Steps to Implement SQL Query Builder

        ✅ Step 1: Define the Product (SQL Query)
        ✅ Step 2: Create the Builder Interface
        ✅ Step 3: Implement Concrete Builder (SQLQueryBuilder)
        ✅ Step 4: Create the Director (Predefined Queries)
        ✅ Step 5: Client Code Usage

'''


from abc import ABC, abstractmethod

# Step 1: Define the Product (SQL Query)
class SQLQuery :
    
    def __init__(self) :
        self.query = ""
    
    def __str__(self) :
        return self.query
    

# Step 2: Create the Builder Interface
class SQLQueryBuilder(ABC) :

    @abstractmethod
    def select(self, table, columns) :
        pass

    @abstractmethod
    def where(self, condition) :
        pass

    @abstractmethod
    def order_by(self, column, order) :
        pass

    @abstractmethod
    def limit(self, count) :
        pass

    @abstractmethod
    def build(self) :
        pass


# Step 3: Implement the Concrete Builder
class SQLConcreteBuilder(SQLQueryBuilder) :

    def __init__(self) :
        self.query = SQLQuery()

    def select(self, table, columns) :
        col_str = ", ".join(columns)
        self.query.query = f"SELECT {col_str} FROM {table}"
        return self
    
    def where(self, condition) :
        self.query.query += f" WHERE {condition}"
        return self
    
    def order_by(self, column, order="ASC") :
        self.query.query += f" ORDER BY {column} {order}"
        return self
    
    def limit(self, count) :
        self.query.query += f" LIMIT {count}"
        return self
    
    def build(self) :
        return self.query
    

        
# Step 4: Create the Director

class SQLQueryDirector :
    def __init__(self, builder : SQLQueryBuilder) :
        self.builder = builder
    
    def build_user_query(self) :
        return self.builder.select("users", ["id", "name", "email"]).where("age > 18").order_by("name", "DESC").build()
    
    def build_product_query(self) :
        return self.builder.select("products", ["id", "name", "price"]).where("price < 1000").limit(10).build()
    


# Step 5: Client Code
def client_code(query_type: str) -> SQLQuery :
    builder = SQLConcreteBuilder()
    director = SQLQueryDirector(builder=builder)

    if query_type == "user" :
        return director.build_user_query()
    elif query_type == "product" :
        return director.build_product_query()
    else :
        raise ValueError("Unknown query type given")
    

if __name__ == "__main__" :

    query_type = input("Enter the SQL Query type (user/product) : ")

    query = client_code(query_type)
    print(query)