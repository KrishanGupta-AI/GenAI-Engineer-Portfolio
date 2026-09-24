name = input("Enter a name : ")
print("Good afternnon ," , name , "!")
print(f"Good Afternnon {name}!")

lettter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(lettter.replace("<|Name|>" , "Krishan").replace("<|Date|>" , "24 Sep 2021"))

space = 'Krishan  is a good boy'
print(space.find('  '))

shivam = space.replace("  ","   ")
print(shivam)

letter = "Dear Harry,\n this python course is nice.\nThanks!"
print(letter)