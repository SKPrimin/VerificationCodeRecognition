import sys
import random
# captcha是用于生成验证码图片的库，可以 pip install captcha 来安装它
from captcha.image import ImageCaptcha

# 用于生成验证码的字符集
CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 字符集的长度
CHAR_SET_LEN = 10
# 验证码的长度，每个验证码由4个数字组成
CAPTCHA_LEN = 4

# 验证码图片的存放路径
CAPTCHA_IMAGE_PATH = 'digitalImages/'
# 用于模型测试的验证码图片的存放路径，测试集

#
def generate_captcha_image(charSet=CHAR_SET, charSetLen=CHAR_SET_LEN, captchaImgPath=CAPTCHA_IMAGE_PATH, choice=200):
    """生成验证码图片"""
    k = 0
    total = 1
    for i in range(CAPTCHA_LEN):
        total *= charSetLen
    numbersList = RandomNumberGeneration(choice)
    for item in numbersList:
        a = item % 10000 // 1000
        b = item % 1000 // 100
        c = item % 100 // 10
        d = item % 10

        captcha_text = charSet[a] + charSet[b] + charSet[c] + charSet[d]
        image = ImageCaptcha()
        image.write(captcha_text, captchaImgPath + captcha_text + '.jpg')
        k += 1
        sys.stdout.write("\rCreating %d/%d" % (k, choice))
        sys.stdout.flush()


def RandomNumberGeneration(n):
    """集合方式实现生成随机数列表"""
    numbers = set()
    while len(numbers) < n:
        # 0~100之间的随机数
        i = random.randint(0, 9999)
        numbers.add(i)
    return numbers


if __name__ == '__main__':
    generate_captcha_image(CHAR_SET, CHAR_SET_LEN, CAPTCHA_IMAGE_PATH, 200)
    sys.stdout.write("\nFinished")
    sys.stdout.flush()
