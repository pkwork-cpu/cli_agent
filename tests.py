from functions.write_file import write_file


def test():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"test 1:\n{result}\n")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"test 2:\n{result}\n")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"test 3:\n{result}\n")


if __name__ == "__main__":
    test()
