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
import Utilities
from collections import deque

class MovingAvgFilterAlt(object):
    
    # Class methods/variables
    Utilities.getLogger('MovingAverageFilterAlt')