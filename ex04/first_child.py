import sys
from random import randint


class Research:
    def __init__(self, path, has_header=True):
        self.has_header = has_header
        self.path = path

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
        return csv_info

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            return [sum(map(lambda x: x[i], self.data)) for i in range(2)]

        @staticmethod
        def fractions(head, tail):
            summ = head + tail
            return head / summ * 100, tail / summ * 100

    class Analytics(Calculations):
        @staticmethod
        def pred_random(count):
            return [{0: [0, 1], 1: [1, 0]}[randint(0, 1)] for _ in range(count)]

        def predict_last(self):
            return self.data[-1]


def main():
    if len(sys.argv) != 3 or sys.argv[2] not in ('False', 'True'):
        sys.exit()
    file_rep = Research(sys.argv[1], {'False': False, 'True': True}[sys.argv[2]])
    try:
        file_data = file_rep.file_nest()
        analytics = file_rep.Analytics(file_data)
        counts = analytics.counts()
        percents = analytics.fractions(*counts)
        rand = analytics.pred_random(3)
        last = analytics.predict_last()
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    except AssertionError:
        print('Invalid file')
        sys.exit()
    except:
        sys.exit()

    print(file_data)
    print(*counts)
    print(*percents)
    print(rand)
    print(last)


if __name__ == '__main__':
    main()
