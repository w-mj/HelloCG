import os
import json

SUBMIT_DIR = '/mnt/cgsubmit'
TESTDATA_DIR = '/mnt/cgtestdata'


def get_score(path: str):
    try:
        with open(path) as f:
            return int(f.read())
    except Exception:
        return 0

def main():
    score_file = os.path.join(SUBMIT_DIR, os.listdir(SUBMIT_DIR)[0])
    user_score = get_score(score_file)
    result = {'verdict': 'AC', 'score': user_score}
    print(json.dumps(result))

if __name__ == '__main__':
    main()
