import nltk
import numpy as np
import statistics

nltk.download('wordnet')

def meteor(trans_file, pred_file):
    refs = []
    with open(trans_file, encoding="utf8") as test:
        for line in test:
            line = line.strip().lower()
            refs.append(line)

    preds = []
    with open(pred_file, encoding="utf8") as pred:
        for line in pred:
            line = line.strip().lower()
            preds.append(line)

    scores = []
    for pair in zip(refs, preds):
        scores.append(nltk.translate.meteor_score.meteor_score([pair[0]], pair[1]))

    meteor_score = statistics.mean(scores)
    return meteor_score
