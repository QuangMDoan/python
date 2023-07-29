import matplotlib.pyplot as plt
'''
The color class creates a color from 3 values, r, g, and b(red, green, and blue).

attributes:
    r - a value between 0-255 for red
    g - a value between 0-255 for green
    b - a value between 0-255 for blue
'''

class Color(object):
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def __repr__(self):
        '''Display a color swatch and then return a text description of r, g, b values.'''

        plt.imshow([[(self.r/255, self.g/255, self.b/255)]])

        string = f"rgb = [{self.r}, {self.g}, {self.b}]"
        return string
    
    def __add__(self, other):
        '''Adds the r, g, and b components of each color together 
            and averaging them.
            The new Color object, with these averaged rgb values,
            is returned.'''
        
        new_r = (self.r + other.r) // 2
        new_g = (self.g + other.g) // 2
        new_b = int((self.b + other.b) / 2)

        new_color = Color(new_r, new_g, new_b)
        return new_color