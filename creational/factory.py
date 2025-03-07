'''
    Imagine we are building a notification system that supports:

    Email notifications
    SMS notifications
    Push notifications

    Instead of hardcoding which class to use, we will use a Factory Method.


'''

# Define an interface Notification


from abc import ABC, abstractmethod

# Abstract product (Interface)
class Notification(ABC):

    @abstractmethod
    def notify(self, message : str):
        pass

# Concrete Product 1
class EmailNotification(Notification):

    def notify(self, message: str):
        print(f"📧 Sending Email: {message}")

# Concrete Product 2
class SMSNotification(Notification):

    def notify(self, message: str):
        print(f"📱 Sending SMS: {message}")

# Concrete Product 3
class PushNotification(Notification):
    
    def notify(self, message: str):
        print(f"📲 Sending Push Notification: {message}")


# Factory Class

'''
    # Here used simpliest way to design factory but we are violeting open-closed principle ----> So that we need to make it abstract as well so that (Adding a new notification type means only adding a new factory class—no need to modify existing code.) 

    class NotificationFactory:

        @staticmethod
        def create_notification(notification_type: str) -> Notification :
            if notification_type == "email" :
                return EmailNotification()
            elif notification_type == "sms" :
                return SMSNotification()
            elif notification_type == "push" :
                return PushNotification()
            else :
                raise ValueError("Invalid notification type")
        
'''


# Creator (Abstract Factory)
class NotificationFactory(ABC):
    
    @abstractmethod
    def create_notification(self) -> Notification :
        pass

    def send_notification(self, message: str):
        notification = self.create_notification()
        notification.notify(message)

# Concrete Creator 1
class SMSNotificationFactory(NotificationFactory) :
    
    def create_notification(self) -> Notification:
        return SMSNotification()

# Concrete Creator 2
class EmailNotificationFactory(NotificationFactory) :

    def create_notification(self) -> Notification :
        return EmailNotification()

# Concrete Creator 3    
class PushNotificationFactory(NotificationFactory) :

    def create_notification(self) -> Notification :
        return PushNotification()
    


def get_notification_factory(notification_type: str) -> NotificationFactory :

    if notification_type == "email" :
        return EmailNotification()
    elif notification_type == "sms" :
        return SMSNotification()
    elif notification_type == "push" :
        return PushNotification()
    else :
        raise ValueError("Invalid notification type")


if __name__ == "__main__" :
    notification_type = input("Enter notification type (email/sms/push): ").strip().lower()

    try :
        # notification = NotificationFactory.create_notification(notification_type)
        notification = get_notification_factory(notification_type)
        notification.notify("Hello this is your notification")
    except Exception as e :
        print(f"Error : {e}")
        
