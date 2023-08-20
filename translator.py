from urllib import request
from urllib import parse
from lxml import etree
from time import sleep
from random import random


def remove_all(element, l: list):
    l2 = []
    for i in l:
        if i != element:
            l2.append(i)
    return l2

def get_meanings(kw):
    args = parse.urlencode({'word': kw, 'lang': 'en'})
    url = f'https://dict.youdao.com/result?{args}'
    req = request.Request(url)
    res = request.urlopen(req)
    html = res.read().decode('UTF-8')
    doc = etree.HTML(html)
    Xpath = doc.xpath('/html/body/div/div/div/div/div[1]/div/div/section/div[2]/div[2]/div/div/ul//li//span/text()')
    class_list = doc.xpath('/html/body/div/div/div/div/div[1]/div/div/section/div[2]/div[2]/div/div/ul//li//span/@class')
    class_list = remove_all("wfs-splice", class_list)
    meanings = f'\n--------------------\n{kw}\n'
    flag = 0
    for i in range(len(Xpath)):
        meanings += Xpath[i]
        if class_list[i] in ["trans", "transformation"]:
            meanings += '\n'
    return meanings


with open('vocab.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')

new_txt = ''
count = 1
for word in lines:
    new_txt += get_meanings(word)
    sleep_time = random()*5
    print(f'{word}翻译完毕，等待{sleep_time:.2f}秒 ({count}/{len(lines)})')
    sleep(sleep_time)
    count += 1

with open('result.txt', 'w', encoding='UTF-8') as f:
    f.write(new_txt)
