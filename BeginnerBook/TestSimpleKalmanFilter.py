# ------------------------------------------------------
#
#   TestSimpleKalmanFilter.py
#   By: Fred Stakem
#   Created: 4.15.13
#
# ------------------------------------------------------

# Libs
import unittest
import random
import matplotlib.pyplot as plt
import math
import numpy
import Globals as globals
from Utilities import *
from SimpleKalmanFilter import SimpleKalmanModel
from SimpleKalmanFilter import SimpleKalmanFilter

class SimpleKalmanFilterTest(unittest.TestCase):
    
    # Setup logging
    logger = getLogger('SimpleKalmanFilterTest')
    single_filter_graph_file = '../output/SimpleKalmanFilterSingle.png'
    multiple_filter_graph_file = '../output/SimpleKalmanFilterDouble.png'
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    @log_test(logger, globals.log_separator)
    def testFilter(self):
        init_x = 5.0
        init_p = 0.35
        test_data = [4.5, 4.8, 5.1, 4.75, 4.4]
        expected_estimates = [4.96, 4.95, 4.96, 4.95, 4.92]
        model = SimpleKalmanModel(A=1.0, H=1.0, Q=0.0, R=5.0)
        filter = SimpleKalmanFilter(model, init_x, init_p)
        
        SimpleKalmanFilterTest.logger.debug('Initial filter:\n%s' % (filter))
        for i, x in enumerate(test_data):
            estimate = filter(x)
            output = 'Additional data: %s Expected estimate: %s Actual estimate: %s' % (str(x), str(expected_estimates[i]), str(estimate))
            SimpleKalmanFilterTest.logger.debug(output)
            assert numpy.allclose([estimate], [expected_estimates[i]], 0.1) , 'SimpleKalmanFilter class filtered incorrectly.'
        
    @log_test(logger, globals.log_separator)
    def testFilterOneCurveCurveGraphically(self):
        test_data = self.generateSignal(5, 100)
        time = range(0, 100, 1)
        filtered_data = []
        init_x = 5.0
        init_p = 0.35
        model = SimpleKalmanModel(A=1.0, H=1.0, Q=0.0, R=5.0)
        filter = SimpleKalmanFilter(model, init_x, init_p)
        
        for x in test_data:
            filtered_data.append( filter(x) )
            
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(time, test_data, 'o-')
        subplot.plot(time, filtered_data, 'ko-')
        subplot.set_xlabel('Time (s)')
        subplot.set_ylabel('Voltage (V)')
        subplot.set_title('SimpleKalmanFilterTest: Voltage vs Time')
        
        plt.savefig(SimpleKalmanFilterTest.single_filter_graph_file)
        
    @log_test(logger, globals.log_separator)
    def testFilterTwoCurvesGraphically(self):
        test_data = self.generateSignal(5, 100)
        time = range(0, 100, 1)
        filtered_data_a = []
        init_x = 5.0
        init_p = 0.35
        model = SimpleKalmanModel(A=1.0, H=1.0, Q=0.0, R=5.0)
        filter_a = SimpleKalmanFilter(model, init_x, init_p)
    
        filtered_data_b = []
        init_x = 5.5
        init_p = 0.35
        model = SimpleKalmanModel(A=1.0, H=1.0, Q=0.0, R=6.0)
        filter_b = SimpleKalmanFilter(model, init_x, init_p)
        
        for x in test_data:
            filtered_data_a.append( filter_a(x) )
            filtered_data_b.append( filter_b(x) )
            
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(time, test_data, 'o-')
        subplot.plot(time, filtered_data_a, 'ko-')
        subplot.plot(time, filtered_data_b, 'go-')
        subplot.set_xlabel('Time (s)')
        subplot.set_ylabel('Voltage (V)')
        subplot.set_title('LowPassFilterTest: Voltage vs Time')
        
        plt.savefig(SimpleKalmanFilterTest.multiple_filter_graph_file)
    
    def generateSignal(self, value, num_samples):
        variation = value * 0.1
        signal = [value] * num_samples
        
        y = []
        for i in signal:
            signal_n_noise = random.uniform(value + variation, value - variation)
            y.append(signal_n_noise)
                          
        return y
        
    
    
    