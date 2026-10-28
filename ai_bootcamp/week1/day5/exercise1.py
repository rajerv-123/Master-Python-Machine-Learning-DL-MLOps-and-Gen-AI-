import re

def clean_text(text):
    # remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text) 
    # remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # convert to lowercase
    text = text.lower()
    return text
    
    
input_text = "Hello, World! This is a test.   "
cleaned_text = clean_text(input_text)   
print(cleaned_text)  # Output: hello world this is a test