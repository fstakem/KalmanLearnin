# ------------------------------------------------------
#
#   Utilities.py
#   By: Fred Stakem
#   Created: 3.25.13
#
# ------------------------------------------------------

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


# Libraries
import logging

def getLogger(name='GenericLogger'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(name)s Line: %(lineno)d |  %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def log_test(logger, log_seperators):
    def log(func):
        def onCall(self):
            output = log_seperators[0]
            output += ' START ' + func.func_name + '() '
            output += log_seperators[0]
            logger.debug(output)

            func(self)
            
            output = log_seperators[0]
            output += ' FINISHED ' + func.func_name + '() '
            output += log_seperators[1]
            logger.debug(output)
            logger.debug('')
        return onCall
    return log

def debug_log(logger, debug_on=False):
    def debug(func):
        def onCall(self):
            if debug_on:
                logger.debug('Before %s()' % (func.func_name))
                lines = ( str(self) ).split('\n')
                for line in lines:
                    logger.debug('\t%s' % (line))
                
            data = func(self)
            
            if debug_on:
                logger.debug('After %s()' % (func.func_name))
                lines = ( str(self) ).split('\n')
                for line in lines:
                    logger.debug('\t%s' % (line))
                    
            return data
        return onCall
    return debug

def readLinesFromFile(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    
    return lines
