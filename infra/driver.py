from selenium import webdriver

class Driver:
    def init(self):
        self.driver = None

    def set_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('--disable-web-security')
        options.add_argument("--start-maximized")
        options.add_argument('--remote-debugging-port=9222')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        return options

    def set_webdriver(self):
        options = self.set_chrome_options()
        self.driver = webdriver.Chrome(options=options)
        return self.driver