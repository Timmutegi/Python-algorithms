"""
In this example, you write a with statement with os.scandir() as the context manager supplier. 
Then you iterate over the entries in the selected directory (".") and print their name and size on the screen. 
"""
import os

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")