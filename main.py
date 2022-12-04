import config
import spacy
import utils
from tqdm import tqdm
import collections
import time



# 日本語辞書の読み込み
nlp = spacy.load('ja_ginza')
# 品詞カウント用
pos_counter = collections.Counter()
# 品詞の出現回数をカウント
def count_pos_of_token(keyword):
    try:
        token_pos_pair = ''
        # 形態素解析
        nlp_keyword=nlp(keyword)
        for sent in nlp_keyword.sents:
            for token in sent:
                token_pos_pair+=f'{token.text}:{token.pos_}|'
                pos_counter[token.pos_]+=1
        return {'keyword': keyword, 'token_pos': token_pos_pair}
    except Exception:
        return {'keyword': keyword, 'token_pos': 'None'}
