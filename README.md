# Installation
To be able to use the program, install the python-packages specified
in requirements.txt by issuing the command
``` bash
$ python -m pip install reuqriements.txt
```

# Usage
To run the program call the main.py file located in prog/src/.
It takes a directory as an argument which is then analysed for its
contents. Giving a relative directory works fine.
```bash
$ python prog/src/main.py 
```

# Testing
To run the tests included in the file `prog/test/test.py` change to
the main project directory and run
```bash
$ pytest
```

# What it does currently
The program recursively iterates over the content of the given
directory, first displaying it in a similar way as the GNU/Linux
package `tree` would do. Thereafter, it builds a dictionary that
retains the structure of the given directory and contains important
information about each file such as the time and date it was last
edited, its size in KiloBytes as well as name and location. This
dictionary is then saved into a json file in location `prog/saves`.
It prints out the information that is collected about each file.

# What is planned
 - give it the ability to take two locations

# Issues
 - no warning, if the given argument is not a directory: the program
will just end without doing anything
 - the filename of the saved json does not reflect the location that
was given as an argument: if it is not renamed, you will forget over
which directory you let it run!

# License
This project is licensed under the MIT license. See [license](LICENSE)
for more detail.