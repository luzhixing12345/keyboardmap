
from keyboardhandler.keyinput import KeyInput

def main():
    keyboard = KeyInput()
    with keyboard as k:
        while True:
            ch = k.get_input()
            if (ch == 'ESC'): break
            print("You pressed "+repr(ch))

if __name__ == '__main__':
    main()