from metrics.bleu2 import bleu2
from metrics.chrf import chrf
from metrics.gleu import gleu
from metrics.meteor import meteor
from metrics.nist import nist
from metrics.wer import wer

def evaluate(ref, pred):
    bleu2_score = bleu2(ref, pred)
    print("BLEU: ", bleu2_score)

    #ribes_score = ribes(ref, pred)
    #print("RIBES: ", ribes_score)

    gleu_score = gleu(ref, pred)
    print("GLEU: ", gleu_score)

    chrf_score = chrf(ref, pred)
    print("CHRF: ", chrf_score)

    meteor_score = meteor(ref, pred)
    print("METEOR: ", meteor_score)

    nist_score = nist(ref, pred)
    print("NIST: ", nist_score)

    wer_score = wer(ref, pred)
    print("WER: ", wer_score)

    print("\n")

evaluate("asistent_testset/testset_sl.txt", "asistent_testset/translation_general_asistent.txt")
evaluate("asistent_testset/testset_sl.txt", "asistent_testset/translation_google.txt")

evaluate("domain_translations/mil_test_sl.txt", "domain_translations/translation_general_mil.txt")
evaluate("domain_translations/mil_test_sl.txt", "domain_translations/translation_domain_mil.txt")
evaluate("domain_translations/mil_test_sl.txt", "domain_translations/translation_google.txt")
