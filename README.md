# PassAlternater
Generates all possible alternations of a string based on specific rules, used for dictionary attacks

Usage
-----

By default, there is a list included in the script (you can see the source code for the list), which is very basic.
If this list does not cover your needs, you can use your own list, using the `-l <list>` flag. An example list is included
 in the source code, and contains lower and upper case. Extending this list is possible by adding strings to a line,
 separated with a comma.


You can use the `-s` flag to get statistics of the output the generator creates. Right now, this only includes the amount
 of possible passwords and the length of the initial word given.

Example
-------

    $ python3 generate.py test
    test
    tesT
    tes7
    ...
    735t
    735T
    7357

**note** This project is written for Python 3.x. This might later be written to be both Python 2.x and 3.x compatible

##Disclaimer
This tool is for educational purposes only and is not intended to be put into practise unless you have authorised access to the system you are trying to break into

## License
This software is licensed under the "Original BSD License".
```
  (C) 2015  NorthernSec          https://github.com/NorthernSec
  (c) 2015  Pieter-Jan Moreels   https://github.com/pidgeyl
```
