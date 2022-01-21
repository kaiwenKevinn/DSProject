import time
from random import random
import zipfile
import os
# from pythoncom import os
import pythoncom
import win32com.client
# import pythoncom

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

download_path_global = os.getcwd() + '\\file_crawler'

# 爬虫+文件转化踩坑集合
# 1、修改浏览器默认下载路径要用绝对路径
# 2、selenium爬虫访问浏览器要设置一定时间间隔，要不然网页没加载成功就切换，网页会崩
# 3、driver.find_element(By.ID, 'id').click()有时候会被其他东东挡住，
#    要用javascript脚本执行（self.driver.execute_script('arguments[0].click()', all_select)）
# 4、下载单个页面的时候会出现点不到的情况，我是点击top按钮让它回到上面页面才可以的
# 5、find element的时候css selector一般不会找不到，其他就不一定
# 6、自动解压下载的文件的时候os.listdir()、ZipFile()、Documents.open()、os.remove()都要用绝对路径，os.rename()可以用来移动文件


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
        self.driver = None
        self.username = username
        self.password = password
        self.start_date = start_date
        self.end_date = end_date
        self.num = num

    def navigate_to_site(self):
        self.driver = webdriver.Firefox(options=self.options)
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
            z = zipfile.ZipFile(self.download_path + '/' + zip_file, 'r')
            for file_name in z.namelist():
                if file_name != '/':
                    new_name = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) + file_name
                    txt_name = new_name.split('.')[0] + '.txt'
                    new_name_absolute_path = os.getcwd() + '/' + self.doc_path + '/' + new_name
                    txt_name_absolute_path = os.getcwd() + '/' + self.txt_path + '/' + txt_name

                    z.extract(member=file_name, path=self.doc_path)
                    os.rename(self.doc_path + '/' + file_name, self.doc_path + '/' + new_name)
                    time.sleep(0.1)
                    self.doc_to_txt(new_name_absolute_path, txt_name_absolute_path)
                    self.encoding_gbk_to_utf8(txt_name_absolute_path)
            time.sleep(0.1)
            z.close()
            time.sleep(0.1)
            os.remove(self.download_path + '/' + zip_file)

    def doc_to_txt(self, word_path, save_path):
        pythoncom.CoInitialize()
        word = win32com.client.Dispatch('kwps.Application')  # 调用word应用
        word.visible = 0  # 后台运行
        word.DisplayAlerts = 0  # 不显示， 不警告
        doc = word.Documents.Open(word_path)
        doc.SaveAs(save_path, 7)  # 保存格式为txt
        doc.Close()
        word.Quit()

    def encoding_gbk_to_utf8(self, path):
        try:
            file_read = open(path, 'r', encoding='GBK')
            content = file_read.read()
            file_write = open(path, 'w', encoding='utf-8')
            file_write.write(content)
            file_read.close()
            file_write.close()
        except UnicodeDecodeError:
            print("One file encoding error")

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

    crawl.crawl('2010-1-20', '2018-1-20', 10)


if __name__ == '__main__':
    main()
