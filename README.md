First teachings of learning Python in the Software Engineering Foundations Bootcamp at Stony Brook University.

To run Python you need to install python3 and ipython
First install Python: https://www.python.org/downloads/
Then in the Terminal run $ pip3 install ipython

_________________________________________________
To run programs you need to be in the Terminal and write ipython
This should open you in ipython
To open a file, write the following:
    %run an7.py
This will open the file any7.py
From there you can run the functions written in the code.
    any7([1, 2, 7, 4, 5])
    will give you: "should be true" as defined in the code.

____________________________________________________
After running a file, you can also specify which function to run if there are multiple functions in the program.
- words.py contains multiple different functions
- One of the functions is called print_upper_words
- To use it, you would write print(print_upper_words("hey"))
- This will only run that function and give you the output which would be:
    - H
    - E
    - Y

___________________________________________________

- Unlike JavaScript, you do not need to link to a html or provide a console.log statement to run the program.
- in count_up.py we have count_up(5, 7) after our def count_up(start, stop) program
- If you %run count_up.py - you will automatically get:
    - 5
    - 6
    - 7