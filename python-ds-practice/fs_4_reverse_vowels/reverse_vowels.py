def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    vowel_list = [char for char in s if char in vowels]
    result = ''
    for char in s:
        if char in vowels:
            result += vowel_list.pop()
        else:
            result += char
    return result

print(reverse_vowels("Hello!")) # 'Holle!'
print(reverse_vowels("Tomatoes")) # 'Temotaos'
print(reverse_vowels("Reverse Vowels In A String")) # 'RivArsI Vewols en e Streng'
print(reverse_vowels("aeiou")) # 'uoiea'
print(reverse_vowels("why try, shy fly?")) # 'why try, shy fly?'
