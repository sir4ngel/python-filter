from operator import index
import matplotlib.pyplot as plt 
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
from collections import Counter

class Nube:

    def crearNube(archivo, columna, numPalabras):

        # Palabras de la columna del archivo que se convertiran a string.
        palabras = ''

        # Definimos las stopwords
        stop_words_unicos = ['Ã', 'Â', 'ð','ðŸ', 'Ÿ', '€','@', '¢' ,'https', 'âœ' 'âœˆï','ˆ','Ÿ','â','œ','ï', 'estÃ','dÃ','mÃ', 'ä', 'https://t.co', 't', 'co', 'í', 'n' ]
        stop_words = stopwords.words('spanish')
        stop_words.extend(stop_words_unicos)

        # Leemos el  archivo pasado en el parametro.
        df = pd.read_csv(archivo, encoding='utf-8')


        listaPalabras = [ z.lower() for y in
                        [ x.split() for x in df[columna] if isinstance(x, str)]
                        for z in y]

        palabras = " ".join(listaPalabras)

        wordcloud = WordCloud(width=1000, height=1000,
                            background_color='white',
                            max_words=numPalabras,
                            stopwords=stop_words,
                            ).generate(palabras)
        return wordcloud
    
    def crearHistograma(archivo, columna, titulo):

        df = pd.read_csv(archivo, encoding='utf-8')

        palabras_usadas = [ z.lower() for y in
                       [ x.split() for x in df[columna] if isinstance(x, str)]
                       for z in y]

        word_count_dict = dict(Counter(palabras_usadas))

        popular_words = sorted(word_count_dict, key = word_count_dict.get, reverse = True)

        popular_words_nonstop = [w for w in popular_words if w not in stopwords.words("spanish")]
        
        plt.barh(range(20), [word_count_dict[w] for w in reversed(popular_words_nonstop[0:20])])
        plt.yticks([x + 0.5 for x in range(20)], reversed(popular_words_nonstop[0:20]))
        plt.title(titulo)
        plt.savefig('./Imagenes/grafica.png')