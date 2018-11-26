punct_signs = """.,"'()-;:"""

def words_from_text(text):
    text = text.lower()
    for char in punct_signs:
        text = text.replace(char, '')
    words  = text.split()    
    return words

def words_from file(filename):
    with open(filename, encoding='utf-8') as fh:
        text = fh.read()
    words = words_from_text(text)    
    return words

def main():
    print(words_from_file('text.txt'))

main()

