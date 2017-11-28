from itertools import cycle


def map_nlp_config_to_dic(dict_conf):
    """
    map nlp_config to usable dic for nlp analysis
    :param dict_conf:
    :return:
    """
    sentence_dic = {}

    for question in dict_conf:
         sentence_dic.update(dict(zip(dict_conf[question], cycle([question]))))

    return sentence_dic


def concat_nlp_config(dict_conf):
    """
    Concat all the lists in a nlp_config dictionary
    :param dict_conf:
    :return:
    """
    sentence_list = []
    for question in dict_conf:
        sentence_list.extend(dict_conf[question])
    return sentence_list
