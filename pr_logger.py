#! /usr/local/bin/python
from argparse import ArgumentParser
from datetime import datetime


def pr_logger(text, htag='h4', btag='p'):
    return make_template(datetime.now(), text, htag, btag)


def make_template(header, body, htag='h1', btag='p'):
    return "<{htag}>{header}</{htag}><{btag}>{body}</{btag}>\n\n".format(
                header=header, body=body, htag=htag, btag=btag)


if __name__ == "__main__":
    parser = ArgumentParser(
        description='Log updates with current time')
    parser.add_argument('content', metavar='CONTENT')
    parser.add_argument(
        '-t', metavar='HEAD_TAG', nargs='?',
        choices=['h1', 'h2', 'h3', 'h4'],
        help='the header tag used')
    parser.add_argument(
        '-b', metavar='BODY_TAG', nargs='?',
        help='the tag of the content used')
    args = parser.parse_args()
    print(pr_logger(args.content, args.t, args.b))
