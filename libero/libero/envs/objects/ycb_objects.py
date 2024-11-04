import os
import re

import pathlib

from robosuite.models.objects import MujocoXMLObject

from libero.libero.envs.base_object import register_object
from libero.libero import get_libero_path
import numpy as np
absolute_path = pathlib.Path(__file__).parent.parent.parent.absolute()


class YCBObjects(MujocoXMLObject):
    def __init__(self, name, obj_name, joints=[dict(type="free", damping="0.0005")]):
        super().__init__(
            os.path.join(
                str(absolute_path),
                f"assets/ycb_objects/{obj_name}/{obj_name}/{obj_name}.xml",
            ),
            name=name,
            joints=joints,
            obj_type="all",
            duplicate_collision_geoms=False,
        )
        self.category_name = "_".join(
            re.sub(r"([A-Z])", r" \1", self.__class__.__name__).split()
        ).lower()
        self.rotation = (0, 0)
        self.rotation_axis = "x"
        self.object_properties = {"vis_site_names": {}}

######################################
#           YCB Objects              # 
######################################
@register_object 
class Apple(YCBObjects):
    def __init__(self,
                 name="apple",
                 obj_name="apple",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Banana(YCBObjects):
    def __init__(self,
                 name="banana",
                 obj_name="banana",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class BowlYCB(YCBObjects):
    def __init__(self,
                 name="bowl_ycb",
                 obj_name="bowl_ycb",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class FlatScrewdriver(YCBObjects):
    def __init__(self,
                 name="flat_screwdriver",
                 obj_name="flat_screwdriver",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Fork(YCBObjects):
    def __init__(self,
                 name="fork",
                 obj_name="fork",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Hammer(YCBObjects):
    def __init__(self,
                 name="hammer",
                 obj_name="hammer"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Knife(YCBObjects):
    def __init__(self,
                 name="knife",
                 obj_name="knife"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Mug(YCBObjects):
    def __init__(self,
                 name="mug",
                 obj_name="mug"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class MustardBottle(YCBObjects):
    def __init__(self,
                 name="mustard_bottle",
                 obj_name="mustard_bottle"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Peach(YCBObjects):
    def __init__(self,
                 name="peach",
                 obj_name="peach"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class PitcherBase(YCBObjects):
    def __init__(self,
                 name="pitcher_base",
                 obj_name="pitcher_base"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class PlateYCB(YCBObjects):
    def __init__(self,
                 name="plate_ycb",
                 obj_name="plate_ycb",
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class PottedMeatCan(YCBObjects):
    def __init__(self,
                 name="potted_meat_can",
                 obj_name="potted_meat_can"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class PowerDrill(YCBObjects):
    def __init__(self,
                 name="power_drill",
                 obj_name="power_drill"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class RubiksCube(YCBObjects):
    def __init__(self,
                 name="rubiks_cube",
                 obj_name="rubiks_cube"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Scissors(YCBObjects):
    def __init__(self,
                 name="scissors",
                 obj_name="scissors"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class Spoon(YCBObjects):
    def __init__(self,
                 name="spoon",
                 obj_name="spoon"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object 
class TomatoSoupCan(YCBObjects):
    def __init__(self,
                 name="tomato_soup_can",
                 obj_name="tomato_soup_can"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None

@register_object
class TunaFishCan(YCBObjects):
    def __init__(self,
                 name="tuna_fish_can",
                 obj_name="tuna_fish_can"
                 ):
        super().__init__(
            name=name,
            obj_name=obj_name,
        )

        self.rotation = {
            "x": (-np.pi/2, -np.pi/2),
            "y": (-np.pi, -np.pi),
            "z": (np.pi, np.pi),
        }
        self.rotation_axis = None