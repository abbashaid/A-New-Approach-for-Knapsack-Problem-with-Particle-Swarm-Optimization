# ------------------------------------------------------------------------------
#
# Yusuf DURSUN
# Dynamically Solving Knapsack Problem Using Particle Swarm Optimization on Python
#
# ------------------------------------------------------------------------------

# Including project dependencies ...
import matplotlib.pyplot as plt
import random
import math


# Defining global variables [Important: Other variables and execution of the algorithm is at the bottom of the page] ...
names = ('Television', 'Camera', 'Projector', 'Walkman', 'Radio', 'Mobile Phone', 'Laptop')
profit = [35, 85, 135, 10, 25, 2, 94]
kg = [2, 3, 9, 0.5, 2, 0.1, 4]
maxKg = 25


# The function we are trying to maximize ...
def fncMax(x):
    t = fncTaneProfit(x)
    return t + fncTaneKilogram(x, t)


def fncTaneProfit(x):
    total = 0
    for i in range (len (x)):
        total += x[i] * profit[i] # Grain *Profit
    return total


def fncTaneKilogram (x, totalProfit):
    total = 0
    for i in range (len (x)):
        total += x[i] *kg[i] # Grain *kg

    if total <= maxKg:
        if total <= totalProfit:
            return totalProfit - total
        else:
            return 0
    else:
        return -totalProfit

    """
        If kilogram exceeds maxKg;
        returning the negative of the 1st function value as penalty points from the function,
        It resets the result value so that it does not take the existing value.
    """



# Our particle class ...
class Particle:
    def __init__ (self, initialValues):
        self.position = [] # particle position
        self.speed = [] # Particle speed
        self.pBest = [] # Individual best position
        self.pBestApproach = -1 # Individual best approach
        self.approach = -1 # Individual approach

        for i in range (numberOfPar):
            self.speed.append(random.uniform (-1, 1))
            self.position.append(initialValues[i])

    # Calculate the fitness for the function ...
    def compute(self, function):
        self.approach = function (self.position)

        # Check if your current position is the individual best ...
        if self.pBestApproach > self.pBestApproach or self.pBestApproach == -1:
            self.pBest = self.position
            self.pBestApproach = self.approach

    # Update new particle speed ...
    def speed_guncelle (self, groupMaxPosition):
        w = 0.99 # Coefficient of request to keep the particle's previous velocity.
        c1 = 1.99 # Coefficient of wanting to keep their own best.
        c2 = 1.99 # Coefficient of wanting to get the best value of the flock.

        for i in range (numberOfPar):
            r1 = random.random()
            r2 = random.random()

            cognitive_speed = c1 *r1 *(self.pBest [i] -self.position [i])
            social_speed = c2 *r2 *(groupMaxPosition [i] -self.position [i])
            self.speed [i] = w *self.speed [i] + cognitive_speed + social_speed

    # Calculating new positions according to the newly updated particle velocity ...
    def position_update (self, boundryValues​​):
        for i in range (numberOfPar):
            maxSpeed = (boundryValues​​[i][1] - boundryValues​​[i][0])

            if self.speed [i] <-maxSpeed:
                self.speed [i] = -maxSpeed
            elif self.speed [i]> maxSpeed:
                self.speed [i] = maxSpeed

            self.position [i] = self.position[i] + self.speed[i]

            if self.position [i] > boundryValues​​​​[i][1]: # If the position is above the upper limit value, pull it to the upper limit value
                self.position [i] = boundryValues​​[i][1]
            elif self.position [i] < boundryValues​​​​[i][0]: # If the position is below the lower limit value, pull it to the lower limit value
                self.position [i] = boundryValues​​[i][0]
            else:
                self.position [i] = round(self.position[i])

class PSO:
    stepProfit, stepKg, groupMaxPosition, groupMaxApprox = [], [], [], -1

    def __init __ (self, function, initialValues, boundryValues ​​,numberOfParticles ,numSwarm, maxIter, stepsPrinting = True): # fncMax, initialValues, boundryValues ​​,Number of particles = 7, maxIter = 0.1
        global numberOfPar

        parNumber = len(initialValues)
        self.groupMaxApproach = -1 # Best approach for group
        self.groupMaxPosition = [] # Best position for group

        # Let's assign initial values ​​to our flock ...
        swarm = []
        for i in range (numSwarm):
            swarm.append (Particle(initialValues))

        # Optimization cycle start ...
        counter = 0
        while counter < maxIter:
            counter + = 1

            # Calculating the suitability of the particles in the flock to the function ...
            for j in range (numSwarm):
                count[j].compute(function)

                # Checking whether the current widget is the best globally and making necessary updates.
                if swarm[j].approx> self.grupMaxApprox or self.grupMaxApprox == -1:
                    self.groupMaxPosition = list (number [j] .position)
                    self.groupMaxApprox = float (suru [j]. approximation)

            # Updating the speed and positions in the herd.
            for j in range (numSwarm):
                suru [j] .speed_guncelle (self.grupMaxPosition)
                suru [j] .position_guncelle (boundryValues)

            totalProfit = 0
            totalKg = 0
            for i in range (numberOfParticles):
                total Profit + = self.groupMaxPosition [i] *profit [i]
                totalKg + = self.groupMaxPosition [i] *kg [i]
            self.adimKar.append (totalProfit)
            self.adimKg.append (totalKg)

            if stepsPrinting:
                print (self.groupMaxPosition)

    # Printing results ...
    def PrintResult (self):
        print ('\ n \ n RESULTS: \ n \ n')
        total Profit = 0
        totalKg = 0
        for i in range (len (self.grupMaxPosition)):
            print (names[i], ':', self.groupMaxPosition[i], 'grain', sep = '')
            totalProfit + = self.groupMaxPosition [i] *profit [i]
            totalKg + = self.groupMaxPosition[i] * kg[i]
        print ('#' *50, '\ nAquired Profit:', totalProfit, ', \nKg:', totalKg, sep = '')

    # Plotting the results on the screen [If we do not want to save the result image to the computer, the parameter named 'fileName' must remain empty!] ...
    def PlotResult (self, filename = ''):
        plt.plot (self.adimKg, self.adimKar)
        plt.xlabel ('Kilogram (kg)')
        plt.ylabel ('Profit made')
        plt.title ('Profit vs. Kilogram Chart')
        plt.grid (True)

        if not (fileName == ''): # If the variable named 'fileName' is not empty, save the file with that name in png format.
            fileName = fileName + ". png"
            plt.savefig(fileName)

        plt.show()
        plt.close()


# Assigning initial and limit values ​​and running the algorithm ...

# initialValues ​​= [0, 0, 0, 0, 0, 0, 0] # Start values ​​[x1, x2 ...]
# nerveValues ​​= [(0, 12), (0, 8), (0, 2), (0, 50), (0, 12), (0, 250), (0, 6)] # Limit values ​​[ (x1_min, x1_max), (x2_min, x2_max) ...]

print ('[item_name: lower_ limit - upper_ limit] \n', sep = '')
initialValues ​​= []
boundryValues ​​= []
for i in range (len (names)):
    initialValues.append(0) # Start values ​​[x1, x2 ...]
    boundryValues.append ((initialValues ​​[i], math.floor (maxKg /kg[i]))) # Limit values ​​[(x1_min, x1_max), (x2_min, x2_max) ...]
    print (names [i], ':', boundryValues​​[i][0], '-', boundryValues[i][1], sep = '')
print ('\nsum to', len (names), 'variable exists ... \ n \ n', sep = '')

pso = PSO(fncMax, initialValues, boundryValues ​​,numberOfParticles = len(names), numSwarm = 100, maxIter = 50, stepsPrinting = True)
pso.PrintResult()
pso.PlotResult(fileName = 'test')

# End of algorithm :)