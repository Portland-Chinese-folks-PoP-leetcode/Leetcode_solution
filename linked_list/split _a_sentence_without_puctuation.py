a_string = "Th!is ?is a$ s@en!!te?!nce."
string_no_punctuation = re.sub("[^\w\s]", "", a_string)



word_list = string_no_punctuation.split()


print(word_list)

