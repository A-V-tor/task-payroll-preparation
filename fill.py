import os
from task_payroll_preparation import collection
import bson


BASEDIR = os.path.join(
    os.path.dirname(__file__), 'sampleDB/sample_collection.bson'
)


def fill_db():
    try:
        with open(BASEDIR, 'rb') as f:
            data = bson.decode_all(f.read())

        collection.insert_many(data)
        return 'Готово'

    except Exception as e:
        return str(e)


if __name__ == '__main__':
    fill_db()
