from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class BotAcs:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', options=chrome_options)

    def Iniciar(self):
        self.driver.get(
            'https://link_of_system.org/Accounting/AccountStep/')
        time.sleep(30)

        link_email = self.driver.find_element_by_id('username')
        link_email.click()
        link_email.send_keys('nome.sobrenome')
        time.sleep(5)

        link_password = self.driver.find_element_by_id('password')
        link_password.click()
        link_password.send_keys('password')
        time.sleep(5)

        login = self.driver.find_element_by_tag_name('button')
        login.click()

        time.sleep(30)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('01')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('02')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('03')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('04')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('05')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[7]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        time.sleep(5)
        link_return.click()

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('06')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[8]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('07')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[9]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('08')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[10]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('09')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[11]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('10')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[12]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('14')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[13]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('15')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[14]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('16')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[15]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('20')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[16]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('21')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[17]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('22')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[18]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('23')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[19]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('29')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[20]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('32')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[21]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('36')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[22]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('37')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[23]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('38')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[24]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('40')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[25]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('17')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[26]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)

        link_new = self.driver.find_element_by_xpath(
            '//*[@id="main"]/section/section/section/div[2]/div/div[2]/div[3]/div/button')
        link_new.click()

        time.sleep(8)

        search = self.driver.find_element_by_xpath(
            '//input[@id = "sbAccountingStep"]')
        search.click()
        search.send_keys('33')
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        search.send_keys(Keys.DOWN)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(2)

        link_create = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[3]/form/div[2]/div/div[2]/button')
        link_create.click()
        time.sleep(4)

        link_yes = self.driver.find_element_by_xpath(
            '/html/body/div[27]/div/div/div[3]/button[1]')
        link_yes.click()
        time.sleep(4)

        link_return = self.driver.find_element_by_xpath(
            '//*[@id = "main"]/section/section/section/div[2]/div/div[2]/form/div[5]/div/div/button')
        link_return.click()
        time.sleep(5)


bot = BotAcs()
bot.Iniciar()
