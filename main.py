from gui import display
from generate import make_map


def main():

    # read input for maze size (maze is a square)
    size = 20

    map = make_map(size)
    # display(map)


if __name__ == "__main__":
    main()
