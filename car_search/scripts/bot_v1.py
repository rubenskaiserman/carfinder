from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep


def url_list(information_list: list, root: str) -> list[str]:
    res = []
    for item in information_list:
        res.append(root + '/' + item.text)
    return res

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    root = 'https://luna.ac/ficha-tecnica/carros'
    css_identifier = ".laTQdt ul li"

    driver.get(root)
    all_brands = driver.find_elements(by=By.CSS_SELECTOR, value=css_identifier)
    urls = url_list(all_brands, root)

    for url in urls:
        driver.get(url)
        all_models = driver.find_elements(by=By.CSS_SELECTOR, value=css_identifier)
        models_url = url_list(all_models, url)
        for m_url in models_url:
            driver.get(m_url)
            all_specs = driver.find_elements(by=By.CSS_SELECTOR, value=css_identifier)
            specs_url = []
            for specs in all_specs:
                specs_url.append(m_url + '/' + specs.text[-4:])
            for s_url in specs_url:
                driver.get(s_url)
                


if __name__ == "__main__":
    main()
