
1.输入原始图片，通过二值化，边缘检测，和基于色调的颜色微调等办法检测出原图中的车牌号的位置；

2.把检测到的车牌(ROI)裁剪，为车牌号的识别做准备；

3.基于裁剪的车牌号，使用直方图的波峰波谷分割裁剪的车牌号（如上图中的第3步）

4.训练机器学习模型做车牌识别，这里训练了2个SVM,一个SVM用来识别省份简称(如 鲁)，另一个SVM用来识别字母和数字。

执行入口 prediction.py 中car_lrp_for_img方法传入图片进行识别，但是基于二值化，峰值裁剪方式定位车牌使用SVM识别的方式识别率很低，建议使用基于CNN的方式

