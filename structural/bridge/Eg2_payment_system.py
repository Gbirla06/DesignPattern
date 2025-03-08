'''
    📌 Real-Life Example: Payment System (UPI, Credit Card, PayPal)

    Imagine you are developing a payment processing system where you need to support different payment methods (UPI, Credit Card, PayPal) 
    and different banks/gateways (HDFC, SBI, PayPal Gateway).


                +---------------------+
                |  IPaymentMethod     |  <--- Abstraction Interface
                |---------------------|
                | + process(amount)   |
                +---------------------+
                        ▲
                        │
            ┌────────┴─────────┐
            |                  |
        +---------------+  +----------------+
        |     UPI       |  |   CreditCard   |
        +---------------+  +----------------+
        | process()     |  | process()      |
        +---------------+  +----------------+

                +---------------------+
                |   PaymentGateway    |  <--- Bridge
                |---------------------|
                | - payment_method    |
                | + make_payment()    |
                +---------------------+
                        ▲
                        │
            ┌────────┴─────────┐
            |                  |
        +---------------+  +------------------+
        |   HDFCBank   |  |  SBIBank         |
        +---------------+  +------------------+
        | make_payment()|  | make_payment()   |
        +---------------+  +------------------+

        
    Steps :
        1️⃣ Step 1: Define the Interface (IPaymentMethod)
        2️⃣ Step 2: Implement Concrete Payment Methods (UPI, CreditCard, PayPal)
        3️⃣ Step 3: Define the Bridge (PaymentGateway)
        4️⃣ Step 4: Create Specialized Gateways (HDFCBank, SBIBank)
        5️⃣ Step 5: Client Code




'''



from abc import ABC, abstractmethod

# 1️⃣ Step 1: Define the Interface (IPaymentMethod)

class IPaymentMethod(ABC) :

    @abstractmethod
    def process(self, amount : float) -> None :
        """Process a payment of the given amount"""
        pass


# 2️⃣ Step 2: Implement Concrete Payment Methods (UPI, CreditCard, PayPal)

class UPI(IPaymentMethod) :
    """Concrete Implementation: UPI Payment"""

    def process(self, amount : float) :
        print(f"Processing UPI Payment of ₹{amount}")

class CreditCard(IPaymentMethod) :
    """Concrete Implementation: Credit Card Payment"""

    def process(self, amount : float) :
        print(f"Processing Credit Card Payment of ₹{amount}")

class PayPal(IPaymentMethod) :
    """Concrete Implementation: PayPal Payment"""

    def process(self, amount : float) :
        print(f"Processing PayPal Payment ₹{amount}")


# 3️⃣ Step 3: Define the Bridge (PaymentGateway)

class PaymentGateway :
    """Bridge: A Payment Gateway that delegates payment processing to a PaymentMethod"""

    def __init__(self, payment_method: IPaymentMethod) :
        self.payment_method = payment_method   # Composition: Uses a PaymentMethod
    
    def make_payment(self, amount: float) -> None :
        """Delegates payment to the selected payment method"""
        print(f"[Gateway] Initiating Payment of ₹{amount}")
        self.payment_method.process(amount)



# 4️⃣ Step 4: Create Specialized Gateways (HDFCBank, SBIBank)

class HDFCBank(PaymentGateway) :
    """Refined Abstraction: HDFC Bank Gateway"""

    def make_payment(self, amount: float) -> None :
        print("[HDFC Bank] Authenticating Transaction...")
        super().make_payment(amount)
        print("[HDFC Bank] Payment Successful!\n")


class SBIBank(PaymentGateway) :
    """Refined Abstraction: SBI Bank Gateway"""

    def make_payment(self, amount: float) -> None :
        print("[SBI Bank] Authenticating Transaction...")
        super().make_payment(amount)
        print("[SBI Bank] Payment Successful!\n")
   

# 5️⃣ Step 5: Client Code
def client_helper(Bank: PaymentGateway, payment_method: str, amount: int) :
   

    upi = UPI()
    credit_card = CreditCard()
    paypal = PayPal()
    
    if payment_method == "UPI" :
        print(f"🔹 Paying via {Bank.__name__} using UPI:")
        bank_upi = Bank(upi)
        bank_upi.make_payment(amount)

    elif payment_method == "CreditCard" :
        print(f"🔹 Paying via {Bank.__name__} using Credit Card:")
        bank_card = Bank(credit_card)
        bank_card.make_payment(amount)
    elif payment_method == "PayPal" :
        print(f"🔹 Paying via {Bank.__name__} using PayPal:")
        bank_paypal = Bank(paypal)
        bank_paypal.make_payment(amount)
    else :
        raise ValueError("Invalid Payment Method")


if __name__ == "__main__" :
    payment_gateway = input("Enter your payment gateway (HDFC / SBI) : ")
    payment_method = input("Enter payment method (UPI / CreditCard / PayPal) : ")
    amount = int(input("Enter the amount : ₹"))

    print("\n--------------------------------------------\n")

    if payment_gateway == "SBI" :
        client_helper(SBIBank, payment_method, amount)
    elif payment_gateway == "HDFC" :
        client_helper(HDFCBank, payment_method, amount)
    else :
        raise ValueError("Invalid Payment Gateway")

   