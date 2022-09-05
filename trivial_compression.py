import zlib
import base64


def compress_file(file, comp_file):
    with open(file) as f:
        text = f.read()
    count = 1
    i = 0
    compressed_text = text[i]
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            count += 1
            i += 1
        else:
            if count > 1:
                compressed_text += str(count)
            compressed_text += text[i + 1]
            i += 1
            count = 1
    if count > 1:
        compressed_text += str(count)
    with open(comp_file, 'w') as fl:
        fl.write(compressed_text)


# compress_file("decompressed_file.txt", "compressed_file.txt")


def decompress_file(comp_file, decompressed_file):
    with open(comp_file) as f:
        comp_text = f.read()
    i = 0
    decomp_text = ""
    while i < len(comp_text) - 1:
        if comp_text[i + 1].isnumeric():
            decomp_text += comp_text[i] * int(comp_text[i + 1])
            i += 2
        else:
            decomp_text += comp_text[i]
            i += 1
    if comp_text[-1].isalpha():
        decomp_text += comp_text[i]
    return decomp_text


def main():
    file1 = ""
    file2 = ""
    user_choose = input("If you want to compress your file press 1\nif you want to decompress your file press 2\n"
                        "input: ")
    if user_choose == '1':
        try:
            file1 = input("input file, that you want to compress: ")
            file2 = input("input file, where you want write compressed text: ")
            compress_file(file1, file2)
        except FileNotFoundError as er:
            print(f"{file1} or {file2} is not found!")
    if user_choose == '2':
        try:
            file1 = input("input file, that you want to decompress: ")
            file2 = input("input file, where you want write decompressed text: ")
            decompress_file(file1, file2)
        except FileNotFoundError as er:
            print(f"{file1} or {file2} is not found!")


main()
