from abc import ABC, abstractmethod

class Converter(ABC):
    
    @abstractmethod
    def convert(self, from_currency, to_currency, amount):
        ...

class FXConverter(Converter):

    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2},{to_currency}')
        return amount * 1.2

class CCXConverter(Converter):

    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 2.2},{to_currency}')
        return amount * 2.2
    

class App:
    
    def __init__(self, converter:Converter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)

if __name__ == '__main__':
    app = App(FXConverter())
    app.start()

