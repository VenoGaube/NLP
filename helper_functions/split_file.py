# Script used for splitting the data to train, validation and test sets.

import random

def file_len(fname):
    with open(fname, encoding='mbcs') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#print(file_len('tc3_train_en11.txt'))
#print(file_len('tc3_train_en11_lower.txt'))

filename_tgt = 'path\\of\\target\\corpus'
filename_src = 'path\\of\\source\\corpus'

#filename_sl = 'data/military_corp/mil_sl.txt'
#filename_en = 'data/military_corp/mil_en.txt'

c = 0

with open(filename_src, 'r', encoding='utf8') as textfile_src, open(filename_tgt, 'r',encoding='utf8') as textfile_tgt:

    out_train_sl = open("tc3_train_tgt.txt", "a", encoding='utf8')
    out_train_en = open("tc3_train_src.txt", "a", encoding='utf8')
    out_test_sl = open("tc3_test_tgt.txt", "a", encoding='utf8')
    out_test_en = open("tc3_test_src.txt", "a", encoding='utf8')
    out_val_sl = open("tc3_val_tgt.txt", "a", encoding='utf8')
    out_val_en = open("tc3_val_src.txt", "a", encoding='utf8')

    for x, y in zip(textfile_src, textfile_tgt):
        if c % 100000 == 0:
            print("100000 lines processed.")
        x = x.strip().lower() + '\n'
        y = y.strip().lower() + '\n'
        rand = random.uniform(0, 1)

        # select the % of the sets
        if rand < 0.005:
            out_test_sl.write(y)
            out_test_en.write(x)
        elif rand < 0.01:
            out_val_sl.write(y)
            out_val_en.write(x)
        else:
            out_train_sl.write(y)
            out_train_en.write(x)
        c += 1


