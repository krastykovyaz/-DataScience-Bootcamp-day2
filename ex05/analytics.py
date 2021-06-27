import sys
from random import randint


class Research:
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            return [sum(elem) for elem in zip(*self.data)]

        def fractions(self):
            first, second = self.counts()
            return [first / (first + second) * 100, second / (first + second) * 100]

    class Analytics(Calculations):
        def predict_random(self, num_steps):
            cases = {0: [0, 1], 1: [1, 0]}
            return [cases[randint(0, 1)] for _ in range(num_steps)]

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, filename, extension):
            with open(filename + extension, 'w') as f:
                f.write(data)

    def __init__(self, filename):
        self.filename = filename
        self.calc = self.Analytics(self.file_reader(filename))

    def file_reader(self, has_header=True):
        with open(self.filename, 'r') as f:
            text = f.read()
        lines = text.split('\n')
        if has_header and len(lines[0].split(',')) != 2:
            raise ValueError('Incorrect header')
        if has_header:
            lines = lines[1:]
        if not lines:
            raise ValueError('No lines')
        for line in lines:
            if line not in('1,0', '0,1'):
                raise ValueError('Incorrect line')
        return [[int(elem) for elem in line.split(',')] for line in lines]


if __name__ == '__main__':
    pass
