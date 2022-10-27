
from keyinput import KeyInput

def main():
    with KeyInput() as input_generator:
        for e in input_generator:
            print(repr(e))

if __name__ == '__main__':
    main()