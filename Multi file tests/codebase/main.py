import datetime
from utils import multiply


def main():
    print("Hello, this is the main file.")
    result = multiply(3, 5)
    print("Result of multiplication:", result)

    print(datetime.datetime.now())


if __name__ == "__main__":
    main()
