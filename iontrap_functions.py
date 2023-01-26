#!/usr/bin/env python

# Importing Libraries
import pandas as pd
import numpy as np
from sympy import *

def SolveForQM():
    # Declaring the symbolic variables
    a, b, c, x = symbols('a, b, c, x',real=True)

    # Defining the equation that needs to be solved
    eqn = a*x**2 + b*x - c;

    # creater the solver
    xSol = solveset(eqn,x)

    return xSol

def genAngularFreqs(reftable):
    # The Driving frequency in radians
    wD = 2*np.pi*reftable.Freq_RF

    # The secular frequencies in radians
    w0 = 2*np.pi*(pd.concat([reftable.fx,reftable.fy,reftable.fz],ignore_index=True))

    return wD, w0

def defineCoefficients(reftable, simpara):

    wD, w0 = genAngularFreqs(reftable)
    # determining the coefficients to the quadratic equation
    aa = (simpara.alpha**2)*((reftable.V0**2)/(2*wD**2*reftable.R**4)).values
    bb = (simpara.beta)*((2*reftable.U0)/(reftable.Z0**2)).values
    cc = w0**2

    return aa, bb, cc

def getQM(reftable,simpara):
    a, b, c, x = symbols('a, b, c, x',real=True)

    xSol = SolveForQM()
    aa, bb, cc  = defineCoefficients(reftable,simpara)

    # Solving for x in x y and z dimensions
    sol_x = list(xSol.subs([(a,aa[0]),(b,bb[0]),(c,cc[0])]))
    sol_y = list(xSol.subs([(a,aa[1]),(b,bb[1]),(c,cc[1])]))
    sol_z = list(xSol.subs([(a,aa[2]),(b,bb[2]),(c,cc[2])]))

    # charge mass ration calculated based on x y and z motional dynamics
    QM = pd.DataFrame( {'qm_x': sol_x, 'qm_y': sol_y, 'qm_z': sol_z })

    return QM
