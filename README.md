# keyboardmap

non-blocking keyboard input map

## Statement Before View Code

The code in this repo is **NOT CREATED BY MYSELF**, which most comes from [curtises](https://github.com/bpython/curtsies) with unrelated code optimization and simplification for reading.

## Usage

```python
from keyinput import KeyInput

def main():
    with KeyInput() as input_generator:
        for e in input_generator:
            print(repr(e))

if __name__ == '__main__':
    main()
```