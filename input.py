import os
import random


def createfile(name, number):
    inputfile = open(os.getcwd() + '/' + name + '.txt', 'w')
    for i in range(1, int(number)):
        inputfile.write(str(random.randint(100, 20000)))
        inputfile.write("\n")
    inputfile.write(str(random.randint(100, 20000)))
    inputfile.close()
