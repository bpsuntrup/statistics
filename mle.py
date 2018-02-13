#!/usr/bin/python
from random import random
from time import sleep

# Suppose X_1, ..., X_n independently follow Pareto(\theta,2). The the 
# likelihood function of \theta given X_1, ..., X_n is 
#
# L(\theta|X_1,...,X_n) = \prod_{i=1}^n \frac{2}{\theta(1+\frac{X_i}{\theta})^3}
#
# Which gives us the log-likelihood function:
# l(\theta) = ln\;\circ L(\theta) = n\,ln(2) - n\,ln(\theta) - 
#                       3\sum_{i=1}^nln(1+\frac{X_i}{\theta})
#
# Hence, solving the equation l'(theta) = 0 should give the MLE of theta. This equation,
#
# 0 = -\frac{n}{\theta} + 3\sum_{i=1}^n\frac{X_i}{1+\theta X_i} 
#
# is difficult to solve. 
# 
# Below, I represent the RHS of the equation with the function mleq(theta) and 
# numerically solve mleq(mle) == 0 for "mle". 
#
# The data is taken from Example 4.6.2 in Bain and Engelhardt's Introduction to 
# Probability and Mathematical Statistics, 2Ed.
# 
# This program is based on Exercise 11 on page 329 of the same book. 
#

# Data from a Pareto distribution
data = [0.85,1.08,0.35,3.28,1.24,2.58,0.02,0.13,0.22,0.52]

# Forward precision 
precision = .0001

# mleq is the ML equation for a sample taken from a Pareto
# distribution. The solution "mle" of the equation will result in
# mleq(mle) == 0.

def mleq(mle, d = data):
    s = 0
    for datum in d:
        s = s + 3*datum/(mle*mle+datum*mle)
    return s - len(d)/mle
    
# Finds solution to mleq(i) == 0 iteratively with forward precision of "precision"
def find_mle():
    i = random()
    r = mleq(i)
    li = random()
    lr = random()
    # if 
    while (True):
        r = mleq(i)
        if r > precision:
            # then r r needs to be smaller. So does making i bigger make
            # r smaller or does making i smaller make r smaller?
            if i <= li and r <= lr:
                # Then making i smaller makes r smaller
                li = i
                lr = r
                i = i*.9
            elif i <= li and r >= lr:
                # Then making i smaller makes r bigger
                li = i
                lr = r
                i = i*1.1
            elif i >= li and r >= lr:
                # then making i bigger makes r bigger
                li = i
                lr = r
                i = i*.9
            else:
                li = i
                lr = r
                i = i*1.1
        elif r < -precision:
            if i <= li and r <= lr:
                # Then making i smaller makes r smaller
                li = i
                lr = r
                i = i*1.1
            elif i <= li and r >= lr:
                # Then making i smaller makes r bigger
                li = i
                lr = r
                i = i*0.9
            elif i >= li and r >= lr:
                # then making i bigger makes r bigger
                li = i
                lr = r
                i = i*1.1
            else:
                li = i
                lr = r
                i = i*0.9
        else:
            break
        print("i:{} r:{}".format(i,r))
       # sleep(.5)
    print("Final result: i:{} r:{}".format(i,r))

if __name__ == "__main__":
    find_mle()
