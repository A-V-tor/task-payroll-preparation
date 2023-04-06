import pandas as pd


def get_freq_for_pandas(period):
    """
    Частота дат для pandas.

    Args:
        period (str): период для определения частоты

    Returns:
        freq (str): частота
    """
    if period == 'month':
        freq = None
    if period == 'day':
        freq = 'D'
    if period == 'hour':
        freq = 'H'
    return freq


def get_dates_list_for_check(start, end, freq):
    """
    Получение списка дат для последующего сравнения и проверки.

    Args:
        start: начало периода
        end: конец периода
        freq: частота периода

    Returns:
        list: список дат заданного периода
    """
    date_range = pd.date_range(
        start=start,
        end=end,
        freq=freq,
    )
    return [d.isoformat() for d in date_range]
