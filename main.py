from bs4 import BeautifulSoup

files = 'index.html'


def copy_content(file):
    with open(file, 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    with open('result.html', 'a') as file:
        file.write(soup.prettify())


# def scraper():
#     with open('index.html', 'r') as fp:
#         soup = BeautifulSoup(fp, 'html.parser')
#     with open('result.html', 'a') as file:
#         file.write(soup.prettify())


if __name__ == '__main__':
    print("Welcome to pyscraper, please enter the filename: ")
    copy_content(input())
