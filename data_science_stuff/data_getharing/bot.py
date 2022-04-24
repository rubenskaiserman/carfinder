from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import psycopg as db
import uuid

def get_car(driver: webdriver) -> list:
    car_path = driver.find_element(by=By.CSS_SELECTOR, value='.navigation')
    return car_path.text.split('/')[1:]

def get_image(driver: webdriver) -> str:
    return driver.find_element(by=By.CSS_SELECTOR, value='.fl img').get_attribute('src')
    
def get_data(driver: webdriver) -> list:
    data = get_car(driver)

    all_values = driver.find_elements(by=By.CSS_SELECTOR, value='td span')
    for value in all_values:
        data.append(value.text)
    data.append(get_image(driver))
    return data

def generate_query(data: list, hex_id: str) -> str:
    query = f"'{hex_id}', "
    for field in data[:-1]:
        query += f"'{field}', "
    query += f"'{data[-1]}'"

    return query

def insert_data(ids: list, driver: webdriver, root: str, hash_set: set) -> list:
    errors = []
    for id in ids:
        with db.connect("dbname=car_search user=usuarioficticio password=senhaficticia") as conn:
            with conn.cursor() as cur:
                driver.get(root + f'?modification_id={id}')
                try:
                    data = get_data(driver)
                    while True:
                        hash_code = uuid.uuid4().hex
                        if hash_code not in hash_set:
                            cur.execute(f'INSERT INTO all_cars VALUES({generate_query(data, hash_code)});')
                            hash_set.add(hash_code)
                            break
                    print(f'Car_number={id} Inserted')               
                except:
                    print(f'Skiping id={id}')
                    errors.append(id)

    return (errors, hash_set)

def main():
    root = 'https://website.com.pais/'
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    hash_set = set()
    res = insert_data(range(18442, 19998), driver, root, set())
    errors, hash_set = res[0], res[1]
    persistent_errors = insert_data(errors, driver, root, hash_set)[0]

    with open('errors.csv', 'w') as problems:
        w_str = ''
        for id in persistent_errors:
            w_str += f'{id}, '
        problems.write(w_str)

if __name__ == '__main__':
    main()