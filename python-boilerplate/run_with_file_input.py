#!/usr/bin/env python
import sys
import fileinput


def function_to_do_something(inputstr):
  return inputstr


def main(argv):
  for line in fileinput.input(argv[1:]):
    result = function_to_do_something(line.strip())
    print result


if __name__ == "__main__":
  main(sys.argv)

