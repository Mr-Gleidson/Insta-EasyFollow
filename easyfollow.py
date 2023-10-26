from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path=r"C:\BotInstagram\bot_curtidas_instagram-master\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        try:
            login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print('Já estamos na página inicial do Instagram!')
            pass

        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))
        self.follow_profiles("6segue")

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        print("Going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def follow_profiles(self, profile):
        driver = self.driver
        driver.get(f"https://www.instagram.com/{profile}")
        time.sleep(5)

        hrefs = driver.find_elements_by_tag_name("a")
        follow_hrefs = [elem.get_attribute("href") for elem in hrefs]
        follow_hrefs = [href for href in follow_hrefs if profile in href and "/following/" in href]

        for follow_href in follow_hrefs:
            try:
                mouse = Controller()
                mouse.position = (783, 230)  # Ajuste isso para a posição correta do botão de "Seguir"
                mouse.click(Button.left)
            except ValueError as err:
                print("Pulando link inválido")
                continue

        followed_profiles = 0
        while followed_profiles <= 117:
            try:
                driver.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]').click()
                time.sleep(random.randint(2, 8))
            except Exception as e:
                print(e)
                time.sleep(5)
            print(f'Já seguimos {followed_profiles} perfis aqui no Insta!')
            followed_profiles += 1
        print('Finalizamos hoje! Aproveite seus seguidores e volte a usar no mínimo a cada 24 horas! =)')


easyFollow = InstagramBot("seu_usuario", "sua_senha")
easyFollow.login()