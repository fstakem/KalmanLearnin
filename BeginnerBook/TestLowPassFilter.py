# ------------------------------------------------------
#
#   TestLowPassFilter.py
#   By: Fred Stakem
#   Created: 4.8.13
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
from LowPassFilter import LowPassFilter

class LowPassFilterTest(unittest.TestCase):
    
    # Setup logging
    logger = getLogger('MovingAvgFilterAltTest')
    single_filter_graph_file = '../output/LowPassFilterSingle.png'
    multiple_filter_graph_file = '../output/LowPassFilterDouble.png'
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    @log_test(logger, globals.log_separator)
    def testFilterInit(self):
        init_data = [10, 20, 30, 40, 50]
        expected_estimate = 13.1
        alpha = 0.9
        
        filter = LowPassFilter(alpha, init_data)
        estimate = filter.previous_estimate
        
        output = 'Initial data: %s Expected estimate: %s Actual estimate: %s' % (str(init_data), str(expected_estimate), str(estimate))
        LowPassFilterTest.logger.debug(output)
        assert numpy.allclose([estimate], [expected_estimate], 0.1) , 'LowPassFilter class was incorrectly initialized.'
     
    @log_test(logger, globals.log_separator)
    def testFilter(self):
        test_data = [10, 20, 30, 40, 50]
        expected_estimates = [1.0, 2.9, 5.6, 9.0, 13.1]
        alpha = 0.9
        filter = LowPassFilter(alpha)
        
        LowPassFilterTest.logger.debug('Initial estimate: %f' % (filter.previous_estimate))
        for i, x in enumerate(test_data):
            estimate = filter(x)
            output = 'Additional data: %s Expected estimate: %s Actual estimate: %s' % (str(x), str(expected_estimates[i]), str(estimate))
            LowPassFilterTest.logger.debug(output)
            assert numpy.allclose([estimate], [expected_estimates[i]], 0.1) , 'LowPassFilter class filtered incorrectly.'
        
    @log_test(logger, globals.log_separator)
    def testFilterOneCurveCurveGraphically(self):
        test_data = self.generateSignal(6, 0.1)
        time = range(0, len(test_data) * 10, 10)
        filtered_data = []
        alpha = 0.8
        filter = LowPassFilter(alpha)
        
        for x in test_data:
            filtered_data.append( filter(x) )
            
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(time, test_data, 'o-')
        subplot.plot(time, filtered_data, 'ko-')
        subplot.set_xlabel('Time (s)')
        subplot.set_ylabel('Voltage (V)')
        subplot.set_title('LowPassFilterTest: Voltage vs Time')
        
        plt.savefig(LowPassFilterTest.single_filter_graph_file)
        
    @log_test(logger, globals.log_separator)
    def testFilterTwoCurvesGraphically(self):
        test_data = self.generateSignal(6, 0.1)
        time = range(0, len(test_data) * 10, 10)
        alpha_a = 0.9
        filtered_data_a = []
        filter_a = LowPassFilter(alpha_a)
        alpha_b = 0.6
        filtered_data_b = []
        filter_b = LowPassFilter(alpha_b)
        
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
        
        plt.savefig(LowPassFilterTest.multiple_filter_graph_file)
    
    def generateSignal(self, max_value, step):
        x = numpy.arange(0, max_value, step)
        y = []
        
        signal = []
        for i in x:
            signal.append(math.sin(i)**2 / 100)
            
        max_num = max(signal)
        min_num = min(signal)
        diff = max_num - min_num
        
        for i in signal:
            noise = random.uniform(-diff/2, diff/2)
            y.append(i + noise / 10 )
                    
        return y
        
    
    
    