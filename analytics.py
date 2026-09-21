def calculate_engagement_rate(views, likes, comments):
    """
    Calcula a taxa de engajamento de um conteúdo com base
    em visualizações, curtidas e comentários.
    """
    if views <= 0:
        return 0.0

    engagement_rate = ((likes + comments) / views) * 100
    return round(engagement_rate, 2)
def compare_video_performance(video_views, channel_average_views):
    """
    Compara as visualizações de um vídeo com a média de visualizações do canal.
    Retorna a diferença percentual.
    """
    if channel_average_views <= 0:
        return 0.0

    difference = ((video_views - channel_average_views) / channel_average_views) * 100
    return round(difference, 2)
def classify_video_performance(percent_difference):
    """
    Classifica o desempenho de um vídeo em relação à média do canal.
    """
    if percent_difference >= 50:
        return "destaque"
    elif percent_difference >= 10:
        return "acima da média"
    elif percent_difference > -10:
        return "na média"
    else:
        return "abaixo da média"
def classify_title_length(title):
    """
    Classifica o tamanho de um título com base na quantidade de caracteres.
    """
    length = len(title.strip())

    if length < 30:
        return "curto"
    elif length <= 70:
        return "ideal"
    else:
        return "longo"
