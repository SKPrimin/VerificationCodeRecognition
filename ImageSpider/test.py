import cv2
# import requests
# img_src = 'https://static.geetest.com/captcha_v3/batch/v3/189/2022-01-05T16/word/05885b04b50b4ca38b051d9d87d70a13.jpg?challenge=8f96d24ede3d43a3bf75375e04b0fe31'
# img = requests.get(url=img_src).content
# with open('codesrc.png', 'wb') as f:
#     f.write(img)

img = cv2.imread('codesrc.png')
cropped = img[-40:, 0:116]
cv2.imwrite("./codesrccv.png", cropped)