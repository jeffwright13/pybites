from typing import Tuple
vowels = "aeiou"

def strip_vowels(text: str) -> Tuple[str, int]:
    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    idx = cnt = 0
    chars = list(text)
    for char in chars:
        if char.lower() in vowels:
            chars[idx] = "*"
            cnt += 1
        idx += 1
    print(chars)
    print(cnt)
    return ("".join(chars), cnt)