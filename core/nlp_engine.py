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
        label = "label"
        return label

    def what_i_mean(self, label):
        """
        This method is in charge to map a label into an natural language answer
        :param label:
        :return: string
        """
        answer = {"label": "This is my answer!"}
        return answer[label]
