class Research:
    def file_reader(self, filename):
        with open(filename, 'r') as f:
            text = f.read()
        return text


if __name__ == '__main__':
    ex = Research()
    print(ex.file_reader('data.csv'))
