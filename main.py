#converting your text to lowercase
input_str = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
input_str = input_str.lower()
#print(input_str)

#Removing numbers if they are not necessary in your analysis
import re
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'
result = re.sub(r'\d+', '', input_str)
#print(result)
#removing punctuations
import string
input_str = "This &is [an] example? {of} string. with.? punctuation!!!!" # Sample string
result = input_str.translate(str.maketrans("","", string.punctuation))
print(result)

