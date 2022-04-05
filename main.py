"""
Course Guide Retriever
Tommy Scheper

Supported for terms Fall 2021 and later.
"""
import os
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from args.cg_args import CGArgs
from specialprint import horizontal_align_print


# Change this if you want. If not you'll have to type it each time
FILE_PATH = ''

# If you're on Mac you shouldn't have to change this
CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

ENCODING = 'utf-8'
URL_START = 'https://www.lsa.umich.edu/cg/cg_results.aspx?'
XPATHS = {
    'num_pages_and_results': "//td[contains(text(), 'Results')]",
    'course_names': "//font[@style='font-weight:bold; font-size:14px;']"
}
MAX_COURSE_NAME_LENGTH = 12  # Longest course name example: ASIANPAM 214


def chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.binary_location = CHROME_PATH
    chrome_options.add_argument('--headless')
    return chrome_options


class CGRetriever:
    def __init__(self) -> None:
        self.filename: str = FILE_PATH or self.retrieve_filename()
        self.filename = self.filename[:-4]  # Chop off the .txt
        self.driver = webdriver.Chrome(options=chrome_options())
        self.cg_args = CGArgs()

    def retrieve_filename(self) -> str:
        while True:
            filename = input('Filename: ')
            if os.path.exists(filename):
                return filename
            print('File does not exist.')
    
    def get_elements(self, xpath) -> List[WebElement]:
        return self.driver.find_elements(By.XPATH, xpath)
    
    def get_element_text(self, xpath) -> str:
        return self.driver.find_element(By.XPATH, xpath).text
    
    def collect_args(self) -> None:
        with open(self.filename + '.txt', 'r', encoding=ENCODING) as fin:
            for line in fin:
                k, v = line.split(': ')
                v = v.rstrip()
                if v:
                    self.cg_args.add_arg(k, v)
    
    def make_url(self) -> str:
        return URL_START + self.cg_args.url_piece()
    
    def open_url(self, url) -> None:
        self.driver.get(url)
        print(f'Opened {url}')
    
    def grab_num_results(self) -> int:
        xpath = XPATHS['num_pages_and_results']
        try:
            return int(self.get_element_text(xpath).split()[-1])
        except NoSuchElementException:
            return 0
    
    def change_show(self, show: int) -> None:
        self.cg_args.set_show(str(show))
        self.open_url(self.make_url())
    
    def fetch_courses(self, url) -> None:
        self.open_url(url)

        with open(self.filename + '-out.txt', 'w', encoding=ENCODING) as fout:
            num_results = self.grab_num_results()
            # Ensure all results are shown on one page
            if num_results > self.cg_args.get_show_int():
                self.change_show(num_results)
            num_results = self.grab_num_results()
            print(f'{num_results} result(s) found (including duplicates)')

            prev_course = ''
            course_elts = self.get_elements(XPATHS['course_names'])
            for elt in course_elts:
                course = elt.text.split(' - ')[0]
                if course != prev_course:
                    horizontal_align_print(
                        course,
                        MAX_COURSE_NAME_LENGTH,
                        'right',
                        os=fout
                    )
                else:
                    num_results -= 1
                
                prev_course = course
            
            print(f'{num_results} unique course(s) found')

    def execute(self) -> None:
        self.collect_args()
        self.fetch_courses(self.make_url())
        self.driver.quit()
        print(f"Complete. Output in {self.filename + '-out.txt'}")


def main():
    cgr = CGRetriever()
    cgr.execute()


if __name__ == '__main__':
    main()
