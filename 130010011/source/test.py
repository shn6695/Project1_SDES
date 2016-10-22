from scipy.integrate import odeint
import numpy as np
import unittest
import mock

def func(initial,t):
	return 10

class testforfiggen(unittest.TestCase):

    def check_odeint(self):
    	t = np.linspace(0.0,5,50)
    	initial = 0
    	ans = odeint(func,initial,t)
    	self.assertAlmostEqual(ans[-1],50)
