from random import randint
import logging
from config import BASE_LOGGING_LEVEL, TOKEN, EXTENSION, ID
import os
import requests


logging.basicConfig(filename='analytics.log', level=BASE_LOGGING_LEVEL,
                    format='%(asctime)s,%(msecs)03d %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class Research:
    def __init__(self, path, has_header=True):
        self.has_header = has_header
        self.path = path
        logging.info(f'File {path} research started')

    def send_message(self, message):
        print(message)
        tg_url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={message}'.replace(' ', '+')
        requests.post(tg_url)

    def file_nest(self):
        with open(self.path) as f:
            file_data = f.read()

            file_iter = iter(file_data.split('\n'))
            if self.has_header:
                next(file_iter)
            csv_info = []
            is_empty = True
            for row in file_iter:
                is_empty = False
                assert row in ('1,0', '0,1')
                csv_info.append([int(i) for i in row.split(',')])
            assert not is_empty

        logging.info('Read data success')
        return csv_info

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info('Calculating started')

        def counts(self):
            res = [sum(map(lambda x: x[i], self.data)) for i in range(2)]
            logging.info(f'Counting info {len(self.data)} observations')
            return res

        @staticmethod
        def fractions(head, tail):
            summ = head + tail
            logging.info('Percents calculating')
            return head / summ * 100, tail / summ * 100

    class Analytics(Calculations):
        @staticmethod
        def pred_random(count):
            logging.info('Random data generate ...')
            return [{0: [0, 1], 1: [1, 0]}[randint(0, 1)] for _ in range(count)]

        def predict_last(self):
            logging.info('Get last predict')
            return self.data[-1]

        @staticmethod
        def save_file(data, filename):
            with open(os.path.splitext(filename)[0] + EXTENSION, 'w') as f:
                f.write(str(data))
