import numpy as np
"""Use numpy arrays and lists"""
def kir(t_nods_quantity, x_nods_quantity, grid, transfer_velocity, time_step, x_step):
    sigma = transfer_velocity * time_step / x_step
    for m in range(1, x_nods_quantity - 1):
        grid[m] = grid[m] - np.dot(sigma ,(grid[m + 1] - grid[m]))
    return grid
