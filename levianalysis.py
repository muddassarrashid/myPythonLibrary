import numpy as np

def getConversionFactor(qm,Z0,omega0,g):

    '''
    Converts the gradient obtained from calibration fitting to
    give eta the conversion factor.
    '''

    return (1/qm)*omega0^2*Z0*g
