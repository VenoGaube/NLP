# Script for converting .xml files to aligned sentences

import xml.etree.ElementTree as ET

data_en = ET.parse('data/vojska-en.xml')
data_sl = ET.parse('data/vojska-sl.xml')

sentences_en = data_en.findall("seg")
sentences_sl = data_sl.findall("seg")

tgt_en = "vojska-en.txt"
tgt_sl = "vojska-sl.txt"

for sentence_en in sentences_en:
    corr_sl = sentence_en.get('corresp')
    new_s_en = ''
    new_s_sl = ''
    for word in sentence_en:
        new_s_en += word.text + ' '
    for word in data_sl.find(".//*[@id='" + corr_sl + "']"):
        new_s_sl += word.text + ' '

    with open('data/' + tgt_en, 'a', encoding='utf-8') as file:
        file.write(new_s_en[:-1] + '\n')

    with open('data/' + tgt_sl, 'a', encoding='utf-8') as file:
        file.write(new_s_sl[:-1] + '\n')

