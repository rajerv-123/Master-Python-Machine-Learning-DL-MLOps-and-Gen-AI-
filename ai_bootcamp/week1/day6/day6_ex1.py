def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            print(line_count, word_count)
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        
count_words_and_lines("sample.txt")