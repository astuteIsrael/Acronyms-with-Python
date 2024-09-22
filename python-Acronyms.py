# asking for phrase

# user_input = str(input("Enter a Phrase: "))
# text = user_input.split()
# Acronyms = " "
# for i in text:
#     Acronyms = Acronyms + str(i[0]).upper()
# print(Acronyms)


user_input = input("Enter a Phrase: ")
text = user_input.split()

# Start with an empty string

acronym = ""  
for word in text:
    acronym += word[0].upper()  # Concatenate the first letter of each word in uppercase
print(acronym)
