# ------------------------------------------------------
#
#   TestChapter1.py
#   By: Fred Stakem
#   Created: 3.25.13
#
# ------------------------------------------------------

# Libs
import unittest
import Globals
from Utilities import *

class Chapter1Test(unittest.TestCase):
    
    # Setup logging
    logger = getLogger('Chapter1Test')
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testAvgFilter(self):
        pass
    
    @log_test(logger, globals.log_separator)
    def testAvgFilterGraphically(self):
        pass