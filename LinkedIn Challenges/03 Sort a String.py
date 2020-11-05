def sort_a_string(s: str) -> str:
    """Takes a string and returns a string with those words sorted alphabetically.
    Case should be ignored... and punctuation..."""
    word_list = sorted([eachWord.lower() + eachWord for eachWord in s.split()])
    # print(word_list)
    cleaned_word_list = [eachWord[len(eachWord)//2:] for eachWord in word_list]
    # print(cleaned_word_list)
    return " ".join(cleaned_word_list)
    
    

# print("Hello world")
# print(sort_a_string("This sentence is in alphabetical order"))
# print(sort_a_string("one, two, three, four, five, six, seven, eight, nine, ten"))

def test_sort_a_string():
    """Testing various use cases"""
    assert sort_a_string("This sentence is in alphabetical order") == "alphabetical in is order sentence This"

def test_sort_a_string_with_punctuation():
    """Testing with punctuation"""
    assert sort_a_string("one, two, three, four, five, six, seven, eight, nine, ten") == "eight, five, four, nine, one, seven, six, ten three, two,"