# VocabTranslator

## Description 介绍

* English words to Chinese meanings.
* Including different parts of speech, meanings and forms.
* Batch translating.
* Based on <a href="http://dict.youdao.com/">dict.youdao.com</a>.
---
* 英语生词自动翻译机
* 多种词性、意思和不同形式
* 批量翻译
* 基于有道词典（<a href="http://dict.youdao.com/">dict.youdao.com</a>）

## Requirements 需要的库

* urllib
* lxml

## Instructions 使用说明

1. Enter vocab in file: __*vocab.txt*__. Single word (or phrase) in one line.
2. Run <a href="translator.py">translator.py</a> and wait.
3. Result will be shown in: __*result.txt*__.
4. To translate new words, clear __*vocab.txt*__ and enter new ones.
---
1. 在文件：__*vocab.txt*__ 里输入生词。 每行限一个词或短语。
2. 运行 <a href="translator.py">translator.py</a> 并等待。
3. 结果显示在文件： __*result.txt*__ 里。
4. 如果要翻译新的词语，请清空 __*vocab.txt*__ 再输入新的词语。

## Exceptions 问题处理

* If entering words that do not exist, its meaning will be empty.
* BUG: Sometimes, a few parts of __*result.txt*__ will be divided into lines incorrectly.
---
* 如果输入不存在的词，该词的解释将为空。
* BUG：__*result.txt*__ 里的单词解释有时会被错误分行（仅限于这个单词的解释，其他单词会正常），请手动调整。
