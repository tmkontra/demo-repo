import os
import sys


def main():
    name = os.getenv("DEMO_NAME") or "World"
    print("Starting: " + str(os.getuid()))
    print("Hello " + name + "!")


if __name__ == "__main__":
    name = sys.argv[1]
    os.environ["DEMO_NAME"] = name
    main()