# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 14:27
# @Author  : daiheng.gao(weipu)
# @Email   : daiheng.gdh@alibaba-inc.com
# @File    : a.py

import cv2

a = "img/gdh.JPG"

content = cv2.imread(a)
content = cv2.resize(content, (220, 280))
cv2.imwrite("gdh_2019.jpg", content)