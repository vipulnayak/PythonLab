import difflib

def stringsimilarity(str1,str2):
    result=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return result.ratio()
str1="Python Exercises"
str2="Python Exercises"
print("Original string")
print(str1)
print(str2)
print("the similarity of two strings is ")
print(stringsimilarity(str1,str2))
str1="Python Exercises"
str2="Python Exercise"
print("Original string")
print(str1)
print(str2)
print("the similarity of two strings is ")
print(stringsimilarity(str1,str2))