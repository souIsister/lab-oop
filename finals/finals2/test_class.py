from performer import Performer
from singer import Singer
from dancer import Dancer

def main():
    p = Performer("John", 25)
    print(p.get_name(), p.get_age())

    d = Dancer("Emily", 28, "Ballet")
    print(d.get_name(), d.get_age(), d.get_dance_style())

    d.dance()

    s = Singer("Linda", 35, "Soprano")
    print(s.get_name(), s.get_age(), s.get_vocal_range())

    s.sing()


if __name__ == "__main__":
    main()