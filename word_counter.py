

text = input("Hello write your text here: ")

splitted_text_0 = text.split(" ")
unique_words = []
splitted_text = []

for x in splitted_text_0:
    if x.strip() != "":
        splitted_text.append(x)

for i in range(len(splitted_text)):
    is_unique = True
    for j in range(len(splitted_text)):
        if splitted_text[i] == splitted_text[j] and i != j:
            is_unique = False
            break
    if is_unique:
        unique_words.append(splitted_text[i])

print(f"Unique words in your text: {unique_words}")

print(f"Count of words in your text: {len(splitted_text)}")

