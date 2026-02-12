arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']

def get_find(text):
    start = text.find('[')
    end = text.find(']')

    for i in range(start + 1, end):
        print(text[i], end='')

    if start != -1 and end != -1:
        print(' ', end='')

for a in arr:
    get_find(a)