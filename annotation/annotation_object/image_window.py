from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from annotation_object.image_my_viewer import MyGraphicsView

class window(QMainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.title = "PyQt5 Graphic View Test cat"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 800
        self.view = MyGraphicsView()
        self.setCentralWidget(self.view)
        self.view.setMouseTracking(True)
        self.annotation_label = QLabel(self)
        self.InitWindow()

    def InitWindow(self):
        self.importbutton = QPushButton("file import ", self)
        self.importbutton.setGeometry(self.width - 150, 20, 100, 50)
        self.importbutton.clicked.connect(self.view.import_image)
        self.importjsonbutton = QPushButton("json import ", self)
        self.importjsonbutton.setGeometry(self.width - 150, 90, 100, 50)
        self.importjsonbutton.clicked.connect(self.view.import_json)
        self.Rotateleftbutton = QPushButton("Rotate-L ", self)
        self.Rotateleftbutton.setGeometry(self.width-150, 160, 100, 50)
        self.Rotateleftbutton.clicked.connect(self.view.rotate_left)
        self.Rotaterightbutton = QPushButton("Rotate-R ", self)
        self.Rotaterightbutton.setGeometry(self.width-150, 230, 100, 50)
        self.Rotaterightbutton.clicked.connect(self.view.rotate_right)
        self.Zoominbutton = QPushButton("Zoom_in", self)
        self.Zoominbutton.setGeometry(self.width-150, 300, 100, 50)
        self.Zoominbutton.clicked.connect(self.view.zoom_in)
        self.Zoomoutbutton = QPushButton("Zoom_out", self)
        self.Zoomoutbutton.setGeometry(self.width-150, 370, 100, 50)
        self.Zoomoutbutton.clicked.connect(self.view.zoom_out)
        self.Originalbutton = QPushButton("Original_view", self)
        self.Originalbutton.setGeometry(self.width - 150, 440, 100, 50)
        self.Originalbutton.clicked.connect(self.view.original_view)
        self.enablepolygonsbutton = QPushButton("create_polygens", self)
        self.enablepolygonsbutton.setGeometry(self.width-270, 20, 100, 50)
        self.enablepolygonsbutton.clicked.connect(self.view.scene.enable_polygons)
        self.enablerectsbutton = QPushButton("create_rect", self)
        self.enablerectsbutton.setGeometry(self.width - 270, 90, 100, 50)
        self.enablerectsbutton.clicked.connect(self.view.scene.enable_rect)
        self.undobutton = QPushButton("undo", self)
        self.undobutton.setGeometry(self.width - 270, 160, 100, 50)
        self.undobutton.clicked.connect(self.view.scene.undo)
        self.delet_item = QPushButton("delet_item", self)
        self.delet_item.setGeometry(self.width - 270, 230, 100, 50)
        self.delet_item.clicked.connect(self.view.scene.delete)
        # self.delet_all = QPushButton("delet_all_item", self)
        # self.delet_all.setGeometry(self.width - 270, 300, 100, 50)
        # self.delet_all.clicked.connect(self.view.scene.delete_all)
        self.savebutton = QPushButton("save", self)
        self.savebutton.setGeometry(self.width - 270, 370, 100, 50)
        self.savebutton.clicked.connect(self.view.save_image)
        self.savejsonbutton = QPushButton("save json", self)
        self.savejsonbutton.setGeometry(self.width - 270, 440, 100, 50)
        self.savejsonbutton.clicked.connect(self.view.save_json)

        # TODO: add QlIST
        # TODO: delet function
        # self.removebutton = QPushButton("removeitem", self)
        # self.removebutton.setGeometry(self.width - 150, 650, 100, 50)
        # self.removebutton.clicked.connect(self.removeitem)

        self.setWindowIcon(QIcon("C:/Users/willi/Desktop/classification/data_annotated/0001.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)