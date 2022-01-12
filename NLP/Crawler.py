import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException, NoSuchElementException
from selenium.webdriver.common.by import By


class Crawler:
    def __init__(self, username, password, start_date='', end_date='', num=0):
        self.url = 'https://wenshu.court.gov.cn/'
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.start_date = start_date
        self.end_date = end_date
        self.num = num

    def navigate_to_site(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.refresh()
        time.sleep(2)

    def login(self):
        self.driver.find_element(By.ID, 'loginLi').click()
        self.driver.refresh()
        time.sleep(2)
        try:
            self.driver.switch_to.frame('contentIframe')
        except NoSuchFrameException:
            self.verify()
            self.driver.switch_to.frame('contentIframe')
        finally:
            user = self.driver.find_element(By.NAME, 'username')
            user.send_keys(self.username)
            time.sleep(2)
            pwd = self.driver.find_element(By.NAME, 'password')
            pwd.send_keys(self.password)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/div[3]/span').click()
            time.sleep(2)

    def verify(self):
        verify_code = input()
        code = self.driver.find_element(By.NAME, 'captcha')
        code.send_keys(verify_code)
        self.driver.find_element(By.CLASS_NAME, 'code-btn').click()
        time.sleep(2)

    def download_single_page(self):
        try:
            self.driver.find_element(By.ID, 'AllSelect').click()
            time.sleep(1)
            self.driver.find_element(By.CLASS_NAME, 'AllDownload').click()
            time.sleep(2)
        except NoSuchElementException:
            print('exception occurs when downloading!')

    def download_pages(self, cases_per_page=5):
        while True:
            self.driver.refresh()
            time.sleep(2)
            self.download_single_page()
            self.num -= cases_per_page
            if self.num <= 0:
                break
            try:
                button = self.driver.find_element(By.XPATH, "//*[text()='下一页']")
                time.sleep(2)
                button.click()
            except NoSuchElementException:
                print('no more pages!')
                return

    def select_cases(self):
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, 'advenced-search').click()
        start = self.driver.find_element(By.ID, 'cprqStart')
        start.send_keys(self.start_date)
        time.sleep(3)
        end = self.driver.find_element(By.ID, 'cprqEnd')
        end.send_keys(self.end_date)
        time.sleep(3)
        self.driver.find_element(By.ID, 'searchBtn').click()
        self.driver.refresh()
        time.sleep(20)

    def crawl(self, start_date, end_date, num):
        assert start_date != '' and end_date != '' and num > 0
        self.start_date = start_date
        self.end_date = end_date
        self.num = num

        self.navigate_to_site()
        self.login()
        self.select_cases()
        self.download_pages()
        time.sleep(1000)


def main():
    username = '18695633836'
    password = '171437slF'
    crawl = Crawler(username, password)
    crawl.crawl('2021-11-01', '2021-12-01', 22)


if __name__ == '__main__':
    main()


