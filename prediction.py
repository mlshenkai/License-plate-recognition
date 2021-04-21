
from card_seg import Cardseg
from car_id_detect import CaridDetect
import cv2

def car_lrp_for_img(img):
    detection_sign, roi, label, color = CaridDetect(img)
    seg_sign, seg_dict, _ , pre= Cardseg(roi,color)
    if seg_sign ==0:
        print('未找到车牌')
    else:
        print("".join(pre))


def car_lsp_for_video(video_path):
    cap=cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret,fram=cap.read()
        car_lrp_for_img(fram)


if __name__=="__main__":
    img=cv2.imread("./test_img/yello.jpg",cv2.IMREAD_COLOR)
    car_lrp_for_img(img)
