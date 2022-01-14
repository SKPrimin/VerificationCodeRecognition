import sys
import time
import ddddocr
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://jwxt3.ahu.edu.cn/default3.aspx')

number = 200
# 选择元素
for i in range(number):
    driver.find_elements_by_xpath('//*[@id="icode"]')[0].screenshot("code.png")
    ocr = ddddocr.DdddOcr()
    with open('code.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes).lower()
    with open(f'./data/{res}.png','wb') as f:
        f.write(img_bytes)
    driver.find_elements_by_xpath('//*[@id="icode"]')[0].click()
    time.sleep(1)
    sys.stdout.write("\rCreating %d/%d" % (i, number))
    sys.stdout.flush()


