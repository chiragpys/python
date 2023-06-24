
class calculator():
    
    def __init__(self,*args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.history = []
        
        
    def add(self):
        return sum(self.args)
    
    def sub(self):
        subtrc = self.args[0]
        for i in self.args[1:]:
            subtrc -= i
        return subtrc
    
    def mul(self):
        product = 1
        for a in self.args:
            product *= a
        return product
    
    def div(self):
        division = self.args[0]
        for i in self.args[1:]:
            division /= i
        return division
    

class LengthConverter:
    CONVERSION_FACTORS = {
        'km': 1000,
        'm': 1,
        'mm': 0.001,
        'cm': 0.01,
    }

    def __init__(self, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        
    def convert(self):
        if self.from_unit not in self.CONVERSION_FACTORS or self.to_unit not in self.CONVERSION_FACTORS:
            return None
        
        meters = self.value * self.CONVERSION_FACTORS[self.from_unit]
        converted_value = meters / self.CONVERSION_FACTORS[self.to_unit]
        
        return converted_value

