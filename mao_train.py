import tensorflow as tf
import tfdeploy as td
import numpy as np
import math
from loader import *

N_INPUT = 769
NUM_DATA = 100
VOLUME_SIZE = 100

BS_AE = 20


export_path = 'net/exports'

# Get the data from the game files
# validation_test, validation_test_l = getTest(N_INPUT, 40, 44)
whiteWins, blackWins = getTrain(N_INPUT, NUM_DATA, VOLUME_SIZE)


def getBatchAE(start, size):
    global whiteWins
    global blackWins

    size = size//2
    start = start*size
    xR = []
    for i in range(start, start+size):
        xR.append(whiteWins[i])
        xR.append(blackWins[i])
        random.shuffle(xR)
    return xR


i = 0
batch_xs = getBatchAE(i, BS_AE)
print(batch_xs.shape)


