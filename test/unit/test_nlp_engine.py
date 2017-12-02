from core.nlp_engine import NLPEngine


def test_nlp_engine():
    engine = NLPEngine()
    assert engine.human_input("Buenas") == "greetings"
