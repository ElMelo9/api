import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

nltk.download("punkt")
nltk.download("stopwords")

class SummaryText:
    # Función para limpiar el texto y dividirlo en oraciones
    def read_article(self,text):
        sentences = nltk.sent_tokenize(text)
        return sentences

# Función para calcular la matriz de similitud entre oraciones
    def sentence_similarity(self,sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []
    
        sent1 = [word for word in sent1 if word not in stopwords]
        sent2 = [word for word in sent2 if word not in stopwords]

        all_words = list(set(sent1 + sent2))

        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)

        for word in sent1:
            vector1[all_words.index(word)] += 1

        for word in sent2:
            vector2[all_words.index(word)] += 1

        return 1 - cosine_distance(vector1, vector2)

# Función para construir la matriz de similitud entre oraciones
    def build_similarity_matrix(self,sentences, stop_words):
        similarity_matrix = np.zeros((len(sentences), len(sentences)))

        for i in range(len(sentences)):
            for j in range(len(sentences)):
                if i == j:
                    continue
                similarity_matrix[i][j] = self.sentence_similarity(sentences[i], sentences[j], stop_words)

        return similarity_matrix

# Función para generar el resumen del texto
    def generate_summary(self,text, num_sentences):
        stop_words = set(stopwords.words("english"))
        sentences = self.read_article(text)
        sentence_similarity_matrix = self.build_similarity_matrix(sentences, stop_words)
    
        # Usar PageRank para obtener las oraciones más importantes
        sentence_scores = nx.pagerank(nx.from_numpy_array(sentence_similarity_matrix))
    
        # Ordenar las oraciones según sus puntuaciones en orden descendente
        ranked_sentences = sorted(((sentence_scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)

        # Tomar las mejores 'num_sentences' oraciones como resumen
        summary = " ".join([sentence for _, sentence in ranked_sentences[:num_sentences]])
    
        return summary


