import time
from random import random
import zipfile
import os
import win32com.client


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

download_path_global = os.getcwd() + '\\file_crawler'


class Crawler:
    def __init__(self, username='18695633836', password='171437slF',
                 start_date='2021-11-01', end_date='2021-12-01', num=20,
                 download_path=download_path_global):
        self.url = 'https://wenshu.court.gov.cn/'
        self.download_path = download_path
        self.doc_path = 'file_unzip/doc'
        self.txt_path = 'file_unzip/txt'
        self.options = webdriver.FirefoxOptions()
        self.options.set_preference("browser.download.folderList", 2)  # 0下载到桌面，1默认下载路径，2指定目录
        self.options.set_preference("browser.download.manager.showWhenStarting", False)
        self.options.set_preference("browser.download.dir", self.download_path)
        self.options.set_preference("browser.download.forbid_open_with", True)  # 不打开保存的提示框
        # 不询问下载路径：后面的参数为要下载页面的content-type的值
        self.options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                    "application/octet-stream,application/vnd.ms-excel,text/csv,application/zip")
        self.driver = webdriver.Firefox(options=self.options)
        self.username = username
        self.password = password
        self.start_date = start_date
        self.end_date = end_date
        self.num = num

    def navigate_to_site(self):
        self.driver.get(self.url)
        time.sleep(random() + 2)

    def login(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/ul/li[1]/a').click()
        time.sleep(random() + 5)  # 有可能点了不跳转
        is_ready = False
        while not is_ready:
            is_ready = True
            try:
                self.driver.switch_to.frame('contentIframe')
                user = self.driver.find_element(By.NAME, 'username')
                user.send_keys(self.username)
                time.sleep(random() * 2)
                pwd = self.driver.find_element(By.NAME, 'password')
                pwd.send_keys(self.password)
                time.sleep(random() * 2)
                self.driver.find_element(By.XPATH, '/html/body/div[2]/div/form/div/div[3]/span').click()
                time.sleep(random() + 5)
            except Exception:
                is_ready = False
                self.driver.refresh()
                time.sleep(random() + 5)
        # 验证码怎么加？

    def verify(self):
        verify_code = input()
        code = self.driver.find_element(By.NAME, 'captcha')
        code.send_keys(verify_code)
        self.driver.find_element(By.CLASS_NAME, 'code-btn').click()
        time.sleep(random() * 2)

    def download_single_page(self):
        is_ready = False
        while not is_ready:
            is_ready = True
            try:
                all_select = self.driver.find_element(By.ID, 'AllSelect')
                self.driver.execute_script('arguments[0].click()', all_select)
                time.sleep(random() + 5)
                all_download = self.driver.find_element(By.CLASS_NAME, 'AllDownload')
                self.driver.execute_script('arguments[0].click()', all_download)
                time.sleep(random() + 5)
            except NoSuchElementException:
                is_ready = False
                self.driver.refresh()
                time.sleep(random() + 3)
                print('exception occurs when downloading!')

    def download_pages(self, cases_per_page=5):
        while True:
            self.download_single_page()
            self.num -= cases_per_page
            if self.num <= 0:
                break
            try:
                self.driver.find_element(By.XPATH, "//*[text()='下一页']").click()
                time.sleep(random() + 5)
                top = self.driver.find_element(By.CSS_SELECTOR, '.layui-icon')
                self.driver.execute_script('arguments[0].click()', top)
                time.sleep(random() + 5)
            except NoSuchElementException:
                print('no more pages!')
                return

    def select_cases(self):
        is_ready = False
        while not is_ready:
            is_ready = True
            try:
                self.driver.find_element(By.CLASS_NAME, 'advenced-search').click()
                try:
                    start = self.driver.find_element(By.ID, 'cprqStart')
                    start.send_keys(self.start_date)
                    time.sleep(random())
                    end = self.driver.find_element(By.ID, 'cprqEnd')
                    end.send_keys(self.end_date)
                    time.sleep(random())
                    self.driver.find_element(By.ID, 's6').click()
                    time.sleep(random() * 2)
                    self.driver.find_element(By.CSS_SELECTOR, '#gjjs_wslx > li:nth-child(4)').click()
                    time.sleep(random())
                    self.driver.find_element(By.ID, 's16').click()
                    time.sleep(random() * 2)
                    self.driver.find_element(By.XPATH, '//*[@id="1_anchor"]').click()
                    time.sleep(random())
                    self.driver.find_element(By.ID, 'searchBtn').click()
                except NoSuchElementException:
                    is_ready = False
                    self.driver.refresh()
                    time.sleep(random() + 3)
                    self.speed_up_for_index()
                    time.sleep(random() + 3)
            except Exception:
                is_ready = False
                self.driver.refresh()
                time.sleep(random() + 3)
                self.speed_up_for_index()
                time.sleep(random() + 3)
        time.sleep(random() + 20)

    def speed_up_for_index(self):
        is_ready = False
        while not is_ready:
            is_ready = True
            try:
                self.driver.find_element(By.CLASS_NAME, 'helpBtn').click()
            except Exception:
                is_ready = False
                self.driver.refresh()
                time.sleep(random() + 3)
        time.sleep(random() + 3)

        is_ready = False
        while not is_ready:
            is_ready = True
            try:
                self.driver.find_element(By.CSS_SELECTOR, '.souye').click()
            except Exception:
                is_ready = False
                self.driver.refresh()
                time.sleep(random() + 3)
        time.sleep(random() + 10)

    def un_zip(self):
        zip_files = os.listdir(self.download_path)
        for zip_file in zip_files:
            z = zipfile.ZipFile(self.download_path+'/'+zip_file, 'r')
            for file_name in z.namelist():
                if file_name != '/':
                    new_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) + file_name
                    txt_name = new_name.split('.')[0]+'.txt'
                    z.extract(member=file_name, path=self.doc_path)
                    os.rename(self.doc_path+'/'+file_name, self.doc_path+'/'+new_name)
                    # self.doc_to_txt(self.doc_path+'/'+new_name, self.txt_path+'/'+txt_name)
            z.close()

    def doc_to_txt(self, word_path, save_path):
            word = win32com.client.Dispatch('Word.Application')  # 调用word应用
            doc = word.Documents.Open(word_path)
            doc.SaveAs(save_path, 4)  # 保存格式为txt
            doc.Close()
            word.Quit()

    def crawl(self, start_date, end_date, num):
        assert start_date != '' and end_date != '' and num > 0
        self.start_date = start_date
        self.end_date = end_date
        self.num = num

        self.navigate_to_site()
        self.speed_up_for_index()
        self.login()
        self.speed_up_for_index()
        self.select_cases()
        self.download_pages()
        self.driver.quit()
        self.un_zip()


def main():
    crawl = Crawler()
    crawl.crawl('2021-11-01', '2021-12-01', 22)


if __name__ == '__main__':
    main()
