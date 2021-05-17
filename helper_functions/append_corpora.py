# Script for combining and potentially preprocessing multiple corpora

filenames = ['corpus1', 'corpus2']
with open('corpus', 'a', encoding='utf-8') as outfile:
    for fname in filenames:
        print(fname)
        with open(fname, 'r', encoding='utf-8') as infile:
            for line in infile:
                outfile.write(line.lower())
