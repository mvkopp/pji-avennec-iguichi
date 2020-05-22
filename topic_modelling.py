import nltk
import ssl

import spacy
from spacy.lang.en import English

import random

import xml.etree.cElementTree as ET

from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

import gensim
from gensim import corpora
import pickle

import pyLDAvis.gensim

def getTitlesFromDatabase () :
    """
    Return all authors from articles database

    :params : /
    :returns: (dict) dictionnary of all author with their infos
    """
    listTitles = []
    tree = ET.parse('articles_database.xml')
    root = tree.getroot()
    for article in root.findall('article') : 
        titleArticle = article.find('title').text
        listTitles.append(titleArticle)
    return listTitles 

def tokenize(text):
    parser = English()
    
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

def get_lemma(word):
    """
    """
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma


def get_lemma2(word):
    """
    """
    return WordNetLemmatizer().lemmatize(word)

def prepare_text_for_lda(text):
    """
    """
    en_stop = set(nltk.corpus.stopwords.words('english'))
    
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

def main():
    """
    """
    #spacy.load('en')
    nltk.download('stopwords')
    nltk.download('wordnet')
    
    text_data = []

    print('Start to get titles...')
    listTitles=getTitlesFromDatabase()
    print('Titles recovered : ',len(listTitles))
    #for title in listTitles:
    #    tokens = prepare_text_for_lda(title)
    #    if random.random() > .99:
    #        print(tokens)
    #        text_data.append(tokens)

    text_data=[['dependency', 'weight', 'aggregation', 'factorize', 'database'],
['expressive', 'power', 'global', 'local', 'priority', 'process', 'calculus'],
['graph', 'analysis', 'fragment', 'bacterial', 'genome', 'assembly'],
['parallel', 'multiple', 'pattern', 'match'],
['resource', 'frugal', 'probabilistic', 'dictionary', 'application', 'bioinformatics'],
['smart', 'devices', 'manufacturing', 'equipment'],
['switching', 'estimation', 'active', 'recognition', 'using', 'projection', 'method'],
['actuator', 'failure', 'compensation', 'link', 'mobile', 'robot', 'base', 'multiple', 'model', 'control'],
['implementation', 'base', 'localization', 'system', 'intelligent', 'vehicle'],
['horizontal', 'vertical', 'aid', 'vehicle', 'localization', 'urban', 'environment'],
['tirapazamine', 'sr-4233', 'combine', 'radiation', 'platinum', 'cytotoxicity', 'vitro', 'human', 'line'],
['railway', 'direct', 'brake', 'system', 'analysis', 'using', 'hybrid', 'graph'],
['graph', 'modeling', 'fault', 'diagnosis', 'continuous', 'stir', 'reactor', 'study'],
['graph', 'online', 'robust', 'diagnosis', 'application', 'hydraulic', 'system'],
['study', 'career', 'adaptability', 'engagement', 'online', 'teacher', 'education', 'industry'],
['design', 'dependable', 'system', 'architecture', 'railroad', 'smart', 'wagon', 'using', 'share', 'function'],
['smew', 'smart', 'mobile', 'embed', 'server'],
['add', 'recursion'],
['model', 'design', 'heterogeneous', 'dynamically', 'reconfigurable'],
['architecture', 'design', 'language', 'multi', 'embed', 'control', 'system'],
['multi', 'periodic', 'synchronous', 'language'],
['scoped', 'extension', 'method', 'dynamically', 'type', 'language'],
['towards', 'scalable', 'blockchain', 'analysis'],
['matrix', 'formulation', 'shape', 'motion', 'application', 'depression', 'severity', 'assessment'],
['bimodal', '2d-3d', 'recognition', 'using', 'stage', 'fusion', 'strategy'],
['specification', 'synthesis'],
['security', 'robustness', 'constraint', 'spread', 'spectrum', 'tardos', 'fingerprinting'],
['comparison', 'diversification', 'method', 'solve', 'quadratic', 'assignment', 'problem'],
['integrate', 'shift', 'scheduling', 'assignment', 'optimization', 'attend', 'delivery'],
['managerial', 'analysis', 'urban', 'parcel', 'delivery', 'business', 'approach'],
['iterate', 'local', 'search', 'multi', 'commodity', 'multi', 'vehicle', 'route', 'problem', 'windows'],
['heuristic'],
['mine_{clust}$$', 'framework', 'multi', 'objective', 'clustering'],
['visualise', 'search', 'landscape', 'triangle', 'program'],
['route', 'planning', 'public', 'transportation', 'system'],
['novel', 'approach', 'base', 'distribute', 'dynamic', 'graph', 'modeling', 'subdivision', 'process', 'distribute', 'optimize', 'carpooling', 'request'],
['update', 'problem'],
['efficient', 'inclusion', 'check', 'deterministic', 'automaton', 'schema'],
['learning', 'regular', 'language', 'using', 'rfsas'],
['equivalence', 'deterministic', 'nest', 'transducer'],
['learning', 'positive', 'unlabeled', 'example'],
['constraint', 'automaton'],
['institutional', 'investor', 'beneficial', 'family', 'performance', 'evidence', 'french', 'stock', 'exchange'],
['explore', 'nonlinear', 'effects', 'family', 'involvement', 'board', 'entrepreneurial', 'orientation'],
['world', 'implementation', 'belief', 'function', 'theory', 'detect', 'dislocation', 'material', 'construction'],
['invent', 'mediterranean', 'harmony', 'matisse', 'paper'],
['determinantal', 'point', 'process', 'monte', 'carlo', 'integration'],
['adaptive', 'importance', 'sampling', 'present', 'future'],
['basis', 'expansion', 'natural', 'actor', 'critic', 'method'],
['algorithme', 'composition', 'musicale'],
['corbaweb', 'generic', 'object', 'navigator'],
['analysis', 'posture', 'movement', 'climbing', 'application', 'testing', 'boot'],
['testing', 'habit', 'developer', 'study', 'large', 'company'],
['software', 'metrics', 'predict', 'health', 'project', 'assessment', 'major', 'company'],
['grzegorz', 'rossolinski', 'liebe', 'stepan', 'bandera', 'afterlife', 'ukrainian', 'nationalist', 'fascism', 'genocide'],
['evolutive', 'component', 'base', 'method', 'agile', 'development', 'service', 'orient', 'architecture'],
['query', 'answer', 'transitive', 'linear', 'order'],
['regularity', 'property', 'differential', 'polynomial', 'modulo', 'regular', 'differential', 'chains'],
['parallel', 'sparse', 'factorization', 'modulo'],
['sparse', 'gaussian', 'elimination', 'modulo', 'update'],
['simulation', 'base', 'optimal', 'motion', 'planning', 'deformable', 'object'],
['fault', 'detection', 'diagnosis', 'using', 'parameter', 'estimation', 'recursive', 'least', 'square'],
['interval', 'observer', 'class', 'uncertain', 'nonlinear', 'singular', 'system'],
['research', 'performance', 'shipboard', 'command', 'control', 'system', 'base'],
['brain', 'computer', 'interface', 'augment', 'reality', 'state'],
['topology', 'drive', 'hierarchical', 'segmentation'],
['sound', 'characterisation', 'method'],
['réduire', 'l’arbitraire', 'négociation', 'quitte', 'concéder'],
['multiparty', 'argumentation', 'consensual', 'expansion', 'apply', 'evidence', 'base', 'medicine'],
["d'argumentation", 'multi', 'party', "l'enrichissement", 'consensuel', 'présentation', 'courte']]    

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')

    NUM_TOPICS = 10
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model10.gensim')
    topics = ldamodel.print_topics(num_words=4)
    print('Display topic ...')
    for topic in topics:
        print(topic)

    dictionary = gensim.corpora.Dictionary.load('dictionary.gensim')
    corpus = pickle.load(open('corpus.pkl', 'rb'))
    lda = gensim.models.ldamodel.LdaModel.load('model10.gensim')

    lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
    pyLDAvis.display(lda_display)

if __name__ == "__main__":
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    main()
