text = list(input().split())
palindrome = input()
palindromes = []

for word in text:
    if word == ''.join(reversed(word)):
        palindromes.append(word)

print(f'{palindromes}')
print(f'Found palindrome {palindromes.count(palindrome)} times')
