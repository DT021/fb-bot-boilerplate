from fuzzywuzzy import process

from core.nlp_config.questions import questions_patterns
from core.nlp_config.answers import answers_patterns
from core.utils.nlp_utils import map_nlp_config_to_dic, concat_nlp_config


class NLPEngine(object):
    def __init__(self):
        pass

    def echo(self, message):
        """
        Simple method for testing purpose. Echo method return what it get.
        :param message: string
        :return: string message
        """
        return "You said: {}".format(message)

    def think(self, message):
        """
        This method is in charge to run all the nlp pipe
        :param message: string
        :return: string
        """
        label = self.what_do_you_mean(message)
        return self.what_i_mean(label)

    def what_do_you_mean(self, message):
        """
        This method map a string into an action
        :param message: string
        :return: label
        """
        label_dic = map_nlp_config_to_dic(questions_patterns)
        question = process.extractOne(message, concat_nlp_config(questions_patterns))
        label = label_dic[question[0]]
        return label

    def what_i_mean(self, label):
        """
        This method is in charge to map a label into an natural language answer
        :param label:
        :return: string
        """
        #return answers_patterns[label]
        return label
