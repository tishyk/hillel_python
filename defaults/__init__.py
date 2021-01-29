import os

# can just be an empty file,
# but it can also execute initialization code for the package
# or set the __all__ variable, described later.
import sys
#Packages are a way of structuring Python’s module namespace by using “dotted module names”.

# Example structure
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...

print("init.py")
__author__ = 'sergii.tischenko'
author = 'sergii.tischenko'

# This would mean that from sound.effects import * would import the three named submodules of the sound package.
#
__path__.append(r'C:\Projects\basics\hillel2')



__all__  = ['echo', 'reverse', 'surround', 'session5_code', 'ver2']
# If __all__ is not defined,
# the statement from sound.effects import * does not import all submodules
# from the package sound.effects into the current namespace
import pprint
pprint.pprint(vars())

# By definition, if a module has a __path__ attribute, it is a package.
# A package’s __path__ attribute is used during imports of its subpackages.