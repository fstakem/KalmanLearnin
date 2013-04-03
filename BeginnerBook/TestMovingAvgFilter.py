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
import Globals as globals
from Utilities import *
from MovingAvgFilter import MovingAvgFilter

class MovingAvgFilterTest(unittest.TestCase):
    
    # Setup logging
    logger = getLogger('MovingAvgFilterTest')
    #graph_file = '../output/RandomAvgFilter.png'
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
        
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilterInit(self):
        init_data = [10, 20, 30, 40, 50]
        expected_mean = 18
        filter_length = 8
        
        filter = MovingAvgFilter(filter_length, init_data)
        mean = filter.previous_mean
        
        output = 'Initial data: %s Expected mean: %s Actual mean: %s' % (str(init_data), str(expected_mean), str(mean))
        MovingAvgFilterTest.logger.debug(output)
        assert mean == expected_mean, 'MovingAvgFilter class was incorrectly initialized.'
     
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilter(self):
        test_data = [10, 20, 30, 40, 50]
        expected_means = [10, 15, 20, 25, 30]
        filter = AvgFilter()
        
        AvgFilterTest.logger.debug('Initial mean: %f' % (filter.previous_mean))
        for i, x in enumerate(test_data):
            mean = filter(x)
            output = 'Additional data: %s Expected mean: %s Actual mean: %s' % (str(x), str(expected_means[i]), str(mean))
            AvgFilterTest.logger.debug(output)
            assert mean == expected_means[i], 'AvgFilter class filtered incorrectly.'
        
    @log_test(logger, globals.log_separator)
    def testMovingAvgFilterGraphically(self):
        test_data = self.generateRandomSignal(50)
        time = range(0, len(test_data) * 10, 10)
        filtered_data = []
        filter = AvgFilter()
        
        for x in test_data:
            filtered_data.append( filter(x) )
            
        fig = plt.figure()
        subplot = fig.add_subplot(111)
        subplot.plot(time, test_data, 'o-')
        subplot.plot(time, filtered_data, 'ko-')
        subplot.set_xlabel('Time (s)')
        subplot.set_ylabel('Voltage (V)')
        subplot.set_title('AvgFilterTest: Voltage vs Time')
        
        plt.savefig(AvgFilterTest.graph_file)
    
    def generateRandomSignal(self, size):
        x = []
        
        for y in range(size):
            x.append( random.uniform(10, 20) )
            
        return x
        
    
    
    