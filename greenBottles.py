import time
number = [
'Zero',
'One',
'Two',
'Three',
'Four',
'Five',
'Six',
'Seven',
'Eight',
'Nine',
'Ten' ]

text_one = 'green bottles hanging on the wall'
text_two = 'And if one green bottle should accidentally fall\nThere\'ll be'

# Each part of the loop makes a new verse
for i in range(10, 0, -1):
    print(number[i], text_one)
    time.sleep(1)
    print(number[i], text_one)
    time.sleep(1)
    print(text_two, number[i-1], text_one)
    time.sleep(1)
