# keyboardmap

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

non-blocking keyboard input map

## Statement Before View Code

The code in this repo is **NOT CREATED BY MYSELF**, which most comes from [curtises](https://github.com/bpython/curtsies) with unrelated code optimization and simplification for reading.

## Usage

clone the code and `keyboardhandler` folder is what you need

example run as

```python
from keyboardhandler.keyinput import KeyInput

def main():
    keyboard = KeyInput()
    with keyboard as k:
        while True:
            ch = k.get_input()
            if (ch == 'ESC'): break
            print("You pressed "+ch)

if __name__ == '__main__':
    main()
```

if you want to control or use other keymaps or rename it, you should check what specific `ch` is and modify `CURSES_NAMES` or `_CURTSIES_NAMES` in [keymap.py](keyboardhandler/keymap.py) to create a new key-value in dict

for example:

```python
CURSES_NAMES = {
    b' ': 'space', # change ' ' to SPACE
    b'\x1b': "ESC",
    b'\t': "TAB",
    b'\x7f': "BACKSPACE",
    b'\n': "ENTER",
    ...
}
```

CURSES_NAMES has higher priority than _CURTSIES_NAMES

## Reference

https://stackoverflow.com/questions/22417323/how-do-enter-and-exit-work-in-python-decorator-classes

https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python