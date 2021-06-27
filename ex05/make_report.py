from config import *
from analytics import Research

if __name__ == '__main__':
    reader = Research(filename)
    heads, tails = reader.calc.counts()
    heads_proba, tails_proba = reader.calc.fractions()

    pred = reader.calc.predict_random(num_steps)
    heads_random, tails_random = [sum(elem) for elem in zip(*pred)]

    report = template.format(
        len(reader.file_reader()),
        heads, tails,
        heads_proba, tails_proba,
        num_steps,
        heads_random, tails_random
    )
    reader.calc.save_file(report, report_filename, report_extention)
