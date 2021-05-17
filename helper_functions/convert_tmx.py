# Script for converting .tmx files to aligned sentences

from translate.storage.tmx import tmxfile

with open("data/corpus.tmx", 'r', encoding='utf-8') as fin:
    tmx_file = tmxfile(fin, 'en', 'sl')

for node in tmx_file.unit_iter():
    with open('data/' + 'src.txt', 'a', encoding='utf-8') as file:
        file.write(node.source + '\n')

    with open('data/' + 'tgt.txt', 'a', encoding='utf-8') as file:
        file.write(node.target + '\n')
