import sys


class Research:
    class Calculations:
        def counts(self, data):
            return [sum(elem) for elem in zip(*data)]

        def fractions(self, data):
            first, second = self.counts(data)
            return [first / (first + second) * 100, second / (first + second) * 100]

    def __init__(self, filename):
        self.filename = filename
        self.calc = self.Calculations()

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
    if len(sys.argv) == 2:
        reader = Research(sys.argv[1])
        data = reader.file_reader()
        print(data)
        first, second = reader.calc.counts(data)
        print(first, second)
        first, second = reader.calc.fractions(data)
        print(first, second)
