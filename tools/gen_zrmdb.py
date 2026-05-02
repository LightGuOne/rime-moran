# gen_zrmdb.py -- 生成 zrmdb.txt

# zrmdb.txt 格式:
# 字 tab 碼1 space 碼2 space 碼3 ...

from utils import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dict', action='store_true')
args = parser.parse_args()


if args.dict:
    print('---')
    print('name: moran_zrmdb')
    print(f'version: "{get_chars_version()}"')
    print('use_preset_vocabulary: false')
    print('...')

for (char, auxes) in aux_table.items():
    print(f'{char}\t{" ".join(auxes)}')
