# -*- coding: utf-8 -*-
"""duygular_AIgalactica_preprocess_kodlar.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zw7-LNa1yUAfEBfcRy8zEpYA57s9LXdr
"""

#SADECE STEMMER KODU - kerem
import pandas as pd
from TurkishStemmer import TurkishStemmer

def stem_text(text):
    stemmer = TurkishStemmer()
    words = text.split()
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)

# Excel dosyasını oku
excel_path = '/content/on_islenmis_nlp_duygular_veriseti.xlsx'  # Dosya yolunu güncelleyin
df = pd.read_excel(excel_path)

# "Özet" sütununu stemmerdan geçir
df['comments'] = df['comments'].astype(str).apply(stem_text)

# "Tür" sütununu stemmerdan geçir (isteğe bağlı, eğer gerekliyse)
# df['Tür'] = df['Tür'].apply(stem_text)

# Sonucu yeni bir Excel dosyasına kaydet (isteğe bağlı)
output_excel_path = '/content/sample_data/duygular?stemmed.xlsx'
df.to_excel(output_excel_path, index=False)

# İşlem tamamlandı mesajı
print("Stemming işlemi tamamlandı. Sonuçlar:", df)

!pip install pandas
!pip install TurkishStemmer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import re
import warnings
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

import nltk
import re
# Excel dosyasını oku
file_path = "/content/drive/MyDrive/DogalDilİşlemeveDuygular/nlp_duygular_veriseti.xlsx"  # Dosya yolunu buraya ekleyin
data = pd.read_excel(file_path)

data

data.info()

label_counts = data["label"].value_counts()
print("Etiket türleri ve frekansları:")
print(label_counts)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import re
import warnings
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

import nltk
import re

nltk.download('stopwords')

WPT = nltk.WordPunctTokenizer()
stop_word_list = nltk.corpus.stopwords.words('turkish')

# Excel dosyasını oku
file_path = "/content/drive/MyDrive/DogalDilİşlemeveDuygular/nlp_duygular_veriseti.xlsx"  # Dosya yolunu buraya ekleyin
data = pd.read_excel(file_path)

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        u"\U0001F680-\U0001F6FF"  # Transport & Map Symbols
        u"\U0001F700-\U0001F77F"  # Alchemical Symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols & Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

def token(values):
    filtered_words = [word for word in values.split() if word not in stop_word_list]
    not_stopword_doc = " ".join(filtered_words)
    return not_stopword_doc

docs = data['comments']
docs = docs.map(lambda x: re.sub('[0123456789,\/…=.!?();:$|''*%&#"“’-]', '', str(x)))
docs = docs.map(lambda x: remove_emojis(x))
docs = docs.map(lambda x: x.lower())
docs = docs.map(lambda x: x.strip())
docs = docs.map(lambda x: token(x))
data['comments'] = docs
print(data.head(20))

# Ön işlenmiş veri setini yeni bir Excel dosyasına kaydet
output_file_path = "/content/drive/MyDrive/DogalDilİşlemeveDuygular/nlp_duygular_veriseti_on_islenmis.xlsx"  # Kaydetmek istediğiniz dosya yolu
data.to_excel(output_file_path, index=False)

print(f"Ön işlenmiş veri seti '{output_file_path}' olarak kaydedildi.")