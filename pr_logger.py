#! /usr/local/bin/python
import sys
from datetime import datetime


def pr_logger(text):
    timestamp = datetime.now()
    html = """<h2>{0}</h2><code>{1}</code>""".format(timestamp, text)
    return html + '\n\n'


if __name__ == "__main__":
    lines = sys.argv[1]
    print(pr_logger(lines))
