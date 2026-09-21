def calculate_engagement_rate(views, likes, comments):
    """
    Calcula a taxa de engajamento de um conteúdo com base
    em visualizações, curtidas e comentários.
    """
    if views <= 0:
        return 0.0

    engagement_rate = ((likes + comments) / views) * 100
    return round(engagement_rate, 2)
