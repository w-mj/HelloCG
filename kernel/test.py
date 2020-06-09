import os

SUBMIT_DIR = '/mnt/cgsubmit'
TESTDATA_DIR = '/mnt/cgtestdata'


def get_score(path: str):
    try:
        with open(path) as f:
            return int(f.read())
    except Exception:
        return 0

def main():
    score_file = os.path.join(SUBMIT_DIR, "score")
    user_score = get_score(score_file)
    print(f'{{"score": {user_score}}}')

if __name__ == '__main__':
    main()
