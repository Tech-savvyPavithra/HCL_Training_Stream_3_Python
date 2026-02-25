from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    def refund(self, amount):
        pass
    
class creditcard(PaymentGateway):
    def pay(self, amount):
        print(f"Processing credit card payment of Rs: {amount}")
    def refund(self, amount):
        print(f"Refunding credit card payment of Rs: {amount}")
        
class upipayment(PaymentGateway):
    def pay(self, amount):
        print(f"Processing UPI payment of Rs: {amount}")
    def refund(self, amount):
        print(f"Refunding UPI payment of Rs: {amount}") 
        
c=creditcard()
c.pay(1000)
c.refund(500)

u=upipayment()
u.pay(2000)
u.refund(1000)
