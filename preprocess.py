import nltk
import string

def FileRead(filePath):  
    f = open(filePath)  
    raw=f.read()  
    return raw

def SenToken(raw):
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')  
    sents = sent_tokenizer.tokenize(raw)  
    return  sents  

def CleanLines(line):
    cleanLines=[]
    for i in line:
        identify = string.maketrans('', '')  
        delEStr = string.punctuation +string.digits
        cleanLine = i.translate(identify,delEStr) 
        cleanLines.append(cleanLine)
    return cleanLines

def WordTokener(sents): 
    wordsInStr=[]
    for sent in sents:
        wordsInStr+=(nltk.word_tokenize(sent))
    return wordsInStr

def CleanWords(wordsList):
    cleanWords=[]
    
    from nltk.corpus import stopwords
    english_stopwords = stopwords.words('english')
    from nltk.stem.lancaster import LancasterStemmer
    st = LancasterStemmer()
    
    #english_punctuations = [',', '.', ':', ';', '?', '!', '(', ')', '[', ']','{','}' ,'&', '*', '@', '#', '$', '%']
    for words in wordsList:
        if words.lower() not in english_stopwords:
            cleanWords.append(st.stem(words.lower()))
    return cleanWords

if __name__ == '__main__':
    raw=FileRead("19.")
    t1=SenToken(raw)
    t1=CleanLines(t1)
    t1=WordTokener(t1)
    t1=CleanWords(t1)
    print t1