import sys
import time
import ddddocr
import cv2
import requests
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login?from_spm_id=333.851.top_bar.login_window')
driver.implicitly_wait(2) # seconds
number = 200
# 选择元素
driver.find_elements_by_css_selector('#login-username')[0].send_keys("1")
driver.find_elements_by_css_selector('#login-passwd')[0].send_keys("1")
driver.find_elements_by_css_selector('div.btn-box>a.btn-login')[0].click()

for i in range(number):
    time.sleep(2)
    try:
        img_src = driver.find_elements_by_css_selector('.geetest_item_img')[0].get_attribute('src')
        driver.find_elements_by_css_selector('.geetest_refresh')[0].click()
        img = requests.get(url=img_src).content
        with open('codesrc.png', 'wb') as f:
            f.write(img)
        # 裁剪出答案
        imgcv = cv2.imread('codesrc.png')
        cropped = imgcv[-40:, 0:116]
        cv2.imwrite("./codesrccv.png", cropped)
        # 初步识别
        ocr = ddddocr.DdddOcr()
        with open('codesrccv.png', 'rb') as f:
            img_an_bytes = f.read()
        res = ocr.classification(img_an_bytes)

        # 图片保存
        with open(f'./textData/{i}_{res}.png', 'wb') as f:
            f.write(img)
        with open(f'./textData/{i}_{res}_answer.png', 'wb') as f:
            f.write(img_an_bytes)
        sys.stdout.write("\rSpider %d/%d" % (i, number))
        sys.stdout.flush()
    except Exception as e:
        # 跳过检测按钮 重试
        driver.find_elements_by_css_selector('.geetest_panel_error_content')[0].click()



    # ocr = ddddocr.DdddOcr()
    # with open('code.png', 'rb') as f:
    #     img_bytes = f.read()
    # res = ocr.classification(img_bytes).lower()
    # with open(f'./data/{res}.png','wb') as f:
    #     f.write(img_bytes)
    # driver.find_elements_by_xpath('//*[@id="icode"]')[0].click()
    # time.sleep(1)
    # sys.stdout.write("\rCreating %d/%d" % (i, number))
    # sys.stdout.flush()
