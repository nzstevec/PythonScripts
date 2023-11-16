import os
import sys

def create_file(filename, size):
    with open(filename, 'w') as f:
        f.write('0' * size)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python make_file.py filename size")
        sys.exit(1)

    filename = sys.argv[1]
    size = int(sys.argv[2])

    create_file(filename, size)