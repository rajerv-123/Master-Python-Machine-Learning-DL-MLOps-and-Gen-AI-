def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())  # Remove non-alphanumeric characters and convert to lowercase
    return text == text[::-1]  # Check if the cleaned text is the same forwards

input_text = "A man, a plan, a canal: Panama"
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:   
    print(f'"{input_text}" is not a palindrome.')       
    
      