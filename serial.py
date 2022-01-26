class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Construct serial generator starting from
        'start' value while also initializing the counter"""
        self.start = start
        self.counter = 0
    
    def __repr__(self):
        return f"Generates unique serial numbers starting with {self.start}"

    def generate(self):
        """After counting how many times 'generate'
        executed, return  addition of count and starting number"""
        self.counter += 1
        return self.start + self.counter - 1

    def reset(self):
        """Reset counter to zero"""
        self.counter = 0
        
