import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 讓程式控制你已經開啟好，並登入蝦皮的那個Chrome瀏覽器
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # 連接到已開啟的Chrome瀏覽器

# 這裡因為我的chromeDriver安裝在和Chrome.exe同個根目錄下，所以括號內不用指定路徑
driver = webdriver.Chrome(options=options)

# 要搶的頁面連結
driver.get('https://tw.shp.ee/1Qn345q')
#測試連結
#driver.get('https://shopee.tw/Little-Fun-%E0%AA%A6-%E1%B5%95%CC%88-%E0%AB%A9%E3%80%90%E5%8F%B0%E7%81%A3%E7%8F%BE%E8%B2%A8%E3%80%91%E5%92%96%E5%95%A1%E7%AC%91%E8%87%89-%E8%A7%A3%E5%A3%93%E7%90%83-%E6%AF%9B%E7%B5%A8%E5%B0%8F%E5%85%AC%E4%BB%94-%E7%8E%A9%E5%81%B6-%E6%89%8B%E6%8D%8F%E5%AE%89%E6%92%AB%E7%8E%A9%E5%85%B7-%E8%A7%A3%E5%A3%93%E6%8B%BF%E6%8D%8F-%E5%92%96%E5%95%A1%E7%90%83-%E5%B0%8F%E5%85%AC%E4%BB%94-i.1081838456.23786408698?xptdk=1adff70f-74bb-48b2-b31d-aecf8f540222')

# 等"直接購買"available後點選
def do():
    while True:
        try:
            WebDriverWait(driver, 1200).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"直接購買")]'))).click()
            print('------do 直接購買')
            break  # 找到並點擊後跳出循環
        except:
            print('找不到"直接購買"按鈕，繼續嘗試...')
            driver.refresh()
            time.sleep(1)  # 稍微等待避免過於頻繁

# 等"去買單"available後點選，需強制睡一秒最順
def do2():
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "SHq91i") and contains(text(),"去買單")]'))).click()
            print('-----do2 去買單')
            break  # 找到並點擊後跳出循環
        except:
            print('找不到"去買單"按鈕，繼續嘗試...')

# 等待"貨到付款"按鈕可用，然後點擊它
def click_cash_on_delivery():
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//button[@aria-label="貨到付款" and @aria-disabled="false"]')
            )).click()
            print('已點擊貨到付款按鈕')
            break  # 點擊後跳出循環
        except:
            # 如果貨到付款按鈕無法點擊或不存在，則選擇信用卡付款
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.XPATH, '//button[contains(text(),"信用卡/金融卡")]')
                )).click()
                print('已點擊信用卡付款按鈕')
                break  # 點擊後跳出循環
            except:
                print('信用卡付款按鈕也無法點擊，請檢查頁面元素')
                break  # 跳出循環
# 檢查是否出現配送失敗的提示框，若有則點擊"OK"按鈕
def handle_popup():
    try:
        # 檢查是否有顯示配送失敗的提示框
        popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//div[contains(@class, "stardust-popup-content") and contains(text(), "由於您的配送失敗次數過多")]')
        ))
        # 如果提示框出現，點擊OK按鈕
        ok_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//button[contains(text(), "OK")]')
        ))
        ok_button.click()
        print("提示框已點擊 OK")
    except Exception as e:
        print("未找到提示框，或提示框無法點擊:", e)
# 等"下訂單"available後點選
def do3():
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "stardust-button--primary") and contains(text(),"下訂單")]'))).click()
            print('-----do3 下訂單')
            break  # 找到並點擊後跳出循環
        except:
            print('找不到"下訂單"按鈕，繼續嘗試...')


# 等"付款"available後點選
def do4():
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"付款")]'))).click()
            print('-----do4 付款')
            break  # 找到並點擊後跳出循環
        except:
            print('找不到"付款"按鈕，繼續嘗試...')


# 等"取得OTP服務密碼"available後點選
def do5():
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"取得OTP服務密碼(Get the password)")]'))).click()
            print('-----do5 取得OTP服務密碼')
            break  # 找到並點擊後跳出循環
        except:
            print('找不到"取得OTP服務密碼"按鈕，繼續嘗試...')


# 執行所有步驟
do()
do2()
click_cash_on_delivery()
#handle_popup()
#do3()
#do4()
#do5()
