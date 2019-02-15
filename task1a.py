filename="Book1.txt"
file=open(filename,"r")

def unique_words(book):
   for line in book:
    line=line.strip()
      for word in line:    
         


def count_the_article(book3):
   count=0   
   words=["a", "the", "at", "run", "to","and","are","or","for","an","this"]  
   for line1 in book3:
      line=line.strip()
   for word in line1:
      for i in range(len(words)) 
        if word=words[i]:
          count=count+1
   print(count)
 

def sorted_words(book1):
   for line2 in book1:
      fields2 = line2.rstrip('\n').split('\t')
      fields2.sort()
      print fields2


def character_word_count(book2):
   tup1={}
   for line3 in book2:
      string=string.split()
   for word in string:
      print(tup1[word]=len(word)) 
