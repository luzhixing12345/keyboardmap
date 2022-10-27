# keyboardmap

non-blocking keyboard input map

## Statement Before View Code

The code in this repo is **NOT CREATED BY MYSELF**, which most comes from [curtises](https://github.com/bpython/curtsies) with unrelated code optimization and simplification for reading.

## Usage

```python
from keyinput import KeyInput

def main():
    with KeyInput() as input_generator:
        while True:
            print(repr(input_generator.get_input()))

if __name__ == '__main__':
    main()
```

## Reference

https://stackoverflow.com/questions/22417323/how-do-enter-and-exit-work-in-python-decorator-classes

https://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python