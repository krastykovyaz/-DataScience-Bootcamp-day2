from analytics import Research
from config import NUM_OF_STEPS, REPORT_FILENAME
import sys


def make_report(filename, has_header):
    research = Research(filename, has_header)
    try:
        analytics = research.Analytics(research.file_nest())
        counts = analytics.counts()
        rand = analytics.pred_random(NUM_OF_STEPS)
        analytics_rand = research.Analytics(rand)
        counts_rand = analytics_rand.counts()
        percents = analytics_rand.fractions(*counts)
        line = (f'We have made {len(analytics.data)} observations of tossing a coin: '
                f'{counts[0]} of them were tails and {counts[1]} of them were heads. '
                f'The probabilities are {round(percents[0], 2)}% and {round(percents[1], 2)}%, respectively. '
                f'Our forecast is that in the next {NUM_OF_STEPS} '
                f'observations we will have: {counts_rand[0]} tail and {counts_rand[1]} heads.')
        analytics.save_file(line, REPORT_FILENAME)
        research.send_message('The report has been successfully created')
    except Exception as e:
        research.send_message('The report hasn’t been created due to an error')
        raise e


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[2] not in ('False', 'True'):
        print(sys.argv[2])
        sys.exit()
    try:
        make_report(sys.argv[1], {'False': False, 'True': True}[sys.argv[2]])
        sys.exit()
    except FileNotFoundError:
        print('File not found')
        sys.exit()
    except AssertionError:
        print('Invalid file')
        sys.exit()
    except:
        sys.exit()
