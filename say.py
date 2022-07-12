# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.daemon("hello, " + sys.argv[1]) # ASCII art be like

import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])