import httplib2
from bs4 import BeautifulSoup
from argparse import ArgumentParser

http = httplib2.Http()

def copy_content(uri, out):
    status, response = http.request(uri, "GET") 
    soup = BeautifulSoup(response, 'html.parser')
    with open(out, 'a') as fp:
        fp.write(soup.prettify())


def find_links(uri, out):
    status, response = http.request(uri, "GET") 
    soup = BeautifulSoup(response, 'html.parser')
    with open(out, 'a') as fp:
        for link in soup.find_all('a', href=True):
            fp.write(link['href'] + '\n')

def find_img(uri, out):
    status, response = http.request(uri, "GET") 
    soup = BeautifulSoup(response, 'html.parser')
    with open(out, 'a') as fp:
        for img in soup.find_all('img'):
            fp.write(img['src'] + '\n')

parser = ArgumentParser()
subparser = parser.add_subparsers(required=True)

parser_html = subparser.add_parser('html', help="Writes the html document into result.html")
parser_html.add_argument('-l', type=str, dest="url", help="Specify the link")
parser_html.add_argument('-o', type=str, dest="output_file", help="Name of the output file")
parser_html.set_defaults(func=copy_content)

parser_links = subparser.add_parser('links', help="Extracts images from the documents and writes them into result.txt")
parser_links.add_argument('-l', type=str, dest="url", help="Specify the link")
parser_links.add_argument('-o', type=str, dest="output_file", help="Name of the output file")
parser_links.set_defaults(func=find_links)

parser_images = subparser.add_parser('images', help="Extracts links from the documents and writes them into result.txt")
parser_images.add_argument('-l', type=str, dest="url", help="Specify the link")
parser_images.add_argument('-o', type=str, dest="output_file", help="Name of the output file")
parser_images.set_defaults(func=find_img)



if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args.url, args.output_file)
