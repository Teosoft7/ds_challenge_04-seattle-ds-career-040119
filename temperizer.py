"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = temperature_c * (9/5) + 32
    return temperature_f

    """
    # To Do
    * `convert_c_to_k`
    * `convert_f_to_k`
    * `convert_k_to_c`
    * `convert_k_to_f`
    """
def convert_c_to_k(temperature_c):
    """Convert Celsius to Kevin."""
    # 0°C + 273.15 = 273.15K
    temperature_k = temperature_c + 273.15
    return temperature_k

def convert_f_to_k(temperature_f):
    """Convert Celsius to Fahrenheit."""
    temperature_k = convert_c_to_k(convert_f_to_c(temperature_f))
    return temperature_k

def convert_k_to_c(temperature_k):
    """Convert Kevin to Celsius."""
    temperature_c = temperature_k - 273.15
    return temperature_c

def convert_k_to_f(temperature_k):
    temperatute_f = convert_c_to_f(convert_k_to_c(temperature_k))
    return temperatute_f
