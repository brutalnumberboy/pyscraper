from bs4 import BeautifulSoup
from argparse import ArgumentParser


def copy_content(file):
    with open(file, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    with open('result.html', 'a') as fp:
        fp.write(soup.prettify())


def search_links(file):
    with open(file, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    with open('result.html', 'a') as fp:
        for link in soup.find_all('a'):
            fp.write(link.getText('href') + '\n')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--html", dest="filename",
                        help='Download an html file of the website', type=str)
    args = parser.parse_args()
    copy_content(args.filename)
