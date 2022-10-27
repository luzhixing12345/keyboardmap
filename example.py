
from keyinput import KeyInput

def main():
    with KeyInput() as input_generator:
        while True:
            print(repr(input_generator.get_input()))

if __name__ == '__main__':
    main()