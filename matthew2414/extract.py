import os
import sys

import nltk
import polib

from nltk.tokenize import moses # Moses handles the punctuations better than the word_tokenize

PO_METADATA = {
    'Project-Id-Version': '1.0',
    'Report-Msgid-Bugs-To': 'tfbfgroup@googlegroups.com',
    'POT-Creation-Date': '2007-10-18 14:00+0100',
    'PO-Revision-Date': '2007-10-18 14:00+0100',
    'Last-Translator': 'you <you@example.com>',
    'Language-Team': 'English <yourteam@example.com>',
    'MIME-Version': '1.0',
    'Content-Type': 'text/plain; charset=utf-8',
    'Content-Transfer-Encoding': '8bit',
}

def tokenize(file_path):
    input_text = open(file_path).read()
    tokenizer = moses.MosesTokenizer()
    tokens = tokenizer.tokenize(input_text.decode('utf8'))
#    tokens = nltk.word_tokenize(input_text.decode('utf8'))
    return set([x.encode('utf-8') for x in tokens])

def main():
    po = polib.POFile("", encoding="utf-8")
    po.metadata = PO_METADATA
    file_path = sys.argv[1]
    tokens = tokenize(file_path)
    for t in tokens:
        entry = polib.POEntry(
            msgid=unicode(t, 'utf-8'),
            msgstr=u'',
            )
        po.append(entry)
    po.save(file_path+".po")
