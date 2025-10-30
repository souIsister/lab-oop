from typing import List
from birds import Bird

class BirdCage:
    def make_bird_sounds(self, birds: List[Bird]) -> None:
        for bird in birds:
            bird.make_sound()
