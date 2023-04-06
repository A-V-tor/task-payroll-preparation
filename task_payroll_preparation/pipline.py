def get_pipeline(beginning_of_period, end_of_period, period):
    """ Конвеер агрегации данных.

    Args:
        beginning_of_period: начало периода агрегации
        end_of_period: конец периода агрегации данных
        period: еденица агрегации

    Returns:
        list: список для выполнения агрегации
    """
    lt = '$lt'
    if period == 'hour':
        date_format = '%Y-%m-%dT%H:00:00'
    if period == 'day':
        date_format = '%Y-%m-%dT00:00:00'
    if period == 'month':
        lt = '$lte'
        date_format = '%Y-%m-01T00:00:00'

    return [
        {
            '$match': {
                'dt': {
                    '$gte': beginning_of_period,
                    f'{lt}': end_of_period,
                }
            }
        },
        {
            '$project': {
                'date': {
                    '$dateToString': {
                        'format': f'{date_format}',
                        'date': '$dt',
                    }
                },
                'value': '$value',
            }
        },
        {'$group': {'_id': '$date', 'total_value': {'$sum': '$value'}}},
        {'$sort': {'_id': 1}},
    ]
