# ------------------------------------------------------
#
#   LowPassFilter.py
#   By: Fred Stakem
#   Created: 4.5.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs

# Locals
from Utilities import *
from collections import deque

class LowPassFilter(object):
    
    # Class methods/variables
    logger = getLogger('LowPassFilter')
    
    def __init__(self, alpha=10, init_values=[]):
        self.previous_estimate = 0
        self.alpha = alpha
        
        for x in init_values:
            self.calculateNextEstimate(x)
        
    def __call__(self, x):
        return self.calculateNextEstimate(x)
    
    def __str__(self):
        return 'LowPassFilter Previous estimate: %f Alpha: %s' % (str(self.previous_estimate), str(self.alpha))
    
    def __repr__(self):
        return str(self)
         
    def calculateNextEstimate(self, x):
        self.previous_estimate = self.alpha * self.previous_estimate + (1 - self.alpha) * x
    
        return self.previous_estimate
    
    
    
    