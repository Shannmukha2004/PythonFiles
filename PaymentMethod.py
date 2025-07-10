from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
class Bank(PaymentMethod):
    def make_payment(self,amount):
        print(f'Bank amount is {amount}')
a=Bank()
a.make_payment(1000)