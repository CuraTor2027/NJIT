'''
    Ryan Arokia-Raj
    20231118
    CS100-019
    HW9_RyanArokiaRaj.py
'''

def file_copy(in_file, out_file):
    phrase = in_file.read()
    out_file.write(phrase)

def file_stats(in_file):
    phrase = in_file.read()
    
    lines = 0
    text = phrase.split("\n")
    for i in text:
        if i:
            lines += 1
    
    words = 0
    text = phrase.split(" ")
    for i in text:
        if i:
            words += 1

    characters = len(phrase)
    
    print(f"lines: {lines}")
    print(f"words: {words}")
    print(f"characters: {characters}")

# 1.
file1 = open("created_equal.txt", "w")
file1.write("We hold these truths to be self-evident,\nthat all men are created equal\n")
file1.close()

file1 = open("created_equal.txt", "r+")
file2 = open("copy.txt", "w")

file_copy(file1, file2)
copy_f = open('copy.txt')
copy_f.read()
copy_f.close()
file1.close()
file2.close()

#2.
file3 = open("created_equal.txt", "r+")
file_stats(file3)
file3.close()
