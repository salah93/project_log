#! /usr/local/bin/python
from argparse import ArgumentParser
from datetime import datetime


def pr_logger(text, htag=4):
    return make_template(datetime.now(), text, htag)


def make_template(header, body, htag=1):
    return ("#" * int(htag) + " {header}\n{body}\n\n").format(
                header=header, body=body)


if __name__ == "__main__":
    parser = ArgumentParser(
        description='Log updates with current time')
    parser.add_argument('content', metavar='CONTENT')
    parser.add_argument(
        '-t', metavar='HEAD_TAG', nargs='?',
        default=4, choices=[1, 2, 3, 4], type=int,
        help='the header tag used')
    args = parser.parse_args()
    print(pr_logger(args.content, args.t))
