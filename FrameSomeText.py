sentence = input("Enter your desired sentence: ")

def FrameText(words):
    wordLength = len(max(words, key=len))
    print('*' * (wordLength + 4))
    for word in words:
        print('* {a:<{b}} *'.format(a=word, b=wordLength))
    print('*' * (wordLength + 4))
FrameText(sentence.split(" "))