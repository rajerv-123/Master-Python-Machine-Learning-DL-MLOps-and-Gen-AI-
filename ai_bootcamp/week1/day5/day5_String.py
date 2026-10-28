#split()
text="Python is a programming language"
words=text.split()
# print(words)   

#join()
words_list=["Python", "is", "a", "programming", "language"] 
# print(" ".join(words_list))  # Joins the list into a single string with spaces  


text="Python is a programming language"
updated_text=text.replace("Python", "Java")  # Replaces 'Python' with 'Java'
# print(updated_text)  # Output: Java is a programming language

messy="   Python is a programming language   "
cleaned_text=messy.strip()  # Removes leading and trailing whitespace
# print(cleaned_text)  # Output: Python is a programming language