from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()


def main():
    with writable_file("_hello.txt") as file:
        file.write("Hello, World!")
        

main()