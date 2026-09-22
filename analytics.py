def calcular_taxa_engajamento(visualizacoes, curtidas, comentarios):
    """
    Calcula a taxa de engajamento de um conteúdo com base
    em visualizações, curtidas e comentários.
    """
    if visualizacoes <= 0:
        return 0.0

    taxa_engajamento = ((curtidas + comentarios) / visualizacoes) * 100
    return round(taxa_engajamento, 2)


def comparar_desempenho_video(visualizacoes_video, media_visualizacoes_canal):
    """
    Compara as visualizações de um vídeo com a média de visualizações do canal.
    Retorna a diferença percentual.
    """
    if media_visualizacoes_canal <= 0:
        return 0.0

    diferenca = (
        (visualizacoes_video - media_visualizacoes_canal)
        / media_visualizacoes_canal
    ) * 100

    return round(diferenca, 2)


def classificar_desempenho_video(diferenca_percentual):
    """
    Classifica o desempenho de um vídeo em relação à média do canal.
    """
    if diferenca_percentual >= 50:
        return "destaque"
    elif diferenca_percentual >= 10:
        return "acima da média"
    elif diferenca_percentual > -10:
        return "na média"
    else:
        return "abaixo da média"


def classificar_tamanho_titulo(titulo):
    """
    Classifica o tamanho de um título com base na quantidade de caracteres.
    """
    tamanho = len(titulo.strip())

    if tamanho < 30:
        return "curto"
    elif tamanho <= 70:
        return "ideal"
    else:
        return "longo"
