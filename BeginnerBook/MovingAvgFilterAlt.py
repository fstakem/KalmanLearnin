# ------------------------------------------------------
#
#   MovingAvgFilterAlt.py
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

class MovingAvgFilterAlt(object):
    
    # Class methods/variables
    logger = getLogger('MovingAverageFilterAlt')
    
    def __init__(self, filter_length=10, init_values=[]):
        self.filter_length = filter_length
        buffer_data = [0] * self.filter_length
        self.sample_buffer = deque(buffer_data)
        
        for x in init_values:
            self.addSampleToBuffer(x)
    
    def __call__(self, x):
        return self.calculateNextMean(x)
    
    def __str__(self):
        mean = self.calculateMean()
        return 'MovingAvgFilter Previous Mean: %f Filter buffer: %s' % (mean, str(self.sample_buffer))
    
    def __repr__(self):
        return str(self)
         
    def calculateNextMean(self, x):
        self.addSampleToBuffer(x)
        return self.calculateMean()
    
    def addSampleToBuffer(self, x):
        self.sample_buffer.pop()
        self.sample_buffer.appendleft(x)
    
    def calculateMean(self):
        return sum(self.sample_buffer) / self.filter_length
        
    