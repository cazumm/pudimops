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
