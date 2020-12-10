from atom_tag_pairing import Atom_Tag_Pairing
from atom_embedding import Atom_Embedder
from Atom_FFNN import Atom_FFNN
from Atom_RNN import Atom_RNN
from word_embedding_ricocorpus import word_embedding_ricocorpus
from word_embedding import Sciart_Word_Embedding

from Process_sciart import Process_Sciart
from Label_Text_Builder import Label_Text_Builder
from Processing import Tex_Processing

# PIMS filter import

import pickle
import os
import tensorflow as tf
from tensorflow import keras
import keras.layers as layers

class Learn_Master():
    """

    """
    def __init__(self, dataset, neural_network, dataset_type=None, NNmodel_path='', WEmodel_path='', vocab_save_path='', data_save_path=''):
        """

        :param neural_network: Either 'ffnn' for feed-forward neural network or 'rnn' for recurrent neural network
        :param word_embedding: Either
        :param model:
        """
        self.neural_network = neural_network




        self.vocab_save_path = vocab_save_path
        self.data_save_path = data_save_path


        if dataset_type == 'tex':
            self.tex_files = dataset  # list of tex files to be cleaned

        else:
            self.data = dataset

    def create_tex_dataset(self):
        LTB = Label_Text_Builder(self.tex_files, self.vocab_save_path, self.data_save_path)
        LTB.main()

        Process_tex = Tex_Processing(self.train_data_path, self.test_data_path)
        Process_tex.main(self.train_vecs_path, self.test_vecs_path)


    def create_dataset(self):
        data_path = r'dataset.pkl'
        PS = Process_Sciart(self.dataset, data_path, vocabfile=self.vocab_file)
        PS.main()


    def build_word_embedding(self, data, we_batch_size, embed_dim, save_we_model_path, vocab_path, we_model_path=''):
        Word_Embed = Sciart_Word_Embedding(data, batch_size=we_batch_size, embedding_dim=embed_dim,
                                           save_model_path=save_we_model_path, vocab_path=self.vocab_save_path, model_path=we_model_path)
        Word_Embed.main()

    def import_word_embedding(self, we_model, dataset):
        Word_Embed = Sciart_Word_Embedding(dataset)












