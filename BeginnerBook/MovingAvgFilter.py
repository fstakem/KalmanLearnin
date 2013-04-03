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
from Utilities import *
from collections import deque

class MovingAvgFilter(object):
    
    # Class methods/variables
    logger = getLogger('MovingAverageFilter')
    
    def __init__(self, filter_length=10, init_values=[]):
        self.previous_mean = 0
        self.filter_length = filter_length
        buffer_data = [0] * self.filter_length
        self.sample_buffer = deque(buffer_data)
        
        for x in init_values:
            self.calculateNextMean(x)
    
    def __call__(self, x):
        return self.calculateNextMean(x)
    
    def __str__(self):
        return 'MovingAvgFilter Previous mean: %f Filter buffer: %s' % (self.previous_mean, str(self.sample_buffer))
    
    def __repr__(self):
        return str(self)
         
    def calculateNextMean(self, x):
        last_x_in_buffer = self.sample_buffer.pop()
        self.sample_buffer.appendleft(x)
        mean = self.previous_mean + (x - last_x_in_buffer) / self.filter_length
        
        self.previous_mean = mean
        
        return mean
    
    
    
    