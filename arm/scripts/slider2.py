#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import threading
import rospy
from std_msgs.msg import String
rospy.init_node('basic_publisher', anonymous=True)
pub = rospy.Publisher('topic_name', String, queue_size=10)
rate = rospy.Rate(1)  


def ros(values):
    
    print(values)
    while True:
        message = String()
        message.data = values

        
        pub.publish(message)

        rospy.loginfo("Published: %s", message.data)
        rate.sleep()

move = threading.Thread(target=ros, args=(1,), daemon=True)


class SliderDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Slider Demo')
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.sliders = []
        self.value_labels = []
        self.slider_names = ["BJ", "SJ", "EJ", "W1J", "W2J"]

        for i, slider_name in enumerate(self.slider_names):
            slider_name_input = QLineEdit()
            slider_name_input.setText(slider_name)
            self.layout.addWidget(slider_name_input)

            label = QLabel()
            self.layout.addWidget(label)

            slider = QSlider(Qt.Horizontal)
            slider.setMinimum(-314)  # Minimum value multiplied by 100 for precision
            slider.setMaximum(314)   # Maximum value multiplied by 100 for precision
            slider.setValue(0)       # Set initial value to 0
            self.layout.addWidget(slider)

            value_label = QLabel()
            self.layout.addWidget(value_label)

            self.sliders.append(slider)
            self.value_labels.append(value_label)

            slider.valueChanged.connect(self.update_value_label)

        self.print_button = QPushButton('Move to Goal')
        self.layout.addWidget(self.print_button)
        self.print_button.clicked.connect(self.print_values)

    def update_value_label(self):
        for i, slider in enumerate(self.sliders):
            value = slider.value() / 100.0  # Divide by 100 to get the actual value
            self.value_labels[i].setText(f'Current Value: {value:.2f}')

    def print_values(self):
        
        values = [slider.value() / 100.0 for slider in self.sliders]  # Divide by 100 to get the actual value
        print("Slider Names:", self.slider_names)
        result = ros(values)
        move.start()
    
    
def main():
    app = QApplication(sys.argv)
    window = SliderDemo()
    window.show()
    
    sys.exit(app.exec_())
   

if __name__ == '__main__':
    main()
