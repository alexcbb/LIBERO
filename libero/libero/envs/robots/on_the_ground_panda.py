import numpy as np

from robosuite.models.robots.manipulators.panda import Panda

class OnTheGroundPanda(Panda):
    @property
    def default_base(self):
        return None

    @property
    def init_qpos(self):
        return np.array(
            [0, -1.61037389e-01, 0.00, -2.44459747e00, 0.00, 2.22675220e00, np.pi / 4]
        )

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
            "coffee_table": lambda table_length: (-0.16 - table_length / 2, 0, 0.41),
            "living_room_table": lambda table_length: (
                -0.16 - table_length / 2,
                0,
                0.42,
            ),
        }