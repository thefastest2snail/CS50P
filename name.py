# import sys

# if len(sys.argv) < 2:
#     sys.exit("too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("too many arguments")

# print("hello, my name is", sys.argv[1])
# print (len(sys.argv))

import sys

if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:]: #slices in square brackets
    print("hello, my name is", arg)
