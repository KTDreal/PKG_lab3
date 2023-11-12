# This Python file uses the following encoding: utf-8
import sys
import os
import cv2 as cv
import numpy as np

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setFixedSize(1200, 800)
        self.currentState = 0
        self.deleteScaled = False
        self.list = ["blurredBuilding.png", "sharpen.jpg", "global.jpg", "otsu.jpg", "adapted.jpg"]
        self.labels = ["Original Image", "Sharpened Image", "Global Threshold Image", "Otsu Threshold Image", "Adapted Threshold Image"]
        img = cv.imread("blurredBuilding.png", 0)
        img_width = img.shape[1]
        img_height = img.shape[0]
        self.ui.label_image.setGeometry(600 - int(img_width * 0.5), 400 - int(img_height * 0.5), img_width, img_height)
        self.ui.label_image.setPixmap(QPixmap("blurredBuilding.png"))
        self.sharpness_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpen_img = cv.filter2D(img, ddepth=-1, kernel=self.sharpness_kernel)
        cv.imwrite("sharpen.jpg", sharpen_img)
        global_img = cv.threshold(img,127,255,cv.THRESH_BINARY)
        cv.imwrite("global.jpg", global_img[1])
        Otsu_img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
        cv.imwrite("otsu.jpg", Otsu_img[1])
        adapted_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
        cv.imwrite("adapted.jpg", adapted_img)

    def closeEvent(self, event):
        os.remove("sharpen.jpg")
        os.remove("global.jpg")
        os.remove("otsu.jpg")
        os.remove("adapted.jpg")
        if(self.deleteScaled):
            os.remove("scaled_image.jpg")
            self.deleteScaled = False

    def leftClicked(self):
        if (self.currentState == 0):
            self.currentState = 4
        else:
            self.currentState -= 1
        self.ui.label_image.setPixmap(QPixmap(self.list[self.currentState]))
        self.ui.label_2.setText(self.labels[self.currentState])

    def rightClicked(self):
        if (self.currentState == 4):
            self.currentState = 0
        else:
            self.currentState += 1
        self.ui.label_image.setPixmap(QPixmap(self.list[self.currentState]))
        self.ui.label_2.setText(self.labels[self.currentState])

    def chooseImg(self):
        fileName = QFileDialog.getOpenFileName(self, 'Choose the file: ')
        if fileName[0].lower().endswith(('.png', '.jpg', '.gif', '.tiff', '.pcx', '.bmp')):
            os.remove("sharpen.jpg")
            os.remove("global.jpg")
            os.remove("otsu.jpg")
            os.remove("adapted.jpg")
            if(self.deleteScaled):
                os.remove("scaled_image.jpg")
                self.deleteScaled = False
            self.currentState = 0;
            self.ui.label_3.setText(fileName[0])
            self.labels = ["Original Image", "Sharpened Image", "Global Threshold Image", "Otsu Threshold Image", "Adapted Threshold Image"]
            img = cv.imread(fileName[0], 0)
            if (img.shape[0] > 600 or img.shape[1] > 1200):
                image = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
                imageName = "scaled_image.jpg"
                cv.imwrite(imageName, image)
                self.deleteScaled = True
            else:
                image = img
                imageName = fileName[0]
                self.deleteScaled = False
            self.list = [imageName, "sharpen.jpg", "global.jpg", "otsu.jpg", "adapted.jpg"]
            img_width = image.shape[1]
            img_height = image.shape[0]
            self.ui.label_image.setGeometry(600 - int(img_width * 0.5), 400 - int(img_height * 0.5), img_width, img_height)
            self.ui.label_image.setPixmap(QPixmap(imageName))
            sharpen_img = cv.filter2D(image, ddepth=-1, kernel=self.sharpness_kernel)
            cv.imwrite("sharpen.jpg", sharpen_img)
            global_img = cv.threshold(image,127,255,cv.THRESH_BINARY)
            cv.imwrite("global.jpg", global_img[1])
            Otsu_img = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
            cv.imwrite("otsu.jpg", Otsu_img[1])
            adapted_img = cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
            cv.imwrite("adapted.jpg", adapted_img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
