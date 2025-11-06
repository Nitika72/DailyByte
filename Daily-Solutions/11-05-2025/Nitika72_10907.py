def word_count (sentence):
    word=sentence.split()
    count=len(word)
    return count

sentence=input("enter sentence")
a=word_count(sentence)
print ("no. of words =",a)
    