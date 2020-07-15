from PyQt5.QtWidgets import QGraphicsView, QGraphicsPixmapItem
from annotation_object.image_scene import image_scene
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPainterPath, QPaintDevice
from PyQt5.QtCore import QByteArray, QBuffer, QIODevice, QPointF, QRectF, Qt
import json

class MyGraphicsView(QGraphicsView):
    def __init__(self):
        QGraphicsView.__init__(self)
        self.setMouseTracking(True)
        self._dlg_file = QFileDialog()
        self.scene = image_scene(self)
        self.setScene(self.scene)

        # for zoom in zoom out
        self.unit_in = 2
        self.unit_out = 1 / 2
        self.imageName_ = None
        self.jsonName_ = None
        self.pixmap = None
        self.save_jsonName = ''
        self.jsonName_ = ''
        self.import_flag = 0
        self.transform_initial = self.transform()
        self.zoom_flag = 0
        self.setRenderHint(QPainter.Antialiasing)

    def import_image(self):
        # clear all item in view
        self.scene.clear()
        self.scene.lastpos = []
        self.scene.polygon = []
        self.scene.Polygon_flag = 0
        self.scene.Rect_flag = 0
        # import image
        options = self._dlg_file.Options()
        self.imageName_, _ = self._dlg_file.getOpenFileName(self, "Read Image", "",
                                                      "Image Files (*.png *.jpg *.jpeg *.gif *.tiff *.tif);;All Files (*)",
                                                      options=options)
        self.pixmap = QPixmap(self.imageName_)
        photo = QGraphicsPixmapItem(self.pixmap)
        # change graphic view free
        self.viewport().installEventFilter(self)
        self.setGeometry(0, 0, self.pixmap.width()+10, self.pixmap.height()+10)
        self.setTransform(self.transform_initial)
        self.scene.addItem(photo)
        self.import_flag = 1



    def import_json(self):
        self.scene.clear()
        self.scene.lastpos = []
        self.scene.polygon = []
        self.scene.Polygon_flag = 0
        self.scene.Rect_flag = 0
        options = self._dlg_file.Options()
        self.jsonName_, _ = self._dlg_file.getOpenFileName(self, "Read Json", "",
                                                            "Json Files (*.json);;All Files (*)",
                                                            options=options)
        if self.jsonName_ !='':
            self.import_flag = 1
            with open(self.jsonName_, 'r') as reader:
                jf = json.loads(reader.read())

            # to turn string back to byte
            image_json = jf["image"].encode(encoding="utf-8")
            ba = QByteArray.fromBase64(image_json)
            img = QImage.fromData(ba, 'PNG')
            self.pixmap = QPixmap.fromImage(img)
            photo = QGraphicsPixmapItem(self.pixmap)
            self.viewport().installEventFilter(self)
            self.setGeometry(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)
            self.scene.addItem(photo)
            if jf["polygon"] != []:
                all_poly_item = []
                for i in jf["polygon"]:
                    single_poly_item = []
                    for j in i:
                        single_poly_item.append(QPointF(j[0], j[1]))
                    all_poly_item.append(single_poly_item)
                    # TODO: make mainwindow not only show a item, not to get this error "wrapped C/C++ object of type XXXX has been deleted"
                    print("test")
                self.scene.load_polygon_item(all_poly_item)
            else:
                print("no polygon")
            if jf["rect"] != []:
                all_rect_item = []
                for i in jf["rect"]:
                    single_rect_item = []
                    for j in i:
                        single_rect_item.append(QPointF(j[0], j[1]))
                    all_rect_item.append(single_rect_item)
                self.scene.load_rect_item(all_rect_item)
            else:
                print("no rect")
        else:
            print("no json import")

    def rotate_left(self):
        if self.import_flag == 1:
            self.rotate(-10)
        # to get current transformation matrix for the view
        elif self.import_flag != 1:
            print("no image import")

    def rotate_right(self):
        if self.import_flag == 1:
            self.rotate(10)
        # to get current transformation matrix for the view
        elif self.import_flag != 1:
            print("no image import")
    def zoom_in(self):
        if self.import_flag == 1 and self.zoom_flag < 4:
            self.zoom_flag +=1
            self.scale(self.unit_in, self.unit_in)
        elif self.import_flag != 1:
            print("no image import")
        elif self.zoom_flag == 4:
            print("can't zoom in")
        # to get current transformation matrix for the view

    def zoom_out(self):
        if self.import_flag == 1 and self.zoom_flag > -4:
            self.zoom_flag -= 1
            self.scale(self.unit_out, self.unit_out)
        # to get current transformation matrix for the view
        elif self.import_flag != 1:
            print("no image import")
        elif self.zoom_flag == -4:
            print("can't zoom out")

    def original_view(self):
        if self.import_flag == 1:
            self.zoom_flag = 0
            self.setTransform(self.transform_initial)
        # to get current transformation matrix for the view
        elif self.import_flag != 1:
            print("no image import")

    def save_image(self):
        options = self._dlg_file.Options()
        if self.pixmap is not None:
            # Get region of scene to capture from somewhere.
            area = QRectF(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)

            # Create a QImage to render to and fix up a QPainter for it.
            image = QImage(QRectF.toRect(area).size(), QImage.Format_ARGB32_Premultiplied)
            painter = QPainter(image)

            # Render the region of interest to the QImage.
            self.scene.render(painter, QRectF(image.rect()), area)
            painter.end()
            save_imageName, _ = self._dlg_file.getSaveFileName(self, "Save Image", "",
                                                               "Image Files (*.png *.jpg *.jpeg *.gif *.tiff *.tif);;All Files (*)",
                                                               options=options)
            # Save the image to a file.
            image.save(save_imageName)
        else:
            print("can't save image")
    def save_json(self):
        options = self._dlg_file.Options()
        if self.pixmap is not None:
            area = QRectF(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)
            self.select_all_scene = QPainterPath()
            self.select_all_scene.addRect(area)
            self.scene.setSelectionArea(self.select_all_scene, Qt.IntersectsItemShape, self.transform())
            allitem = self.scene.items()
            selecteditem = self.scene.selectedItems()
            # selecteditem: different object has different type, use, selecteditem[?].type(), can get different object, polygon type == 5, rect type == 3, gripitem type == 2
            polygon_point = []
            rect_point = []
            for i in selecteditem:
                if i.type() == 5:
                    # get polgon item point
                    each_point_polygon = []
                    for j in i.m_points:
                        each_point_polygon.append([j.x(), j.y()])
                    polygon_point.append(each_point_polygon)
                elif i.type() == 3:
                    each_point_rect = []
                    each_use = [[i.rect_point[0].x(), i.rect_point[1].x()], [i.rect_point[0].y(), i.rect_point[1].y()]]
                    for j in i.rect_point:
                        if j is i.rect_point[0]:
                            each_point_rect.append([min(each_use[0]), min(each_use[1])])
                        else:
                            each_point_rect.append([max(each_use[0]), max(each_use[1])])
                    rect_point.append(each_point_rect)
            # save image
            PIC = self.pixmap.toImage()
            ba = QByteArray()
            buffer = QBuffer(ba)
            buffer.open(QIODevice.WriteOnly)
            PIC.save(buffer, 'PNG')
            base64_data = ba.toBase64().data()
            image_data = str(base64_data, encoding='utf-8')

            # save to json
            annotation_object = {
                'polygon': polygon_point,
                'rect': rect_point,
                'image': image_data}

            self.save_jsonName, _ = self._dlg_file.getSaveFileName(self, "Save Json", "",
                                                              "Json Files (*.json);;All Files (*)", options=options)
            if self.save_jsonName != '':
                with open(self.save_jsonName, 'w') as json_file:
                    json.dump(annotation_object, json_file)
                print("test")
            else:
                print("no choose save path")
        else:
            print("can't save json")

