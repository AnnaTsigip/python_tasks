
# восстановление

with open('file_003_2.txt', 'r') as data:
    string = data.readline()
    # print(string)


def decoding_rle(ss):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

print(decoding_rle(string))


with open('file_003_2_2.txt', 'w') as data:
    data.write(decoding_rle(string))