from analytics import (
    calcular_taxa_engajamento,
    comparar_desempenho_video,
    classificar_desempenho_video,
    classificar_tamanho_titulo,
)


def test_calculo_taxa_engajamento():
    resultado = calcular_taxa_engajamento(1000, 100, 50)
    assert resultado == 15.0


def test_taxa_engajamento_com_zero_visualizacoes():
    resultado = calcular_taxa_engajamento(0, 100, 50)
    assert resultado == 0.0


def test_comparacao_desempenho_video():
    resultado = comparar_desempenho_video(150000, 100000)
    assert resultado == 50.0


def test_classificacao_desempenho_video():
    resultado = classificar_desempenho_video(50)
    assert resultado == "destaque"


def test_classificacao_tamanho_titulo():
    resultado = classificar_tamanho_titulo(
        "TESTANDO UM NOVO SISTEMA PARA ANALISAR MEUS VÍDEOS"
    )
    assert resultado == "ideal"


def test_classificacao_titulo_curto():
    resultado = classificar_tamanho_titulo("NOVO VÍDEO")
    assert resultado == "curto"


def test_classificacao_titulo_longo():
    titulo_longo = "A" * 71
    resultado = classificar_tamanho_titulo(titulo_longo)
    assert resultado == "longo"
