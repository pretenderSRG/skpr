def has_r(word):
    if type(word) != str:
        raise TypeError(f"str expected got {type(word)} instead")
    return "r" in word.lower()
