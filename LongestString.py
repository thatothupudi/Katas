def Longest_word(word):
    print("The longest word is: ")
    words = list(word.split(" "))
    length = []
    for t in words:
        length.append(len(t))
    Longest = max(length)
    returnlist = []
    for s in words:
        if len(s) == Longest:
            returnlist.append(s)
            list_word = s
            print(list_word)
Longest_word(input("Please enter your sentence: "))                