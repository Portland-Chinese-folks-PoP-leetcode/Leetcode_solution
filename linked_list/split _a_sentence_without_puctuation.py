import re
a_string = "Th!is ?is a$ s@en!!te?!nce."
print('the length of the a_string is ', len(a_string))
string_no_punctuation = re.sub("[^\w\s]", "", a_string)
print(dir(re))
print(string_no_punctuation)


word_list = string_no_punctuation.split()


print(word_list)
