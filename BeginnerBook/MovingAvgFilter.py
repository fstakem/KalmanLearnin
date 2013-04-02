# ------------------------------------------------------
#
#   MovingAvgFilter.py
#   By: Fred Stakem
#   Created: 4.1.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs

# Locals
import Utilities
from collections import deque

class MovingAvgFilter(object):
    
    # Class methods/variables
    Utilities.getLogger('MovingAverageFilter')
    
    def __init__(self, filter_length=10, init_values=[]):
        self.previous_mean = 0
        self.filter_length = filter_length
        buffer_data = [0] * self.filter_length
        self.sample_buffer = deque(buffer_data)
        
        if len(init_values) > 0:
            for x in init_values:
                self.calculateNextMean(x)
    
    def __call__(self, x, reset=False, filter_length=10):
        if reset:
            self.reset(filter_length)
            
        return self.calculateNextMean(x)
    
    def __str__(self):
        pass
    
    def reset(self, filter_length):
        self.previous_mean = 0
        self.filter_length = filter_length
        buffer_data = [0] * self.filter_length
        self.sample_buffer = deque(buffer_data)
        
    def calculateNextMean(self, x):
        pass
    
    
    
    