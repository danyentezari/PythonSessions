# How to find all mobile numbers with exactly three consecutive 7s.

### List of phone numbers
- 0501237776
- 0507779236
- 0501777777
- 0501712376
- 0502777877
- 0507778777
- 0527773212
- 0521777212

### Regular expression pattern
^(05(0|2|4|6))([0-6]|[8-9])\*(777)([0-6]|[8-9])*$

### Breakdown of the pattern
| Expression | Explanation |
| ------ | ------ |
|^(05(0\|2\|4\|6)) | pattern starts with 050, or 052, or 054, or 056
|([0-6]\|[8-9])* | followed by zero or more numbers between 0 to 6 or 8 to 9
|\(777\) | followed by three consecutive 7s, and
| \(\[0-6]\|[8-9])\*\$ | ending with zero or more numbers between 0 to 6 or 8 to 9

### Resources
- Regex Cheatsheet
[https://www.debuggex.com/cheatsheet/regex/python](https://www.debuggex.com/cheatsheet/regex/python)
- Video on regular expressions (this is math not programming). 
[https://www.youtube.com/watch?v=1qGPpeVZvdM]

    Note:
Regular expressions are used in Linguistics and Computer Science. You may need some familiarity with notations used in "Formal Languages" and "Automata Theory". 
