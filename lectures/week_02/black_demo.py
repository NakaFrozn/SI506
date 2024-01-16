# Black package: PEP 08 compliant code formatter

# Repo: https://github.com/psf/black
# Docs: https://black.readthedocs.io/en/stable/

# Python community styling guide: PEP 08
# https://www.python.org/dev/peps/pep-0008/

# See also J. Finer, "How to Write Beautiful Python Code With PEP 8" (Real Python, 2018).
# https://realpython.com/python-pep8/

# REFORMAT ME with black!

# Styling issues exhibited by the example code below
# 1. Insufficent blank line separators between import statements and other code.
# 2. Use of ''' quotes rather than """ quotes to designate multi-line strings.
# 3. Incorrect spacing around assignment operators (=); use of single quotes (')
#    rather than double quotes (") to denote a string.
# 4. Inconsistent and/or excessive spacing between list ([...]) elements.
# 5. Inconsistent and/or excessive spacing between dictionary ({...}) items.
# 6. Insufficient blank line separators between function definitions and other code.
# 7. Incorrect spacing around function parameter default value assignment operator (=).
# 8. Incorrect spacing between function call arguments.
# 9. Incorrect spacing between function parentheses and function call arguments.

from pathlib import Path
sentences='''
This is a test of black's alleged formatting prowess.
Let's see how it performs.
'''
char ='a'
num=[1,2, 3,   4]
dict_ =    {'a':1, 'b' :  2}
def multiply(x, y = 1):
    return x*y
product_02=multiply(506,2)
print( f"\ncurrent working directory = {Path.cwd()}" )

# LINE LENGTH: black default line length defaults to 88 characters per line.
# https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length

# GOTCHA: black fails to reformat string exceeding line length limit (default = 88; overridden = 100)
# Fix: add black setting experimental-string-processing = true to pyproject.toml

string = "This string--a sequence of characters--is 128 characters long and exceeds the 88 character default line length by 38 characters."
# print(len(string))
