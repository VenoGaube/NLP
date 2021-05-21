import jiwer

def wer(trans_file, pred_file):
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

    error = jiwer.wer(refs, preds)
    return error
