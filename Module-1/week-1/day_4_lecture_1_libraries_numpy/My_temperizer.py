"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c

def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = temperature_c*(9/5)+32
    return temperature_f

def convert_c_to_k(temperature_c):
    """Convert Celsius to Kelvin."""
    temperature_k = temperature_c+273.15
    return temperature_k
    
def convert_k_to_c(temperature_k):
    """Convert to Kelvin to Celcius."""
    temperature_c =  temperature_k - 273.15
    return temperature_c  
    
def convert_f_to_k(temperature_f):
    """Convert Fahrenheit to Kelvin."""
    temperature_k = convert_f_to_c(temperature_f) +273.15
    return temperature_k
    
def convert_k_to_f(temperature_k):
    """Convert Fahrenheit to Kelvin."""
    temperature_f = convert_k_to_c(temperature_k)*(9/5)+32
    return temperature_f

def convert_f_to_all(temperature_f)

 