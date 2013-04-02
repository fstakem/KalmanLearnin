# ------------------------------------------------------
#
#   AvgFilter.py
#   By: Fred Stakem
#   Created: 3.28.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs

# Locals
import Utilities

class AvgFilter(object):
    
    # Class methods/variables
    Utilities.getLogger('AverageFilter')
    
    def __init__(self, init_values=[]):
        self.previous_mean = 0
        self.num_samples = 0
        
        if len(init_values) > 0:
            for x in init_values:
                self.calculateNextMean(x)
    
    def __call__(self, x, reset=False):
        if reset:
            self.reset()
        
        return self.calculateNextMean(x)
    
    def __str__(self):
        return 'AvgFilter Previous mean: %f Number of samples: %d' % (self.previous_mean, self.num_samples)
    
    def reset(self):
        self.previous_mean = 0
        self.num_samples = 0
    
    def calculateNextMean(self, x):
        new_num_samples = self.num_samples + 1
        alpha = (new_num_samples - 1) / float(new_num_samples)
        average = alpha * self.previous_mean + (1 - alpha) * x
        
        self.num_samples = new_num_samples
        self.previous_mean = average
        
        return average
    
    
    

