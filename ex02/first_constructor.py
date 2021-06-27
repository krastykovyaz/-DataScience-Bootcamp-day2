import sys


class Research:
    def __init__(self, path):
        self.path = path

    def file_constructor(self):
        with open(self.path) as f:
            file_data = f.read()
            file_iter = iter(file_data.split('\n'))
            header: str = next(file_iter)
            assert len(list(filter(lambda x: x, header.split(',')))) == 2
            is_empty = True
            for row in file_iter:
                is_empty = False
                assert row in ('1,0', '0,1')
            assert not is_empty
        return file_data


def main():
    if len(sys.argv) != 2:
        sys.exit()
    file_rep = Research(sys.argv[1])
    try:
        print(file_rep.file_constructor())
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    except AssertionError:
        print('Invalid file')
        sys.exit()
    except:
        sys.exit()


if __name__ == '__main__':
    main()
