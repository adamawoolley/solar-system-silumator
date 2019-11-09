from dataclasses import dataclass
from typing import List

@dataclass
class system():
    planets: List
    suns: List
    star_map: str

    def update_position(self):
        pass

    def update_velocity(self):
        pass

    def update_acceleration(self):
        pass
