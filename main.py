from generate import make_map
from gui import  display
def main():

    # read input for maze size (maze is a square)
    size = 20

    map = make_map(size)
    display(map)


if __name__ == "__main__":
    main()
