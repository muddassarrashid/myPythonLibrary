
import numpy as np

class linearfittings():

    def __init__(self, x, y, wx):
        self.x = x
        self.y = y

        self.coef, self.cov = self.DoFit()
        self.errors = self.getErrors()
        self.fitfunc = self.fitFuctions(self.x)
        self.errorfunc = self.errorFunctions(self.x)

    def DoFit(self):
        coef, cov = np.polyfit(self.x,self.y,1, cov=True)
        return coef, cov

    def getErrors(self):
        errors = np.sqrt(np.diag(self.cov))
        return errors

    def getFitParameters(self):
        coef = self.DoFit()
        errors = self.getErrors()

        return coef, errors

    def fitFuctions(self,x):

        func = np.poly1d(self.coef)

        return func(x)

    def errorFunctions(self,x):
        xplus = self.coef + self.errors
        xminus = self.coef - self.errors

        xplusFunc = np.poly1d(xplus)
        xminusFunc = np.poly1d(xminus)

        errorArray = (np.vstack([xplusFunc(x),xminusFunc(x)])).T

        return errorArray
