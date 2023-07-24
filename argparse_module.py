import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


parser = argparse.ArgumentParser('Arguments: --file filename, --offset offset')
parser.add_argument("-file")
parser.add_argument("-ofs")

args = parser.parse_args()
n= int(args.ofs)

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened
decode_Caesar_cipher(encoded_text, -n)
