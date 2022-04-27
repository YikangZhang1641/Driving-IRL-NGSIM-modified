from NGSIM_env.envs.ngsim_env import NGSIMEnv
import matplotlib.pyplot as plt
from NGSIM_env.utils import *
import numpy as np
import csv
from NGSIM_env.utils import *
from gym.utils.play import *

# parameters
n_iters = 200
lr = 0.05
lam = 0.01
feature_num = 8
vehicle_id = 317
period = 0
render_env = True

# create environment
print('Target Vehicle: {}'.format(vehicle_id))
# env = NGSIMEnv(scene='us-101', period=period, vehicle_id=vehicle_id, IDM=False)
env =
play(env, keys_to_action={'', }) # keys pressed : actions
