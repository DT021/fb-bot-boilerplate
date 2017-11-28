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
        return "Hello World!"
