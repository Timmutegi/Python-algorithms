def headline(text: str, centered: bool = True) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

print(headline("Python Type Checking"))
print(headline("use MyPy", centered="center"))