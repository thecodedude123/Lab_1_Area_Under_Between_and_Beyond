from scipy.integrate import quad
from scipy.optimize import fsolve
import numpy as np
import math

output = open('Lab_1_Area_Under_Between_And_Beyond.txt','w')
function = input("f(x): ")
funcType = input("function type (sin, cos, tan, sec, csc, cot, asin, acos, atan, asec, acsc, acot, ln, log, exp, sqrt, none): ")
function = function.replace('^', '**')
deltaX = 1e-3
mode = input("mode(magnitude, net):")
a = float(input("a: "))
b = float(input("b: "))
critPoints = []
isNeg = False
def f(x):
    if funcType == "sin":
        return math.sin(eval(function))
    elif funcType == "cos":
        return math.cos(eval(function))
    elif funcType == "tan":
        return math.tan(eval(function))
    elif funcType == "sec":
        return 1/math.cos(eval(function))
    elif funcType == "csc":
        return 1/math.sin(eval(function))
    elif funcType == "cot":
        return 1/math.tan(eval(function))
    elif funcType == "asin":
        return math.asin(eval(function))
    elif funcType == "acos":
        return math.acos(eval(function))
    elif funcType == "atan":
        return math.atan(eval(function))
    elif funcType == "asec":
        return math.acos(1/eval(function))
    elif funcType == "acsc":
        return math.asin(1/eval(function))
    elif funcType == "acot":
        return math.atan(1/eval(function))
    elif funcType == "ln":
        return math.log(eval(function))
    elif funcType == "log":
        base = float(input("base:"))
        return math.log(eval(function), base)
    elif funcType == "exp":
        return math.exp(eval(function))
    elif funcType == "sqrt":
        return math.sqrt(eval(function))
    else: 
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
output.write("roots and endpoints: " + str(critPoints) + "\n")
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

if mode == "magnitude":
    output.write("magnitude: " + str(areaMagnitude(critPoints)))
elif mode == "net":
    output.write("net: " + str(areaNet(critPoints)))
output.close()


        


