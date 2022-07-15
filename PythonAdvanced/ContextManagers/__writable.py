import pathlib
import logging

file_path = pathlib.Path("hello.txt")

try:
    with file_path.open(mode="w") as file:
        file.write("Hello, World!")

except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)
