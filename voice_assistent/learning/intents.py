import json
import nltk
import pathlib
import tensorflow as tf
import numpy as np
from common import utils
from nltk.stem import LancasterStemmer

ROOT_PATH = utils.get_root_path()


class Intents:
    def __init__(self):
        nltk.download('punkt')

        self.words_bag = []
        self.intents_bag = []
        self.intents = []
        self.sentences = []
        self.tags = []
        self.steammer = None
        self.model = None
        self.load_intents()
        self.set_content_based_on_intents()
        self.create_model()

    def create_model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Input(shape=(len(self.words_bag),)),
            tf.keras.layers.Dense(8),
            tf.keras.layers.Dense(8),
            tf.keras.layers.Dense(len(self.intents_bag), activation="softmax"),
        ])

        self.model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

    def load_intents(self) -> list():
        json_path = pathlib.Path(ROOT_PATH).joinpath("intents.json")
        with open(json_path) as intents_file:
            self.intents = json.load(intents_file)

    def set_content_based_on_intents(self) -> (list(), list()):
        all_words = []
        self.steammer = LancasterStemmer()
        for intent in self.intents:
            for pattern in intent["patterns"]:
                words = nltk.word_tokenize(pattern)
                words = [self.steammer.stem(word.lower()) for word in words]
                all_words.extend(words)
                self.sentences.append(words)
                self.tags.append(intent["intent"])
                words = []

        self.words_bag = sorted(list(set(all_words)))
        self.intents_bag = sorted(list(set(self.tags)))

    def get_features(self):
        features = []
        for sentence in self.sentences:
            feature = [0 for i in range(len(self.words_bag))]
            for idx, word in enumerate(self.words_bag):
                if word in sentence:
                    feature[idx] = 1
            features.append(feature)
        return np.array(features)

    def get_labels(self) -> list:
        labels = []
        for tag in self.tags:
            label = [0 for i in range(len(self.intents_bag))]
            label[self.intents_bag.index(tag)] = 1
            labels.append(label)
        return np.array(labels)
    
    def str_to_input(self, sentence):
        words_in_sentence = [self.steammer.stem(word.lower()) for word in sentence.split(" ")]
        feature = [0 for i in range(len(self.words_bag))]
        for idx, word in enumerate(self.words_bag):
            if word in words_in_sentence:
                feature[idx] = 1
        return np.array([feature])

    def train(self):
        features = self.get_features()
        labels = self.get_labels()
        self.model.fit(features, labels, epochs=500)
    
    def predict(self, sentence):
        feature = self.str_to_input(sentence)
        intents_predicts = self.model.predict(feature)[0]
        intent_idx = np.argmax(intents_predicts)
        if intents_predicts[intent_idx] > 0.75:
            return self.intents_bag[intent_idx]
        return None
