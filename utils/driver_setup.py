from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def create_driver():
    # Inicializar el navegador Chrome usando webdriver-manager
    chrome_options = Options()

    # Evitar popups de Chrome
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.password_manager_leak_detection": False,
        "signin.allowed": False
    }

    chrome_options.add_experimental_option("prefs", prefs)

    # Iniciar maximizado y en incógnito
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    # Evitar log
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver