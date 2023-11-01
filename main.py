from bs4 import BeautifulSoup
from argparse import ArgumentParser


def copy_content(args):
    with open(args, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    with open('result.html', 'a') as fp:
        fp.write(soup.prettify())


def find_links(args):
    with open(args, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    with open('result.txt', 'a') as fp:
        for link in soup.find_all('a', href=True):
            fp.write(link['href'] + '\n')


parser = ArgumentParser()
subparser = parser.add_subparsers(required=True)

parser_html = subparser.add_parser('html', help="Writes the html document into result.html")
parser_html.add_argument('-f', type=str, dest="filename")
parser_html.set_defaults(func=copy_content)

parser_links = subparser.add_parser('links', help="Extracts links from the documents and writes them into result.txt")
parser_links.add_argument('-l', type=str, dest="filename")
parser_links.set_defaults(func=find_links)



if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args.filename)
