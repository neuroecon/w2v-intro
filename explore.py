import gensim
import os

output_path = os.path.join('.', 'vectors', 'w2v_fox')
if not os.path.exists(output_path):
    print('Fox vector couldn\'t be found. Did you run `python3 train.py`?')
    print('Exiting')
    exit()

vectors = gensim.models.Word2Vec.load(output_path)

print('Make sure to run this file interactively (python3 -i explore.py')

print(
"""
If the training worked properly, you should have your very own word2vec model!
I've loaded that model into the variable name `vectors` for you to play 
around with in the interpreter. Try out some of the following methods:

>>> vectors.similar_by_word('apple')
>>> vectors.similar_by_word('orange')

>>> vectors.wv['cat']
>>> vectors.similar_by_vector(vectors.wv['cat'])

>>> vectors.wv.similarity('car', 'bus')
>>> vectors.wv.similarity('car', 'carpet')

>>> vectors.similar_by_vector(vectors.wv['king'])
>>> vectors.similar_by_vector(vectors.wv['king'] - vectors.wv['man'] + vectors.wv['woman'])

These are just a few of the features of the gensim module. Check out
the documentation at https://radimrehurek.com/gensim/ for more details.
Alternatively, use help(vectors) in the interpreter and browse through
the available methods. 
"""
)