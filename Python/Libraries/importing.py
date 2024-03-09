from my_package import hello,goodbye
import sys

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])