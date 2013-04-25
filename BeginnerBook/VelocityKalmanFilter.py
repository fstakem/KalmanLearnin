# ------------------------------------------------------
#
#   VelocityKalmanFilter.py
#   By: Fred Stakem
#   Created: 4.24.13
#
# ------------------------------------------------------

# The following code is an adaptation from the book
# "Kalman Filter for Beginners with MATLAB Examples"
# By Phil Kim.

# Libs
import numpy

# Locals
from Utilities import *

class VelocityKalmanModel(object):
    
    def __init__(self, A=numpy.array([ [0.0, 0.0], [0.0, 0.0] ]), 
                       H=numpy.array([ [0.0, 0.0] ]), 
                       Q=numpy.array([ [0.0, 0.0], [0.0, 0.0] ]), 
                       R=1):
        self.A = A
        self.H = H
        self.Q = Q
        self.R = R
        
    def __str__(self):  
        output = 'System model:\n'
        output += 'A: %s\n' % (str(self.A.tolist()))
        output += 'H: %s\n' % (str(self.H.tolist()))
        output += 'Q: %s\n' % (str(self.Q.tolist()))
        output += 'R: %s\n' % (str(self.R))
        
        return output
    
    def __repr__(self):
        return str(self)

class VelocityKalmanFilter(object):
    
    # Class methods/variables
    logger = getLogger('VelocityKalmanFilter')
    
    def __init__(self, sys_model=VelocityKalmanModel(), init_x=numpy.array([ [0.0], [0.0] ]), 
                       init_p=numpy.array([ [0.0, 0.0], [0.0, 0.0] ])):
        self.sys_model = sys_model
        self.x = init_x
        self.x_p = numpy.array([ [0.0], [0.0] ])
        self.P = init_p
        self.P_p = numpy.array([ [0.0, 0.0], [0.0, 0.0] ])
        self.K = numpy.array([0.0, 0.0])
        
    def __call__(self, z):
        self.calculatePrediction()
        self.calculateKalmanGain()
       
        return self.calculateEstimate(z)
    
    def __str__(self):
        output = 'SimpleKalmanFilter:\n'
        output += 'Current prediction: %s\n' % (str(self.x_p.tolist()))
        output += 'Current prediction of error covariance: %s\n' % (str(self.P_p.tolist()))
        output += 'Current kalman gain: %s\n' % (str(self.K.tolist()))
        output += 'Current estimate: %s\n' % (str(self.x.tolist()))
        output += 'Current estimate of error covariance: %s\n' % (str(self.P.tolist()))
        
        return output
    
    def __repr__(self):
        return str(self)
    
    def calculatePrediction(self):
        self.x_p = self.sys_model.A.dot(self.x) 
        self.P_p = self.sys_model.A.dot(self.P).dot(self.sys_model.A.transpose()) + self.sys_model.Q
        
    def calculateKalmanGain(self):
        alpha = self.sys_model.H.dot(self.P_p).dot( self.sys_model.H.transpose() ) + self.sys_model.R
        self.K = ( self.P_p.dot( self.sys_model.H.transpose() ) ) / alpha
    
    def calculateEstimate(self, z):
        alpha = z - self.sys_model.H.dot(self.x_p)
        self.x = self.x_p + self.K.dot(alpha)
        beta = self.K * self.sys_model.H.dot(self.P_p)
        self.P = self.P_p - beta
        
        return self.x
    
if __name__ == "__main__":
    test_data = [ numpy.array([ [0.0], [20.0] ]),
                  numpy.array([ [0.0], [21.0] ]),
                  numpy.array([ [0.0], [22.0] ]),
                  numpy.array([ [0.0], [23.0] ]),
                  numpy.array([ [0.0], [22.0] ]),
                  numpy.array([ [0.0], [21.0] ]),
                  numpy.array([ [0.0], [20.0] ]),
                  numpy.array([ [0.0], [22.0] ]) ]
    
    # Setup the model
    a = numpy.array([ [1.0, 0.1], [0.0, 1.0] ])
    h = numpy.array([1.0, 0.0])
    q = numpy.array([ [1.0, 0.0], [0.0, 3.0] ])
    r = 10
    model = VelocityKalmanModel(A=a, H=h, Q=q, R=r)
    
    # Setup the filter
    init_x = numpy.array([ [0.0], [20.0]])
    init_p = numpy.array([ [5.0, 0.0], [0.0, 5.0] ])
    filter = VelocityKalmanFilter(model, init_x, init_p)
    print str(filter)
    
    for v in test_data:
        estimate = filter(v)
        print str(filter)
         

    
    
    
    