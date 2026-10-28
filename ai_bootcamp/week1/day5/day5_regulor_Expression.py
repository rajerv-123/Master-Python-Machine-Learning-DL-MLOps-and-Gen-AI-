import re


text = "The rain in Spain"
# Check if the string starts with "The" and ends with "Spain"
digits=re.findall(r'\d+', text)  # Finds all sequences of digits in the string
print(digits)  # Output: [] since there are no digits in the string   

updated_text = re.sub(r'Spain', 'France', text)  # Replaces 'Spain' with 'France'
print(updated_text)  # Output: The rain in France