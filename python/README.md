# Python backend handling for G-code generation.

## Setting up the Python environment.

First, create a virtual environment. The name of this environment is `env`.

`python3 -m venv env`

Next, activate the virtual environment.

`source env/bin/activate`

Finally, install the required dependencies.

`pip3 install -r requirements.txt`


## Dependencies

[Pyserial](https://pythonhosted.org/pyserial/)

## G-code

[A helpful guide for G-code commands](https://marlinfw.org/meta/gcode/)

G0 - Linear non-print move.

G1 - Linear print move.

G28 - Home axis.
