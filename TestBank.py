import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

@pytest.mark.usefixtures('setup')
class TestBank:

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_1(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Your Name'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[1]').text
            assert element == '---Your Name--- :', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_2(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Hermoine Granger'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[2]').text
            assert element == 'Hermoine Granger', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_3(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Harry Potter'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[3]').text
            assert element == 'Harry Potter', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_4(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Ron Weasly'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[4]').text
            assert element == 'Ron Weasly', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_5(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Albus Dumbledore'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[5]').text
            assert element == 'Albus Dumbledore', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_6(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customer Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Neville Longbottom'):
            element = self.browser.find_element(By.XPATH, '//*[@id="userSelect"]/option[6]').text
            assert element == 'Neville Longbottom', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_7(self):
        with allure.step ('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Add Customer'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').is_enabled()
            assert element == True

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_8(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').is_enabled()
            assert element == True

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_9(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Customers'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[3]').is_enabled()
            assert element == True

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_10(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Home'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[1]/button[1]').is_enabled()
            assert element == True

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_11(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Hermoine Granger'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[2]').text
            assert element == 'Hermoine Granger', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_12(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Harry Potter'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[3]').text
            assert element == 'Harry Potter', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_13(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Ron Weasly'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[4]').text
            assert element == 'Ron Weasly', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_14(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Albus Dumbledore'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[5]').text
            assert element == 'Albus Dumbledore', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_15(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Neville Longbottom'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[6]').text
            assert element == 'Neville Longbottom', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_16(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Dollar'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select/option[2]').text
            assert element == 'Dollar', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_17(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Pound'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select/option[3]').text
            assert element == 'Pound', 'Ошибка'

    @allure.feature('Тест XYZ Bank')
    @allure.story('Тест личного кабинета')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_18(self):
        with allure.step('Открыть ссылку'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Bank Manager Login'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[2]/button').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Кликнуть Open Account'):
            self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Выбрать Rupee'):
            element = self.browser.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select/option[4]').text
            assert element == 'Rupee', 'Ошибка'