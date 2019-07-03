import time
import random
import json
from googletrans import Translator

translator = Translator()

def clean_word(word):
    return word.replace(',', '').strip()

def translate(word, to_ng='yo'):
    
    try:
        trans = translator.translate(clean_word(word), dest=to_ng)
        return trans
    except Exception:
        t = random.randrange(3, 8)
        print('error occurred retrying in {}s..'.format(t))
        time.sleep(t)
        print(word)
        translate(word)

def main():
    start_time = time.time()
    word_dict = dict()


    with open('./log.txt', 'r') as l:
        log = l.readlines()
        try:
            last_line = log[0]
        except IndexError:
            last_line = 0
        
    with open('./word.txt', 'r') as w:
        words = w.readlines()
        for i in range(int(last_line), len(words)):
            word = words[i]
            time.sleep(random.randrange(1, 3)) # wait for x second, to avoid ip band
            translated_word = translate(word).text
            word_dict[clean_word(word).lower()] = translated_word
            print(f"{i}| {clean_word(word)} |---------------------------| {translated_word} |")

            with open('./word_pair.json', 'w') as f:
                json.dump(word_dict, f, ensure_ascii=False)

            with open('./log.txt', 'w+') as l:
                l.write(str(i))

    duration = time.time() - start_time
    print(f"Translated {len(words)} words in {duration} seconds")

if __name__ == "__main__":
    main()
