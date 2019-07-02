import time
import random

def clean_word(word):
    return word.replace(',', '').strip().lower()

def translate(word, to_ng='yo'):
    from googletrans import Translator
    translator = Translator()
    try:
        trans = translator.translate(clean_word(word), dest=to_ng)
        return trans
    except Exception:
        t = random.randrange(6, 13)
        print('error occurred retrying in {}s..'.format(t))
        time.sleep(t)
        try:
            trans = translator.translate(clean_word(word), dest=to_ng)
            return trans
        except Exception:
            t = random.randrange(8, 15)
            print('error occurred again retrying in {}s..'.format(t))
            time.sleep(t)
            trans = translator.translate(clean_word(word), dest=to_ng)
            return trans

def main():
    import json

    word_dict = dict()
    print('English --------------------------- Yoruba')
    with open('./word.txt', 'r') as words:
        for word in words:
            time.sleep(random.randrange(1, 5)) # wait for x second, to avoid ip band
            translated_word = translate(word).text
            word_dict[clean_word(word)] = translated_word
            print('{} ---------------------------{}'.format(clean_word(word), translated_word))
            with open('./word_pair.json', 'w') as f:
                    json.dump(word_dict, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
