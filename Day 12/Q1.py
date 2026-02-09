# WAP to count the number of unique words in a given sentence using sets. sets{}
sentence = input("Enter a sentence: ")
sentence1 = sentence.lower()
words = sentence1.split()   # sentence ko words me tod diya
unique_words = set(words)  # set me daalne se duplicates hat jaate hain

print("Number of unique words:", len(unique_words))
print(unique_words)