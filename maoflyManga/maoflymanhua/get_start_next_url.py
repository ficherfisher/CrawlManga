import yaml
import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class get_start:

    def __init__(self):
        yaml_config = open(os.path.join(os.path.dirname(__file__), "config_url.yaml"), encoding="utf-8")
        page_dict = yaml.load(yaml_config.read(), Loader=yaml.FullLoader)
        self.urls = list(page_dict.values())
        yaml_config.close()
        print("-" * 20 + "加载start_url" + "-" * 20)
        self.keys = list(page_dict.keys())

    def get_start_url(self):
        start_urls = []
        for index, i in enumerate(self.urls):
            url = i
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  # 设置无界面
            options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 无图模式
            options.add_argument('lang=zh_CN.UTF-8')  # utf-8
            options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            next_item = driver.find_element(By.XPATH, "//div[@class='form-inline']//a[5]")
            try:
                ActionChains(driver).click(next_item).perform()
                time.sleep(3)
                start_urls.append(driver.current_url)
            except Exception as e:
                print(e)
            print("-" * 20 + self.keys[index] + "-" * 20)

        return start_urls


if __name__ == "__main__":
    get_start_ = get_start()
    print(get_start_.get_start_url())




