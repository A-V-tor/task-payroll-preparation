#!/usr/bin/env python3
import os
import json
import logging

from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from dotenv import find_dotenv, load_dotenv
from task_payroll_preparation import collection
from pipline import get_pipeline
from other import get_freq_for_pandas, get_dates_list_for_check

load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('token'))
dp = Dispatcher(
    bot,
)


@dp.message_handler(Text(startswith=['{']))
async def send_data(message: types.Message):
    json_message = json.loads(message.text)

    beginning_of_period = datetime.strptime(
        json_message.get('dt_from'), '%Y-%m-%dT%H:%M:%S'
    )
    end_of_period = datetime.strptime(
        json_message.get('dt_upto'), '%Y-%m-%dT%H:%M:%S'
    )
    period = json_message.get('group_type')

    freq = get_freq_for_pandas(period)
    pipeline = get_pipeline(beginning_of_period, end_of_period, period)

    list_dates = []
    list_values = []
    result = list(collection.aggregate(pipeline))
    for i in result:
        list_dates.append(i['_id'])
        list_values.append(i['total_value'])

    dates = get_dates_list_for_check(
        json_message.get('dt_from'), json_message.get('dt_upto'), freq
    )

    for i, k in enumerate(dates):
        if k not in list_dates:
            list_dates.insert(i, k)
            list_values.insert(i, 0)

    await message.reply({'dataset': list_values, 'labels': list_dates})


executor.start_polling(dp, skip_updates=True)
