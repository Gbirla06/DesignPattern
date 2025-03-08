'''

    Imagine you're building a notification system where users can receive messages via Email, SMS, or Push Notifications.

    Instead of creating separate classes for each combination, we use the Decorator Pattern to add notification methods dynamically.

----------------------------------------------------------------------------------------------------------------------------------------------
    
    UML Diagram

         ┌───────────────────────┐
         │   Notifier (Interface)│   <--- Abstract Component
         │   + send(msg)         │
         └───────────┬───────────┘
                     │
         ┌───────────┴───────────┐
         │    BasicNotifier      │   <--- Concrete Component
         │    (Base Notification)│
         └───────────┬───────────┘
                     │
         ┌───────────┴───────────┐
         │   NotifierDecorator   │   <--- Abstract Decorator
         │   + send(msg)         │
         └───────────┬───────────┘
                     │
 ┌───────────────────┴───────────────────┐
 │                 │                     │
 │      EmailNotifier                    │
 │      + send(msg)                      │
 │                                       │
 │                 SMSNotifier           │
 │                 + send(msg)           │
 │                                       │
 │                 PushNotifier          │
 │                 + send(msg)           │
 └───────────────────────────────────────┘

----------------------------------------------------------------------------------------------------------------------------------------------

    Steps :
        Step 1: Create Abstract Component (Notifier)
        Step 2: Create Concrete Component (BasicNotifier)
        Step 3: Create Abstract Decorator (NotifierDecorator)
        Step 4: Create Concrete Decorators (EmailNotifier, SMSNotifier, PushNotifier)
'''


from abc import ABC, abstractmethod

# Step 1: Create Abstract Component (Notifier)

class Notifier(ABC) :

    @abstractmethod
    def send(self, message: str) :
        pass


# Step 2: Create Concrete Component (BasicNotifier)

class BasicNotifier(Notifier) :

    def send(self, message: str) :
        print(f"Basic Notificatio: {message}")



# Step 3: Create Abstract Decorator (NotifierDecorator)

class NotificationDecorator(Notifier, ABC) :

    def __init__(self, notifier : Notifier) :
        self.notifier = notifier
    
    def send(self, message: str) :
        self.notifier.send(message)



# Step 4: Create Concrete Decorators (EmailNotifier, SMSNotifier, PushNotifier)

class EmailNotifier(NotificationDecorator) :
    
    def send(self, message) :
        super().send(message)
        print(f"📧 Sending Email: {message}")

class SMSNotifier(NotificationDecorator) :

    def send(self, message) :
        super().send(message)
        print(f"📱 Sending SMS: {message}")

class PushNotifier(NotificationDecorator) :
    
    def send(self, message) :
        super().send(message)
        print(f"🔔 Sending Push Notification: {message}")



if __name__ == "__main__" :
    
    # Basic Notification
    notifier = BasicNotifier()
    print("\n📢 Only Basic Notification:")
    notifier.send("Hello, User !!")

    # Add Email Notification
    email_notifier = EmailNotifier(notifier)
    print("\n📢 Basic + Email Notification:")
    email_notifier.send("Hello, User !!")

    # Add SMS Notification on top of Email
    sms_email_notifier = SMSNotifier(email_notifier)
    print("\n📢 Basic + Email + SMS Notification:")
    sms_email_notifier.send("Hello, User !!")

    # Add Push Notification on top of Email + SMS
    full_notifier = PushNotifier(sms_email_notifier)
    print("\n📢 Basic + Email + SMS + Push Notification:")
    full_notifier.send("Hello, User!")