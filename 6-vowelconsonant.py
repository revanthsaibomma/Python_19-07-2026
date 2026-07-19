char = input("Enter a character: ").strip().lower()
if char in ['a', 'e', 'i', 'o', 'u']:
    print(f"The character {char} is a vowel.")
else:
    print(f"The character {char} is a consonant.")
