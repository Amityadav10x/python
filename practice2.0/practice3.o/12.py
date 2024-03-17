def capitalize_word(sentence):
    words = sentence.split()
    capitalize_word = []
    for word in words :
        capitalize_word.append(word.capitalize())
    return " ".join (capitalize_word)
    
sentence = "united university"
capitalize = capitalize_word(sentence)
print(capitalize)


