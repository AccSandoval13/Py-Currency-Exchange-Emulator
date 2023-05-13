# To Run Type: python3 currencyExchangeEmulator.py 

# Activity: Currency Exchange Emulator (Day 4)

class Currency: # Base class

# Our class currencies is a dictionary that contains the exchange rates of other currencies 
  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def changeTo(self, new_unit): # This method changes the unit of the Currency from self.unit to new_unit and updates the value

    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit]) # This line converts the value of the Currency from self.unit to new_unit
    self.unit = new_unit # Updating the unit of the Currency to new_unit 

  def __repr__(self):
    return f"{self.value:.2f} {self.unit}" # This method returns the string to be printed, which is the value rounded to two digits, accompanied by its acronym 
  
  def __str__(self):
    return self.__repr__() # This method returns the same value as __repr__(self)
  


  def __add__(self, other): # Defines the '+' operator,  if other is a Currency object, the currency values are added and the result will be the unit of self. If other is an int or a float, other will be treated as a USD value 
    if isinstance(other, Currency): # isinstance() is a built-in function that returns True if the specified object is of the specified type, otherwise False
      if self.unit == other.unit: # If the units are the same, the values are added and the result will be the unit of self 
        return Currency(self.value + other.value, self.unit) # This line returns the value of the Currency object with the unit of self
      else:
        total_value = self.value * Currency.currencies[self.unit] + other.value * Currency.currencies[other.unit] # This line is converting the value of the Currency from self.unit to other.unit 
        return Currency(total_value, self.unit) # This returns the value of the Currency object with the unit of self
    elif isinstance(other, (int, float)): # If other is an int or a float, other will be treated as a USD value, elif is short for else if 
      total_value = self.value + other / Currency.currencies[self.unit] 
      return Currency(total_value, self.unit) # This returns the value of the Currency object with the unit of self 
    else:
      raise TypeError(f"unsupported operand type(s) for +: 'Currency' and '{type(other).__name__}'") 
      
      

  def __sub__(self, other): # All __sub__ (self, other) type functions are parallel to 
    # Defines the '-' operator. If other is a Currency object, the currency values are subtracted and the result will be the unit of self. 
    # If other is an int or a float, other will be treated as a USD value.
    if isinstance(other, Currency):
      if self.unit == other.unit:
        return Currency(self.value - other.value, self.unit)
      else:
        total_value = self.value * Currency.currencies[self.unit] - other.value * Currency.currencies[other.unit]
        return Currency(total_value, self.unit)
    elif isinstance(other, (int, float)):
      total_value = self.value - other / Currency.currencies[self.unit]
      return Currency(total_value, self.unit)
    else:
      raise TypeError(f"unsupported operand type(s) for -: 'Currency' and '{type(other).__name__}'")
                
      

v1 = Currency(1.43, "EUR") # 
v2 = Currency(2.33, "USD")

print(v1 + v2) # This line prints the value of v1 + v2 
print(v2 + v1) # This line prints the value of v2 + v1 
print(v1 + 3) # 3 is treated as a USD value, so the result is in EUR  
print(v2 - 3) # 3 is treated as a USD value, so the result is in USD 
print(v1 + 7) # an int or a float is considered to be a USD value
print(v1 - v2) # This line prints the value of v1 - v2 

