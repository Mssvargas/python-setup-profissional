from python_setup_profissional.main import saudacao


def test_saudacao_padrao():
    assert saudacao() == "Olá, mundo!"


def test_saudacao_com_nome():
    assert saudacao("Marlon") == "Olá, Marlon!"
