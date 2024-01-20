import os


def main():
    name = "World"
    print("Starting: " + str(os.getuid()))
    print("Hello " + name + "!")


if __name__ == "__main__":
    main()