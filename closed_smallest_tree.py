from closest_path import get_similar_words
import sys


def get_smallest_words(word):
    similar_words = get_similar_words(word)
    similar_words = [x for x in similar_words if x != word]
    # find smallest length word
    if len(similar_words) == 0:
        return []
    smallest_word = min(similar_words, key=len)
    smallest_len = len(smallest_word)
    small_words = [x for x in similar_words if len(x) == smallest_len]
    return small_words

if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print('Usage: ./main.py <word> depth')
        sys.exit(1)
    
    word = sys.argv[1]
    depth = int(sys.argv[2])

    if depth == 0:
        similar_words = get_similar_words(word, only_smaller=True)
        print(similar_words)
        sys.exit(0)

    if depth == 1:
        similar_words = get_similar_words(word, only_smaller=True)
        sim_dict = {w: get_similar_words(w, only_smaller=True) for w in similar_words}
        for [key, val] in sim_dict.items():
            if len(val) == 0:
                continue
            smallest_len_val = min(val, key=len)
            print(key + " => " + str(val) + " => " + smallest_len_val + " (" + str(len(smallest_len_val)) + ")")
    