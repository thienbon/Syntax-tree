from tkinter import *
from tkinter import filedialog
import regex
import nltk 
grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> PROPERN | DET NOM | PRON
  VP -> ADVP V NP PP | V VP | V NP | ADVP V NP | V NP NP| V PP
  ADVP -> ADV
  PP -> P NP
  DET -> Q | CD
  ADJP -> ADJ | ADVP ADJ| ADJ ADVP
  NOM -> N | N N ADJP | UN N

  PROPERN -> 'nam' | 'lan' | 'Nam' | 'Lan'
  PRON -> 'nó' | 'Nó'
  V -> 'đọc' | 'thích' | 'có' | 'mua' | 'tặng'|'ở' | 'ate' | 'eat' | 'saw' 
  P -> 'ở'
  N -> 'sách' | 'thư_viện' |'cuốn' | 'bread'
  UN -> 'cuốn'
  Q -> 'nhiều'
  ADV -> 'rất' | 'mới' | 'đang' | 'hay' |'mua'
  ADJ -> 'hay' | 'mới'| 'nhiều'
  CD -> 'một' | 'hai'

"""
)
  #S -> NP VP
  #PP -> P NP
  #NP -> Det N | Det N PP | 'I'
  #VP -> V NP | VP PP
  #Det -> 'an' | 'my'
  #N -> 'elephant' | 'pajamas'
  #V -> 'shot'
  #P -> 'in'
#nltk.app.rdparser()
#nltk.app.srparser()
root = Tk()
root.title('Parse tree')
root.geometry("500x650")
def open_txt():
    text_file = open("D:/text/text.txt",'r',encoding = "utf8")
    stuff = text_file.read()
    my_text.insert(END,stuff)
    text_file.close()
def save_txt():
    text_file = open("D:/text/text.txt",'w' , encoding = "utf8")
    text_file.write(my_text.get(1.0, END))
def parse_txt():
    text_file = open("D:/text/text.txt",'r' , encoding = "utf8")
    Lines=text_file.readlines()
    for line in Lines:
        sentence = line.split()
        print(sentence)
        def parse(sent):
            a = []
            parser = nltk.ChartParser(grammar)
            for tree in parser.parse(sent):
                a.append(tree)
                return(a[0])
        print(parse(sentence))


my_text = Text(root, width=40, height=10, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black")
my_text.pack()
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(pady=20)
save_button = Button(root , text = "Save Text" , command = save_txt)
save_button.pack(pady=20)
parse_button = Button(root , text = "Parse" , command = parse_txt )
parse_button.pack(pady=20)
root.mainloop()
