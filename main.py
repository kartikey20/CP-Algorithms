import time
import random
import math
import numpy as np
import csv
import os
import _thread
import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.__version__)

print(str(0)+','+str(0), file=open('target.csv', 'w'))


def start_drag():
    os.system('python Draggable.py')


_thread.start_new_thread(start_drag, ())

initial = [5, 5]
bounds = [(-800, 800), (-800, 800)]

colors = np.array([
    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229)

]) / 255.


class Particle:
    def __init__(self, initial):
        self.pos = []
        self.vel = []
        self.best_pos = []
        self.best_error = -1
        self.error = -1
        for i in range(0, num_dimensions):
            self.vel.append(random.uniform(-1, 1))
            self.pos.append(initial[i])

    def update_velocity(self, global_best_position):
        w = 0.5
        c1 = 1
        c2 = 2

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            cog_vel = c1*r1*(self.best_pos[i]-self.pos[i])
            social_vel = c2*r2*(global_best_position[i]-self.pos[i])
            self.vel[i] = w*self.vel[i]+cog_vel+social_vel

    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.pos[i] = self.pos[i]+self.vel[i]

            if self.pos[i] > bounds[i][1]:
                self.pos[i] = bounds[i][1]

            if self.pos[i] < bounds[i][0]:
                self.pos[i] = bounds[i][0]

    def evaluate_fitness(self, fitness_function):
        self.error = fitness_function(self.pos)
        print("ERROR------->", self.error)

        if self.error < self.best_error or self.best_error == -1:
            self.best_pos = self.pos
            self.best_error = self.error


def fitness_function(x):
    x0, y0 = getXY('target.csv')
    x0 = float(x0)
    y0 = float(y0)
    total = 0
    total += (x0-x[0])**2 + (y0-x[1])**2
    return total


def getXY(filename):
    lat = 0
    long = 0
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            lat = row[0]
            long = row[1]
    return lat, long


class Interactive_PSO():
    def __init__(self, fitness_function, initial, bounds, num_particles):
        global num_dimensions

        num_dimensions = len(initial)
        global_best_error = -1
        global_best_position = []
        self.gamma = 0.0001
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(initial))

        i = 0
        while True:

            #print('x'+','+'y',file = open('pos.csv','w'))
            for j in range(0, num_particles):
                swarm[j].evaluate_fitness(fitness_function)
                print('global_best_position', swarm[j].error, global_best_error)

                if swarm[j].error < global_best_error or global_best_error == -1:
                    global_best_position = list(swarm[j].pos)
                    global_best_error = float(swarm[j].error)
                    plt.title("PyShine Interactive PSO, Particles:{}, Error:{}".format(
                        num_particles, round(global_best_error, 1)))

                if i % 2 == 0:
                    global_best_error = -1
                    global_best_position = list(
                        [swarm[j].pos[0] + self.gamma * (swarm[j].error) * random.random(),
                         swarm[j].pos[1] + self.gamma * (swarm[j].error) * random.random()])

            pos_0 = {}
            pos_1 = {}
            for j in range(0, num_particles):
                pos_0[j] = []
                pos_1[j] = []

            for j in range(0, num_particles):
                swarm[j].update_velocity(global_best_position)
                swarm[j].update_position(bounds)

                pos_0[j].append(swarm[j].pos[0])
                pos_1[j].append(swarm[j].pos[1])
                #print(str(swarm[j].pos[0])+','+str(swarm[j].pos[1]),file = open('pos.csv','a'))
                plt.xlim([-500, 500])
                plt.ylim([-500, 500])

            for j in range(0, num_particles):
                plt.plot(pos_0[j], pos_1[j],  color=colors[j], marker='o')

            x, y = getXY('target.csv')
            plt.plot(float(x), float(y),  color='k', marker='o')
            plt.pause(0.01)

            plt.clf()
            i += 1
        print('Results')
        print('Best Position:', global_best_position)
        print('Best Error:', global_best_error)


Interactive_PSO(fitness_function, initial, bounds, num_particles=16)  # let say 2 particles and 50 iterations
