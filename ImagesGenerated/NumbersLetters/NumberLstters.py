import sys
import random
# captcha是用于生成验证码图片的库，可以 pip install captcha 来安装它
from captcha.image import ImageCaptcha

# 用于生成验证码的字符集
CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 字符集的长度
CHAR_SET_LEN = 36
# 验证码的长度，每个验证码由4个数字组成
CAPTCHA_LEN = 4

# 验证码图片的存放路径
CAPTCHA_IMAGE_PATH = 'AlphaNumericImages/'


def generate_captcha_image(charSet=CHAR_SET, charSetLen=CHAR_SET_LEN, captchaImgPath=CAPTCHA_IMAGE_PATH, choice=200):
    """生成验证码图片"""
    k = 0
    total = 1
    for i in range(CAPTCHA_LEN):
        total *= charSetLen
    for i in range(charSetLen):
        for j in range(charSetLen):
            for m in range(charSetLen):
                for n in range(charSetLen):
                    # 计算出choice对应概率
                    if random.randint(0, int(total/choice)):
                        continue
                    captcha_text = charSet[i] + charSet[j] + charSet[m] + charSet[n]
                    image = ImageCaptcha()
                    image.write(captcha_text, captchaImgPath + captcha_text + '.jpg')
                    k += 1
                    sys.stdout.write("\rCreating %d/%d" % (k, choice))
                    sys.stdout.flush()


if __name__ == '__main__':
    generate_captcha_image(CHAR_SET, CHAR_SET_LEN, CAPTCHA_IMAGE_PATH, 200)
    sys.stdout.write("\nFinished")
    sys.stdout.flush()
