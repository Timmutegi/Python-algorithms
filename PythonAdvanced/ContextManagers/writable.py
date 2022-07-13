class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tab):
        if self.file_obj:
            self.file_obj.close()


def main():
    with WritableFile("hello.txt") as file:
        file.write("Hello, World!")


main()