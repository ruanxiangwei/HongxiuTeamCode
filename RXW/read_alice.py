filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    words = contents.strip()
    num_words = len(words)
    print(f"the txt have {num_words} words")
