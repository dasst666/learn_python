

text = input("Hello write your text here: ")

raw_words = text.lower().split()
unique_words = []
splitted_words = []
longest_word = ""

for x in raw_words:
    if x.strip() != "":
        splitted_words.append(x)

for i in range(len(splitted_words)):
    if len(splitted_words[i]) > len(longest_word):
        longest_word += splitted_words[i]
    is_unique = True
    for j in range(len(splitted_words)):
        if splitted_words[i] == splitted_words[j] and i != j:
            is_unique = False
            break
    if is_unique:
        unique_words.append(splitted_words[i])
# можно переписать из collections Counter

print(f"Unique words in your text: {unique_words}")

print(f"Count of words in your text: {len(splitted_words)}")

print(f"Most longest word in your text: {max}")

