# coding:utf-8

from os import path
import sys
import jieba
from wordcloud import WordCloud, STOPWORDS

ExcludeWord = ['我', '你', '了', '的', '是', '吧', '吗', '在', '不', '都', '就', 
               '没', '有', '也', '又', '他', '她', '们', '和', '为', '到', '还',
               '但', '被', '会', '这', '并', '一个', '能', '个', '要', '而']

def word_segment(text):
  jieba_word = jieba.cut(text, cut_all = False)
  seg_list = ' '.join(jieba_word)
  open("wordcount/input/jieba_result.txt", "w", encoding = 'UTF8').write(seg_list)
  return seg_list

def generate_wordcloud(text):
  font_path = path.join("./fonts/msyh.ttf")
  stopwords = set(STOPWORDS)
  wc = WordCloud(
          background_color = "white",
          max_words = 200, 
          width = 1080,
          height = 768,
          min_font_size = 10,
          relative_scaling = 0.5,
      #    mask = alice_mask,
          stopwords = stopwords,
          font_path = font_path,
          repeat = False,
                )

  wc.generate(text)
  _output = "wordcloud.png"
  wc.to_file(_output)

if __name__=='__main__':
  _file = "wordcount/input/KFCDataSet.txt"
  text = open(_file, encoding = 'UTF8').read()
  for x in ExcludeWord:
    text = text.replace(x, " ")
  text = word_segment(text)
  generate_wordcloud(text)