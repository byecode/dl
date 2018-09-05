#识别图中的关键点
import cv2


import cv2
import numpy as np

# imread()函数读取目标图片和模板
# img_rgb = cv2.imread("test_all_start_all_image.jpg", 0)
img_rgb = cv2.imread("start_line.jpg", 0)
template = cv2.imread('test_all_start_all_image.jpg', 0)

(waldoHeight, waldoWidth) = template.shape[:2]

# matchTemplate 函数：在模板和输入图像之间寻找匹配,获得匹配结果图像
# minMaxLoc 函数：在给定的矩阵中寻找最大和最小值，并给出它们的位置
res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(res)
topLeft = maxLoc
botRight = (topLeft[0] + waldoWidth, topLeft[1] + waldoHeight)
roi = img_rgb[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

# construct a darkened transparent 'layer' to darken everything
# in the puzzle except for waldo
mask = np.zeros(img_rgb.shape, dtype="uint8")
puzzle = cv2.addWeighted(img_rgb, 0.25, mask, 0.75, 0)

puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi

# display the images
cv2.imshow("Puzzle", img_rgb)
cv2.imshow("Waldo", template)
cv2.waitKey(0)

