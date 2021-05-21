from google_trans_new import google_translator

translator = google_translator()

def en_sl_file_translate(source_file, output_file_dest):
    f_in = open(source_file, 'r', encoding="utf8")
    f_out = open(output_file_dest, 'a', encoding="utf8")

    lines = f_in.readlines()
    count = len(lines)
    for i, line in enumerate(lines):
        res = translator.translate(line, lang_src='en', lang_tgt='sl')
        f_out.write(res.lower() + "\n")
        print(i, "/", count)

    f_in.close()
    f_out.close()

en_sl_file_translate("domain_translations/mil_test_en.txt", "domain_translations/translation_google.txt")
