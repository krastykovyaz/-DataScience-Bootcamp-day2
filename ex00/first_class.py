class Must_read():
    def __init__(self, filename):
        with open(filename, 'r') as f:
            print(f.read())


if __name__ == '__main__':
    Must_read('data.csv')
