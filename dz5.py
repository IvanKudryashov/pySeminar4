from dz4 import greate_file, read_file

def run_length_encoding(text: str):
    result = []
    a = None
    count = 1
    for i in text + chr(ord(text[-1]) + 1):
        if i == a:
            count += 1
        else:
            if count > 1:
                result.append(f'{count}{a}')
            else:
                result.append(a)
            count = 1
        a = i
    result.append(a)
    return ''.join(result[1:-1])


def decode_rle(text: str):
    count = ''
    result = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            if count:
                result += int(count) * i
                count = ''
            else:
                result += i
    return result

rle_text = run_length_encoding('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
print(rle_text)
greate_file('seminar4/RLE.txt', rle_text)
print(decode_rle(read_file('seminar4/RLE.txt')))