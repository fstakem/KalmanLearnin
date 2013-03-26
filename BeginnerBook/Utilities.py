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