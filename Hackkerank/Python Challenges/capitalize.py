def solve(s):
    split_text = list(s)
    if split_text[0].isalpha():
        split_text[0] = split_text[0].title()
    for i in range(1, len(split_text)):
        if split_text[i-1] == " ":
            split_text[i] = split_text[i].title()
    return "".join(split_text)

print(solve("this string has 1too many  spaces"))
