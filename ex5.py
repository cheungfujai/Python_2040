def reverse(wonderland):
    return wonderland[::-1]

wonderland = raw_input('Please input a palindrome: ')

if (wonderland == reverse(wonderland)):
    print('Welcome to the wonderland!')
else:
    while wonderland != reverse(wonderland):
        wonderland = raw_input('No, you must input a palindrome: ')
        reverse(wonderland)

print('Welcome to the wonderland!')