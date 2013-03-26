# ------------------------------------------------------
#
#   Chapter1.py
#   By: Fred Stakem
#   Created: 3.25.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs

# Locals
import Utilities

# Setup
Utilities.getLogger('Chapter_1')

# Data structures

# Functions
def avgFilter(x, reset=False):
    if not hasattr(avgFilter, 'previous_mean') or reset:
        avgFilter.previous_mean = 0
        avgFilter.num_samples = 0
    
    try:
        avgFilter.num_samples += 1
        alpha = (avgFilter.num_samples - 1) / avgFilter.num_samples
        average = alpha * avgFilter.previous_mean + (1 - alpha) * x
    except Exception as e:
        avgFilter.num_samples -= 1
        raise e
    
    avgFilter.previous_mean = average
    
    return average
    
    



