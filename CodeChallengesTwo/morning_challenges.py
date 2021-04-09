# Shortest Word

def shortest_word(s): 
    string = s.split()
    newString = len(min(string))
    return(newString)


print(shortest_word("I don't think that word means what you think it means"))
# should return: 1