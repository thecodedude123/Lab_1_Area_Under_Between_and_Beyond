from scipy.integrate import quad
from scipy.optimize import fsolve
import numpy as np
import math

output = open('output.txt','w')

function = "x**2-x"
deltaX = 1e-3
a = 0
b = 5
critPoints = []
isNeg = False
def f(x):
    return eval(function)

for i in np.arange(a , b, deltaX):
    if f(i) < 0:
        if not isNeg and i not in critPoints:
            critPoints.append(i)
        isNeg = True
    if f(i) > 0:
        if isNeg and i not in critPoints:
            critPoints.append(i)
        isNeg = False
for i in range(len(critPoints)):
        if i != len(critPoints) - 1 and i != 0:
            critPoints[i] = fsolve(lambda x: f(x), [critPoints[i]])[0]

critPoints.append(a)
critPoints.append(b)
critPoints = sorted(set(critPoints))
output.write("roots and endpoints: " + str(critPoints))
def areaNet(boundsOfIntegration):
    integrals = []
    for i in range(len(boundsOfIntegration)):
        if i != len(boundsOfIntegration) - 1:
            integral = quad(lambda x: f(x), boundsOfIntegration[i], boundsOfIntegration[i+1])[0]
        elif i == len(boundsOfIntegration) - 1:
            integral = 0
        integrals.append(integral)
    for i in range(len(integrals)):
        integral += integrals[i]
    return integral
def areaMagnitude(boundsOfIntegration):
    integrals = []
    for i in range(len(boundsOfIntegration)):
        if i != len(boundsOfIntegration) - 1:
            integral = quad(lambda x: f(x), boundsOfIntegration[i], boundsOfIntegration[i+1])[0]
        elif i == len(boundsOfIntegration) - 1:
            integral = 0
        if integral < 0:
            integral *= -1
        integrals.append(integral)
    for i in range(len(integrals)):
        integral += integrals[i]
    return integral
def areaBounded(boundsOfIntegration, functions):
    integrals = []
    for i in range(len(boundsOfIntegration)):
        if i != len(boundsOfIntegration) - 1:
            integral = quad(functions[0], boundsOfIntegration[i], boundsOfIntegration[i+1])[0] + -quad(functions[1], boundsOfIntegration[i], boundsOfIntegration[i+1])[0] 
        elif i == len(boundsOfIntegration) - 1:
            integral = 0

        integrals.append(integral)
    for i in range(len(integrals)):
        integral += integrals[i]
    return integral


output.write("\ndistance traveled: " + str(areaMagnitude(critPoints)))
output.write("\nnet change: " + str(areaNet(critPoints)))
output.write("\nbounded area: " + str(areaBounded([0,math.pi],[lambda x: math.sin(x)/x,lambda x: 0.5*x-2])))
output.write("\nbounded area: " + str(areaBounded([-3,0],[lambda x: x**2*(x+3),lambda x: -(x**2*(x+3))])))
output.close()


        


