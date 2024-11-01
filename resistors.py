""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 2024Test 1
Tomasz Giedrojc
100793058

"""
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)

# Define the VariableResistor class
class VariableResistor(Resistor):
    """Model a variable resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance and initializes actual resistance."""
        super().__init__(res)
        self.actual_resistance = res  # Start with actual resistance equal to fixed resistance

    def set_resistance(self, percent):
        """Set actual resistance as a percentage of the fixed resistance."""
        if 0 <= percent <= 100:
            self.actual_resistance = (percent / 100) * self.resistance
        else:
            raise ValueError("Percentage must be between 0 and 100.")

    def current(self, voltage):
        """Calculate current using the actual resistance."""
        if self.actual_resistance == 0:
            raise ValueError("Actual resistance is zero; current is undefined.")
        return voltage / self.actual_resistance

    def __str__(self):
        """Return a string representation of the variable resistor."""
        return "Variable Resistor, R=" + str(self.resistance) + ", Actual R=" + str(self.actual_resistance)

# Main Program for Testing
if __name__ == "__main__":
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    # Uncommented block to test VariableResistor
    r2 = VariableResistor(1000.0)
    print("R2:", r2)
    print("R2 100%: voltage=12.0, current=", r2.current(12.0))
    r2.set_resistance(50.0)
    print("R2 50%: voltage=12.0, current=", r2.current(12.0))
