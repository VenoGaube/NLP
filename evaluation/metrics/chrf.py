import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def chrf(trans_file, pred_file):
    refs = []
    with open(trans_file, encoding="utf8") as test:
        for line in test:
            line = line.strip().lower().split()
            refs.append(line)

    preds = []
    with open(pred_file, encoding="utf8") as pred:
        for line in pred:
            line = line.strip().lower().split()
            preds.append(line)

    score = nltk.translate.chrf_score.corpus_chrf(refs, preds)
    return score