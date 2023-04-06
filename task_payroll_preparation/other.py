import pandas as pd


def get_freq_for_pandas(period):
    if period == 'month':
        freq = None
    if period == 'day':
        freq = 'D'
    if period == 'hour':
        freq = 'H'
    return freq


def get_dates_list_for_check(start, end, freq):
    date_range = pd.date_range(
        start=start,
        end=end,
        freq=freq,
    )
    return [d.isoformat() for d in date_range]
