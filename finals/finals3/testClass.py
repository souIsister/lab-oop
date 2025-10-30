from sparrow import Sparrow
from parrot import Parrot
from birdCage import BirdCage

if __name__ == "__main__":
    sparrow = Sparrow()
    parrot = Parrot()

    print("Test Case 1:")
    sparrow.make_sound()

    print("\nTest Case 2:")
    parrot.make_sound()

    print("\nTest Case 3:")
    birds = [sparrow, parrot]
    for b in birds:
        b.make_sound()
        
    print("\nTest case 4:") 
    print("Bird class is abstract.") 

    print("\nTest Case 5:")
    cage = BirdCage()
    cage.make_bird_sounds(birds)

