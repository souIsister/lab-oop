from sparrow import Sparrow
from parrot import Parrot
from birdCage import BirdCage
from birds import Bird


def test1():
    s = Sparrow()
    print("Test case 1:", end=" ")
    s.make_sound()


def test2():
    p = Parrot()
    print("Test case 2:", end=" ")
    p.make_sound()


def test3():
    birds = [Sparrow(), Parrot()]
    print("Test case 3:")
    for bird in birds:
        bird.make_sound()


def test4():
    print("Test case 4:")
    try:
        bird = Bird()
        print("Bird class is NOT abstract.")
    except TypeError:
        print("Bird class is abstract.")


def test5():
    print("Test case 5:")
    cage = BirdCage()
    cage.make_bird_sounds([Sparrow(), Parrot()])


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
