from analytics import (
    calculate_engagement_rate,
    compare_video_performance,
    classify_video_performance,
    classify_title_length,
)


def test_calculate_engagement_rate():
    result = calculate_engagement_rate(1000, 100, 50)
    assert result == 15.0


def test_engagement_rate_with_zero_views():
    result = calculate_engagement_rate(0, 100, 50)
    assert result == 0.0


def test_compare_video_performance():
    result = compare_video_performance(150000, 100000)
    assert result == 50.0


def test_classify_video_performance():
    result = classify_video_performance(50)
    assert result == "destaque"


def test_classify_title_length():
    result = classify_title_length(
        "TESTANDO UM NOVO SISTEMA PARA ANALISAR VÍDEOS"
    )
    assert result == "ideal"
