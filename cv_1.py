import cv2
from matplotlib import pyplot as plt



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    cap.set(3,240)
    cap.set(4,480)
    for x in range(18):
        print("read val " + str(x) + " => " + str(cap.get(x)))
    while True:
        retval, image = cap.read()
        # cv2.line(image, (0, 0), (260, 260), (255, 0, 0), 5)
        cv2.rectangle(image, (420, 120), (500, 128), (0, 255, 0), 3)

        cv2.circle(image, (425, 63), 63, (0, 0, 255), 0)  # 圆，-1为向内填充

        # gray = cv2.cvtColor(image,cv2.COLOR_BAYER_GB2RGB)
        cv2.imshow("image",image)
        if cv2.waitKey(1) & 0xff  == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()
    pass