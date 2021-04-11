## Filename: byte.py
 # Author: Marcelo Feitoza Parisi
 # 
 # Description: Convert object/file
 # byte notation.
 # 
 # ###########################
 # # DISCLAIMER - IMPORTANT! #
 # ###########################
 # 
 # Stuff found here was built as a
 # Proof-Of-Concept or Study material
 # and should not be considered
 # production ready!
 # 
 # USE WITH CARE!
##
import math

# Got this from stackoverflow
def convert_size(size_bytes):
    # If our size is 0, return 0 B
    if size_bytes == 0:
        return "0  B"

    # Size units
    size_name = (" B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")

    # Checking the base for our division
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)

    # Rounding the resulting value
    s = round(size_bytes / p, 2)

    # Return the size
    return "%s %s" % (s, size_name[i])