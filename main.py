import os
import csv
import pickle
import logging
from logger import myLogger

# Declare Logger
logger = myLogger(__name__, log_level=logging.INFO)
logger = logger.setLogger()

char_load_file = 'characters.csv'
pkl_file = 'characters.pkl'

def char_dict_load():
    # Character File Load
    if os.path.exists(char_load_file):
        logger.info("Character Load")
        character = {}

        char_load = open(char_load_file, 'r', encoding='utf-8')
        reader = csv.reader(char_load, delimiter=',')

        for line in reader:
            character[line[0]] = line[2]
            # print(line[0], line[2])

        with open(pkl_file, 'wb') as f:
            pickle.dump(character, f)
            logger.info('Character File Dumped')

    else:
        logger.error("No Character File!!")
        import sys; sys.exit()



def char_to_pron(characters, hangul):
    # logger.info(characters)
    pron = ''
    logger.info(hangul)

    for _, v in enumerate(hangul):        
        if(ord(v) >= 44032 and ord(v) <= 55215):
            # logger.info(v)
            # logger.info(characters[v])
            pron += characters[v] + ' '
    
    logger.info(pron.strip())


if __name__ == '__main__':
    # char_dict_load()
    
    with open(pkl_file, 'rb') as f:
        characters = pickle.load(f)
        logger.info('Character File Loaded')
    
    char_to_pron(characters, '안녕하세요!!')
    char_to_pron(characters, '반가워요')