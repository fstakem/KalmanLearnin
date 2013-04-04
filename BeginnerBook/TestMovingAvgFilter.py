# ------------------------------------------------------
#
#   TestMovingAvgFilter.py
#   By: Fred Stakem
#   Created: 4.2.13
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
from MovingAvgFilter import MovingAvgFilter

class MovingAvgFilterTest(unittest.TestCase):
    
    # Setup logging
    logger = getLogger('MovingAvgFilterTest')
    graph_file = '../output/MovingAvgFilter.png'
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilterInit(self):
        init_data = [10, 20, 30, 40, 50]
        expected_mean = 35
        filter_length = 4
        
        filter = MovingAvgFilter(filter_length, init_data)
        mean = filter.previous_mean
        
        output = 'Initial data: %s Expected mean: %s Actual mean: %s' % (str(init_data), str(expected_mean), str(mean))
        MovingAvgFilterTest.logger.debug(output)
        assert mean == expected_mean, 'MovingAvgFilter class was incorrectly initialized.'
     
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilter(self):
        test_data = [10, 20, 30, 40, 50]
        expected_means = [1, 3, 6, 10, 15]
        filter = MovingAvgFilter()
        
        MovingAvgFilterTest.logger.debug('Initial mean: %f' % (filter.previous_mean))
        for i, x in enumerate(test_data):
            mean = filter(x)
            output = 'Additional data: %s Expected mean: %s Actual mean: %s' % (str(x), str(expected_means[i]), str(mean))
            MovingAvgFilterTest.logger.debug(output)
            assert mean == expected_means[i], 'MovingAvgFilter class filtered incorrectly.'
        
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilterGraphically(self):
        test_data = self.generateSignal(6, 0.1)
        time = range(0, len(test_data) * 10, 10)
        filtered_data = []
        filter = MovingAvgFilter()
        
        for x in test_data:
            filtered_data.append( filter(x) )
            
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(time, test_data, 'o-')
        subplot.plot(time, filtered_data, 'ko-')
        subplot.set_xlabel('Time (s)')
        subplot.set_ylabel('Voltage (V)')
        subplot.set_title('AvgFilterTest: Voltage vs Time')
        
        plt.savefig(MovingAvgFilterTest.graph_file)
    
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
        
    
    
    