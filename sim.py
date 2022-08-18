from typing import Tuple

import numba as nb
import numpy as np

from fastdrag import drag_g7


@nb.njit
def simulate(
        sim_time: nb.float32,
        time_step: nb.float32,
        aim_dir_x: nb.float32,
        aim_dir_y: nb.float32,
) -> Tuple[np.ndarray, np.ndarray]:
    drag = 0.0
    flight_time = 0.0
    while flight_time < sim_time:
        flight_time += time_step
        drag = drag_g7(0.25)
    return (np.zeros(0), np.zeros(0))
