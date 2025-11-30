words_list = input().split(" | ")

notebook = {}
for pairs in words_list:
    word, definition = pairs.split(": ")
    if word not in notebook:
        notebook[word]=[]
    notebook[word].append(definition)

test_words = input().split(" | ")
command = input()
if command == "Test":
    for word in test_words:
        if word in notebook:
            print(f"{word}:")
            for definition in notebook[word]:
                print(f" -{definition}")
else:
    word_list = list(notebook.keys())
    print(" ".join(word_list))
