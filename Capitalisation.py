def capitaliseEachWord(inpStr):
    output = " "
    for char in inpStr:
        if not output[-1].isalnum():
            output += char.upper()
        else:
            output += char.lower()
    return output[1:]

def sentenceCapitalisation(inpStr):
    output = ". "
    endChar = ".?!:\n"
    for pos, char in enumerate(inpStr):
        if (output[-2] in endChar and output[-1] == " ") or (output[-1] in endChar) or (output[-1] == ' ' and char.lower() == 'i' and inpStr[pos + 1] == ' '):
            output += char.upper()
        else:
            output += char.lower()
    return output[2:]
funcDict = {"1":capitaliseEachWord, "2":sentenceCapitalisation}

try:
    choice = funcDict[input('''Choose your formatting by entering the corresponding number:
    1) Capitalise the first letter of every word in the input(Title formatting)
    2) Capitalise the first letter of every sentence(Paragraph formatting)
''')]
except ValueError:
    sys.exit("Incorrect choice chosen. Please try again. Use the corresponding number for your choice")

inputTxt = input("Enter the text to be formatted")
print(f'Formatted text: \n{choice(inputTxt)}')
