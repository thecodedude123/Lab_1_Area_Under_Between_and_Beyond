from scipy.integrate import quad #for integrating functions
from scipy.optimize import fsolve #to solve for roots of a function
import numpy as np #to be able to search for roots of a function to a degree of precision 
import math #to use functions such as sin(x)

output = open('output.txt','w') #open a text file to store data

function = "x**2-x" #initialize the function
deltaX = 1e-3 # degree of precision to find the roots
a = 0 # lower bound of integration
b = 5 # upper bound of integration
critPoints = [] # points that we should integrate over to flip the sign if the area is negative to get the absolute value of the area
isNeg = False  # checking sections of the function that are negative
def f(x):
    return eval(function)  # turning f(x) into something that we can plug values into instead of being a string

for i in np.arange(a , b, deltaX): # looping over the points to find where the function changes signs
    if f(i) < 0: # finding where it changed signs
        if not isNeg and i not in critPoints: # making sure we don't have points that we don't need
            critPoints.append(i) # adding the point to the list
        isNeg = True # sets the value of isNeg since f(i) < 0
    if f(i) > 0: # finding where it changed sign
        if isNeg and i not in critPoints: # making sure we don't have points that we don't need
            critPoints.append(i) # adding the point to the list
        isNeg = False # sets the value of isNeg since f(i) > 0
for i in range(len(critPoints)): # looping through the points
    critPoints[i] = np.around(fsolve(lambda x: f(x), [critPoints[i]])[0], 10, out=None) # finding more precise roots of function

critPoints.append(a) # making sure the upper bound of integration is included
critPoints.append(b) # making sure the lower bound of integration is included
critPoints = sorted(set(critPoints))  # sorts the numbers from lowest to highest and makes sure there are no repeated points
output.write("roots and endpoints: " + str(critPoints))
def areaNet(boundsOfIntegration):  # makes a function to find the net area given some bound of integration
    integral = quad(lambda x: f(x), boundsOfIntegration[0], boundsOfIntegration[1])[0]  # evaluates integral from a to b subtracting area under the graph
    return integral # returns the integral

def areaMagnitude(boundsOfIntegration): # makes a function to find the magnitude of area given some bounds of integration for negative areas
    integrals = [] #creates a list of integrals 
    for i in range(len(boundsOfIntegration)): #loops through the integrals
        if i != len(boundsOfIntegration) - 1: #checks if the integral is in range of the bounds
            integral = quad(lambda x: f(x), boundsOfIntegration[i], boundsOfIntegration[i+1])[0] #evaluates the integral between those bounds
        elif i == len(boundsOfIntegration) - 1:  #checks if the integral isn't within the bounds
            integral = 0 # adds no area
        if integral < 0: # checks if the area is negative
            integral *= -1 #multiplies negative area by negative 1 
        integrals.append(integral) # adds that integral to list of integrals
    for i in range(len(integrals)): # loops though every integral in the list of integrals
        integral += integrals[i] # sets the integral equal to the sum of all of the areas that were turned positive
    return integral # returns the magnitude of the area
def areaBounded(boundsOfIntegration, functions): #makes a function to find the area between 2 graphs
    
    area = quad(functions[0], boundsOfIntegration[0], boundsOfIntegration[1])[0] - quad(functions[1], boundsOfIntegration[0], boundsOfIntegration[1])[0] # subtracts the negative area under the graph (the same as adding positive area) from the area above the graph. This can be done because the area above the graph is completely positive, and the area below is completely negative
    return area # returns the area bounded


output.write("\ndistance traveled: " + str(areaMagnitude(critPoints))) # outputs the distance traveled
output.write("\nnet change: " + str(areaNet([a,b])))  # outputs the net change
output.write("\nbounded area: " + str(areaBounded([0,math.pi],[lambda x: math.sin(x)/x,lambda x: 0.5*x-2]))) #outputs the bounded area in question 3 
output.write("\nbounded area: " + str(areaBounded([-3,0],[lambda x: x**2*(x+3),lambda x: -(x**2*(x+3))]))) # outputs the area in the loop for question 4 
output.close() # stops writing to the file


        


