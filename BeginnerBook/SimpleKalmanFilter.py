# ------------------------------------------------------
#
#   SimpleKalmanFilter.py
#   By: Fred Stakem
#   Created: 4.15.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs
import numpy

# Locals
from Utilities import *

class SimpleKalmanModel(object):
    
    def __init__(self, A=1.0, H=1.0, Q=0.0, R=1.0):
        self.A = A
        self.H = H
        self.Q = Q
        self.R = R
        
    def __str__(self):  
        output = 'System model:\n'
        output += 'A: %s\n' % (str(self.A))
        output += 'H: %s\n' % (str(self.H))
        output += 'Q: %s\n' % (str(self.Q))
        output += 'R: %s\n' % (str(self.R))
        
        return output
    
    def __repr__(self):
        return str(self)

class SimpleKalmanFilter(object):
    
    # Class methods/variables
    logger = getLogger('SimpleKalmanFilter')
    
    def __init__(self, sys_model=SimpleKalmanModel(), init_x=0.0, init_p=0.0):
        self.sys_model = sys_model
        self.x = init_x
        self.x_p = 0.0
        self.P = init_p
        self.P_p = 0.0
        self.K = 0.0
        
    def __call__(self, z):
        self.calculatePrediction()
        self.calculateKalmanGain()
       
        return self.calculateEstimate(z)
    
    def __str__(self):
        output = 'SimpleKalmanFilter:\n'
        output += 'Current prediction: %s\n' % (str(self.x_p))
        output += 'Current prediction of error covariance: %s\n' % (str(self.P_p))
        output += 'Current kalman gain: %s\n' % (str(self.K))
        output += 'Current estimate: %s\n' % (str(self.x))
        output += 'Current estimate of error covariance: %s\n' % (str(self.P))
        
        return output
    
    def __repr__(self):
        return str(self)
    
    def calculatePrediction(self):
        self.x_p = self.sys_model.A * self.x 
        self.P_p = self.sys_model.A * self.P * self.sys_model.A + self.sys_model.Q
    
    def calculateKalmanGain(self):
        alpha = self.sys_model.H * self.P_p * self.sys_model.H + self.sys_model.R
        self.K = self.P_p * self.sys_model.H / alpha
    
    def calculateEstimate(self, z):
        alpha = z - self.sys_model.H * self.x_p
        self.x = self.x_p + self.K * alpha
        beta = self.K * self.sys_model.H * self.P_p
        self.P = self.P_p - beta
        
        return self.x
    
if __name__ == "__main__":
    init_x = 5.0
    init_p = 0.35
    test_data = [4.5, 4.8, 5.1, 4.75, 4.4]
    expected_estimates = [1.0, 2.9, 5.6, 9.0, 13.1]
    model = SimpleKalmanModel(A=1.0, H=1.0, Q=0.0, R=5.0)
    filter = SimpleKalmanFilter(model, init_x, init_p)
    print str(filter)
    
    for v in test_data:
        estimate = filter(v)
        print str(filter)
         

    
    
    
    