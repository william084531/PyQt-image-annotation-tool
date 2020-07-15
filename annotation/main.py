
from PyQt5.QtWidgets import QApplication
import sys
# from annotation.image_window_test import window
from annotation_object.image_window import window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    window.show()
    sys.exit(app.exec())


# class window(QMainWindow):
#     def __init__(self, parent=None):
#         super(window, self).__init__(parent)
#         self.title = "PyQt5 Graphic View Test cat"
#         self.top = 100
#         self.left = 100
#         self.width = 1000
#         self.height = 800
#         self.view = MyGraphicsView()
#         self.setCentralWidget(self.view)
#         self.view.setMouseTracking(True)
#         self.InitWindow()
#
#     def InitWindow(self):
#         self.importbutton = QPushButton("file import ", self)
#         self.importbutton.setGeometry(self.width - 150, 20, 100, 50)
#         self.importbutton.clicked.connect(self.view.import_image)
#         self.importjsonbutton = QPushButton("json import ", self)
#         self.importjsonbutton.setGeometry(self.width - 150, 90, 100, 50)
#         self.importjsonbutton.clicked.connect(self.view.import_json)
#         self.Rotateleftbutton = QPushButton("Rotate-L ", self)
#         self.Rotateleftbutton.setGeometry(self.width-150, 160, 100, 50)
#         self.Rotateleftbutton.clicked.connect(self.view.rotate_left)
#         self.Rotaterightbutton = QPushButton("Rotate-R ", self)
#         self.Rotaterightbutton.setGeometry(self.width-150, 230, 100, 50)
#         self.Rotaterightbutton.clicked.connect(self.view.rotate_right)
#         self.Zoominbutton = QPushButton("Zoom_in", self)
#         self.Zoominbutton.setGeometry(self.width-150, 300, 100, 50)
#         self.Zoominbutton.clicked.connect(self.view.zoom_in)
#         self.Zoomoutbutton = QPushButton("Zoom_out", self)
#         self.Zoomoutbutton.setGeometry(self.width-150, 370, 100, 50)
#         self.Zoomoutbutton.clicked.connect(self.view.zoom_out)
#         self.Originalbutton = QPushButton("Original_view", self)
#         self.Originalbutton.setGeometry(self.width - 150, 440, 100, 50)
#         self.Originalbutton.clicked.connect(self.view.original_view)
#         self.enablepolygonsbutton = QPushButton("create_polygens", self)
#         self.enablepolygonsbutton.setGeometry(self.width-270, 20, 100, 50)
#         self.enablepolygonsbutton.clicked.connect(self.view.scene.enable_polygons)
#         self.enablerectsbutton = QPushButton("create_rect", self)
#         self.enablerectsbutton.setGeometry(self.width - 270, 90, 100, 50)
#         self.enablerectsbutton.clicked.connect(self.view.scene.enable_rect)
#         self.undobutton = QPushButton("undo", self)
#         self.undobutton.setGeometry(self.width - 270, 160, 100, 50)
#         self.undobutton.clicked.connect(self.view.scene.undo)
#         self.delet_item = QPushButton("delet_item", self)
#         self.delet_item.setGeometry(self.width - 270, 230, 100, 50)
#         self.delet_item.clicked.connect(self.view.scene.delete)
#         self.delet_all = QPushButton("delet_all_item", self)
#         self.delet_all.setGeometry(self.width - 270, 300, 100, 50)
#         self.delet_all.clicked.connect(self.view.scene.delete_all)
#         self.savebutton = QPushButton("save", self)
#         self.savebutton.setGeometry(self.width - 270, 370, 100, 50)
#         self.savebutton.clicked.connect(self.view.save_image)
#         self.savejsonbutton = QPushButton("save json", self)
#         self.savejsonbutton.setGeometry(self.width - 270, 440, 100, 50)
#         self.savejsonbutton.clicked.connect(self.view.save_json)
#
#         # TODO: delet function
#         # self.removebutton = QPushButton("removeitem", self)
#         # self.removebutton.setGeometry(self.width - 150, 650, 100, 50)
#         # self.removebutton.clicked.connect(self.removeitem)
#
#         self.setWindowIcon(QtGui.QIcon("C:/Users/willi/Desktop/classification/data_annotated/0001.jpg"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)

            # if self.Rect_flag == 1:
            #     self.view.setDragMode(QGraphicsView.RubberBandDrag)

# class MyGraphicsScene(QGraphicsScene):
#     def __init__(self, parent=None):
#         super(MyGraphicsScene, self).__init__(parent)
#         self._parent = parent
#         self.Polygon_flag = 0
#         self.Rect_flag = 0
#         self.rubberband_select_flag = 0
#         self.lastpos = []
#         self.polygon = []
#         self.rect = []
#         self.line_item_list = []
#         self.Grip_item_list = []
#         self.view = MyGraphicsView()
#
#
#     def enable_polygons(self):
#         self.Polygon_flag = 1
#         self.Rect_flag = 0
#
#     def enable_rect(self):
#         self.Rect_flag = 1
#         self.Polygon_flag = 0
#
#     def undo(self):
#         # # TODO: if future need redo this function should change because it kill the last element
#         # # kill point
#         if len(self.polygon) >= 1:
#             self.removeItem(self.itemAt(self.polygon[-1].x(), self.polygon[-1].y(), self.view.transform()))
#             self.removeItem(self.itemAt(self.polygon[-1].x(), self.polygon[-1].y(), self.view.transform()))
#             del self.polygon[-1]
#             if len(self.polygon) == 1:
#                 self.lastpos = []
#         else:
#             print("can't undo")
#
#     def delete(self):
#         if self.selectedItems() != [] and self.rubberband_select_flag !=1:
#             selecteditem = self.selectedItems()
#             for idx in range(len(selecteditem)):
#                 selecteditem = selecteditem + selecteditem[idx].m_items
#             # selecteditem = selecteditem+selecteditem[0].m_items
#             for i in selecteditem:
#                 self.removeItem(i)
#         # elif self.selectedItems() != [] and self.rubberband_select_flag ==1:
#         #     self.rubberband_select_flag = 0
#         #     selecteditem = self.selectedItems()
#         #     for i in selecteditem:
#         #         self.removeItem(i)
#         else:
#             print("can't delete")
#
#     def delete_all(self):
#         if self.selectedItems() != [] and self.rubberband_select_flag ==1:
#             self.rubberband_select_flag = 0
#             selecteditem = self.selectedItems()
#             for i in selecteditem:
#                 self.removeItem(i)
#         else:
#             print("can't delete all")
#
#     def load_polygon_item(self, point):
#         for i in point:
#             self.polygon_item = PolygonAnnotation()
#             self.addItem(self.polygon_item)
#             self.polygon_item.addPoint(i)
#             # self.polygon_item.addPoint(i)
#
#     def load_rect_item(self, point):
#         for i in point:
#             self.rect_item = rect(i[0])
#             self.addItem(self.rect_item)
#             self.rect_item.addPoint(i)
#             # self.rect_item.addPoint(i)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.RightButton:
#             self.rubberband_select_flag = 1
#             #window.view.setDragMode(QGraphicsView.RubberBandDrag)
#             self._parent.setDragMode(QGraphicsView.RubberBandDrag)
#
#         if event.button() == Qt.LeftButton:
#             self.rubberband_select_flag = 0
#             self._parent.setDragMode(QGraphicsView.ScrollHandDrag)
#             pos = event.scenePos()
#             if self.Polygon_flag == 1:
#                 self._parent.setDragMode(QGraphicsView.NoDrag)
#                 # self.polygon_item cannot put in intiital
#                 self.polygon_item = PolygonAnnotation()
#                 # to get all point coordinate
#                 self.polygon.append(pos)
#                 # catch the last element as x, y coordinate
#                 x = self.polygon[-1].x()
#                 y = self.polygon[-1].y()
#                 if self.lastpos == []:
#                     self.lastpos = [self.polygon[-1].x(), self.polygon[-1].y()]
#                 else:
#                     self.lastpos[0] = self.polygon[-2].x()
#                     self.lastpos[1] = self.polygon[-2].y()
#                 # add circle point in scene
#                 if self._parent.import_flag == 1:
#                     point = GripItem(self.polygon_item, len(self.polygon))
#                     self.addItem(point)
#                     self.Grip_item_list.append(point)
#                     point.setPos(self.polygon[-1])
#                     print(self.lastpos)
#                     self.line_Item = line(self.polygon[-1])
#                     self.addItem(self.line_Item)
#                     self.line_item_list.append(self.line_Item)
#
#             elif self.Rect_flag == 1 and self.rect == [] and self._parent.import_flag == 1:
#                 self._parent.setDragMode(QGraphicsView.NoDrag)
#                 # to get all point coordinate
#                 self.rect.append(pos)
#                 self.square = rect(self.rect[0])
#                 self.addItem(self.square)
#
#             elif self.Rect_flag == 1 and self.rect != [] and self._parent.import_flag == 1:
#                 self.Rect_flag = 0
#                 pos = event.scenePos()
#                 self.rect.append(pos)
#                 self.square.addPoint(self.rect)
#                 # TODO: save special info for this rect item use setData
#                 # self.square.setData(3, "test_rect")
#                 self.rect = []
#         super(MyGraphicsScene, self).mousePressEvent(event)
#
#     def mouseReleaseEvent(self, event):
#         QGraphicsScene.mouseReleaseEvent(self, event)
#         self._parent.setDragMode(QGraphicsView.NoDrag)
#
#
#     def mouseMoveEvent(self, event):
#         # call basic function
#         QGraphicsScene.mouseMoveEvent(self, event)
#         if self.Polygon_flag == 1 and self._parent.import_flag == 1 and self.lastpos != []:
#             self.line_Item.move_line(event.scenePos())
#         if self.Rect_flag == 1 and self.rect != []:
#             self.square.move_rect(event.scenePos())
#             print(self.rect)
#
#
#     def mouseDoubleClickEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             if self.Polygon_flag == 1:
#                 self.Polygon_flag = 0
#                 for i in range(len(self.Grip_item_list)):
#                     self.removeItem(self.Grip_item_list[i])
#                     self.removeItem(self.line_item_list[i])
#                 self.addItem(self.polygon_item)
#                 self.polygon_item.addPoint(self.polygon)
#                 # TODO: save special info for this polygon item use setData
#                 # self.polygon_item.setData(5, "test_polygon")
#                 self.polygon = []
#                 self.lastpos = []
#         super(MyGraphicsScene, self).mouseDoubleClickEvent(event)

# class MyGraphicsView(QGraphicsView):
#     def __init__(self):
#         QGraphicsView.__init__(self)
#         self.setMouseTracking(True)
#         self._dlg_file = QFileDialog()
#         self.scene = MyGraphicsScene(self)
#         self.setScene(self.scene)
#         # for zoom in zoom out
#         self.unit_in = 2
#         self.unit_out = 1 / 2
#         self.imageName_ = None
#         self.jsonName_ = None
#         self.pixmap = None
#         self.save_jsonName = ''
#         self.jsonName_ = ''
#         self.import_flag = 0
#         self.transform_initial = self.transform()
#         self.zoom_flag = 0
#
#     def import_image(self):
#         # clear all item in view
#         self.scene.clear()
#         self.scene.lastpos = []
#         self.scene.polygon = []
#         self.scene.Polygon_flag = 0
#         self.scene.Rect_flag = 0
#         # import image
#         options = self._dlg_file.Options()
#         self.imageName_, _ = self._dlg_file.getOpenFileName(self, "Read Image", "",
#                                                       "Image Files (*.png *.jpg *.jpeg *.gif *.tiff *.tif);;All Files (*)",
#                                                       options=options)
#         self.pixmap = QPixmap(self.imageName_)
#         photo = QGraphicsPixmapItem(self.pixmap)
#         # change graphic view free
#         self.viewport().installEventFilter(self)
#         self.setGeometry(0, 0, self.pixmap.width()+10, self.pixmap.height()+10)
#         self.setTransform(self.transform_initial)
#         self.scene.addItem(photo)
#         self.import_flag = 1
#
#
#
#     def import_json(self):
#         self.scene.clear()
#         self.scene.lastpos = []
#         self.scene.polygon = []
#         self.scene.Polygon_flag = 0
#         self.scene.Rect_flag = 0
#         options = self._dlg_file.Options()
#         self.jsonName_, _ = self._dlg_file.getOpenFileName(self, "Read Json", "",
#                                                             "Json Files (*.json);;All Files (*)",
#                                                             options=options)
#         if self.jsonName_ !='':
#             self.import_flag = 1
#             with open(self.jsonName_, 'r') as reader:
#                 jf = json.loads(reader.read())
#
#             # to turn string back to byte
#             image_json = jf["image"].encode(encoding="utf-8")
#             ba = QByteArray.fromBase64(image_json)
#             img = QImage.fromData(ba, 'PNG')
#             self.pixmap = QPixmap.fromImage(img)
#             photo = QGraphicsPixmapItem(self.pixmap)
#             self.viewport().installEventFilter(self)
#             self.setGeometry(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)
#             self.scene.addItem(photo)
#             if jf["polygon"] != []:
#                 all_poly_item = []
#                 for i in jf["polygon"]:
#                     single_poly_item = []
#                     for j in i:
#                         single_poly_item.append(QPointF(j[0], j[1]))
#                     all_poly_item.append(single_poly_item)
#                     # TODO: make mainwindow not only show a item, not to get this error "wrapped C/C++ object of type XXXX has been deleted"
#                     print("test")
#                 self.scene.load_polygon_item(all_poly_item)
#             else:
#                 print("no polygon")
#             if jf["rect"] != []:
#                 all_rect_item = []
#                 for i in jf["rect"]:
#                     single_rect_item = []
#                     for j in i:
#                         single_rect_item.append(QPointF(j[0], j[1]))
#                     all_rect_item.append(single_rect_item)
#                 self.scene.load_rect_item(all_rect_item)
#             else:
#                 print("no rect")
#         else:
#             print("no json import")
#
#     def rotate_left(self):
#         if self.import_flag == 1:
#             self.rotate(-10)
#         # to get current transformation matrix for the view
#         elif self.import_flag != 1:
#             print("no image import")
#
#     def rotate_right(self):
#         if self.import_flag == 1:
#             self.rotate(10)
#         # to get current transformation matrix for the view
#         elif self.import_flag != 1:
#             print("no image import")
#     def zoom_in(self):
#         if self.import_flag == 1 and self.zoom_flag < 4:
#             self.zoom_flag +=1
#             self.scale(self.unit_in, self.unit_in)
#         elif self.import_flag != 1:
#             print("no image import")
#         elif self.zoom_flag == 4:
#             print("can't zoom in")
#         # to get current transformation matrix for the view
#
#     def zoom_out(self):
#         if self.import_flag == 1 and self.zoom_flag > -4:
#             self.zoom_flag -= 1
#             self.scale(self.unit_out, self.unit_out)
#         # to get current transformation matrix for the view
#         elif self.import_flag != 1:
#             print("no image import")
#         elif self.zoom_flag == -4:
#             print("can't zoom out")
#
#     def original_view(self):
#         if self.import_flag == 1:
#             self.zoom_flag = 0
#             self.setTransform(self.transform_initial)
#         # to get current transformation matrix for the view
#         elif self.import_flag != 1:
#             print("no image import")
#
#     def save_image(self):
#         options = self._dlg_file.Options()
#         if self.pixmap is not None:
#             # Get region of scene to capture from somewhere.
#             area = QRectF(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)
#
#             # Create a QImage to render to and fix up a QPainter for it.
#             image = QImage(QRectF.toRect(area).size(), QImage.Format_ARGB32_Premultiplied)
#             painter = QPainter(image)
#
#             # Render the region of interest to the QImage.
#             self.scene.render(painter, QRectF(image.rect()), area)
#             painter.end()
#             save_imageName, _ = self._dlg_file.getSaveFileName(self, "Save Image", "",
#                                                                "Image Files (*.png *.jpg *.jpeg *.gif *.tiff *.tif);;All Files (*)",
#                                                                options=options)
#             # Save the image to a file.
#             image.save(save_imageName)
#         else:
#             print("can't save image")
#     def save_json(self):
#         options = self._dlg_file.Options()
#         if self.pixmap is not None:
#             area = QRectF(0, 0, self.pixmap.width() + 10, self.pixmap.height() + 10)
#             self.select_all_scene = QtGui.QPainterPath()
#             self.select_all_scene.addRect(area)
#             self.scene().setSelectionArea(self.select_all_scene, Qt.IntersectsItemShape, self.transform())
#             selecteditem = self.scene().selectedItems()
#             # selecteditem: different object has different type, use, selecteditem[?].type(), can get different object, polygon type == 5, rect type == 3, gripitem type == 2
#             polygon_point = []
#             rect_point = []
#             for i in selecteditem:
#                 if i.type() == 5:
#                     # get polgon item point
#                     each_point_polygon = []
#                     for j in i.m_points:
#                         each_point_polygon.append([j.x(), j.y()])
#                     polygon_point.append(each_point_polygon)
#                 elif i.type() == 3:
#                     each_point_rect = []
#                     each_use = [[i.rect_point[0].x(), i.rect_point[1].x()], [i.rect_point[0].y(), i.rect_point[1].y()]]
#                     for j in i.rect_point:
#                         if j is i.rect_point[0]:
#                             each_point_rect.append([min(each_use[0]), min(each_use[1])])
#                         else:
#                             each_point_rect.append([max(each_use[0]), max(each_use[1])])
#                     rect_point.append(each_point_rect)
#             # save image
#             PIC = self.pixmap.toImage()
#             ba = QByteArray()
#             buffer = QBuffer(ba)
#             buffer.open(QIODevice.WriteOnly)
#             PIC.save(buffer, 'PNG')
#             base64_data = ba.toBase64().data()
#             image_data = str(base64_data, encoding='utf-8')
#
#             # save to json
#             annotation_object = {
#                 'polygon': polygon_point,
#                 'rect': rect_point,
#                 'image': image_data}
#
#             self.save_jsonName, _ = self._dlg_file.getSaveFileName(self, "Save Json", "",
#                                                               "Json Files (*.json);;All Files (*)", options=options)
#             if self.save_jsonName != '':
#                 with open(self.save_jsonName, 'w') as json_file:
#                     json.dump(annotation_object, json_file)
#                 print("test")
#             else:
#                 print("no choose save path")
#         else:
#             print("can't save json")


    # def save_json(self):

# TODO : make polygon resize
# class PolygonAnnotation(QGraphicsPolygonItem):
#     def __init__(self, parent=None):
#         super(PolygonAnnotation, self).__init__(parent)
#         self.m_points = []
#         self.setZValue(10)
#         pen = QPen(Qt.green)
#         pen.setWidth(2)
#         pen.setCosmetic(True)
#         self.setPen(pen)
#         self.setAcceptHoverEvents(True)
#         self.setFlag(QGraphicsItem.ItemIsSelectable, True)
#         self.setFlag(QGraphicsItem.ItemIsMovable, True)
#         self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
#         self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.view = MyGraphicsView()
#         self.m_items = []
#         self.poly_item = []
#
#     def number_of_points(self):
#         return len(self.m_items)
#
#
#     def addPoint(self, p):
#         if self.m_points == []:
#             self.m_points = p
#             self.setPolygon(QtGui.QPolygonF(self.m_points))
#             for i in range(len(self.m_points)):
#                 item = GripItem(self, i, 1)
#                 self.scene().addItem(item)
#                 self.m_items.append(item)
#                 item.setPos(self.m_points[i])
#
#     def movePoint(self, i, p):
#         if 0 <= i < len(self.m_points):
#             self.m_points[i] = self.mapFromScene(p)
#             self.setPolygon(QtGui.QPolygonF(self.m_points))
#             # print("sss", self.m_points)
#
#     def move_item(self, index, pos):
#         if 0 <= index < len(self.m_items):
#             item = self.m_items[index]
#             item.setEnabled(False)
#             item.setPos(pos)
#             item.setEnabled(True)
#
#     def itemChange(self, change, value):
#         if change == QGraphicsItem.ItemPositionHasChanged:
#             for i, point in enumerate(self.m_points):
#                 self.move_item(i, self.mapToScene(point))
#         return super(PolygonAnnotation, self).itemChange(change, value)
#
#     def hoverEnterEvent(self, event):
#         self.setBrush(QtGui.QColor(0, 100, 100, 100))
#         super(PolygonAnnotation, self).hoverEnterEvent(event)
#
#     def hoverLeaveEvent(self, event):
#         self.setBrush(QtGui.QBrush(Qt.NoBrush))
#         super(PolygonAnnotation, self).hoverLeaveEvent(event)


# class line(QGraphicsLineItem):
#     def __init__(self, lastpos):
#         super(line, self).__init__()
#         self.setFlag(QGraphicsItem.ItemIsMovable, True)
#         self.setFlag(QGraphicsItem.ItemIsSelectable, True)
#         pen = QPen(Qt.green)
#         pen.setWidth(2)
#         pen.setCosmetic(True)
#         self.setPen(pen)
#         self.lastpos = lastpos
#
#     def move_line(self, point):
#         self.pos = point
#         self.setLine(self.pos.x(), self.pos.y(), self.lastpos.x(), self.lastpos.y())
#
# class GripItem(QGraphicsPathItem):
#     def __init__(self, annotation_item, index, type=0):
#         super(GripItem, self).__init__()
#         self.m_annotation_item = annotation_item
#         self.m_index = index
#         self.circle = QtGui.QPainterPath()
#         self.circle.addEllipse(QRectF(-4, -4, 8, 8))
#         self.square = QtGui.QPainterPath()
#         self.square.addRect(QRectF(-4, -4, 8, 8))
#         self.setPath(self.circle)
#         self.setBrush(Qt.green)
#         self.setFlag(QGraphicsItem.ItemIsSelectable, True)
#         if type == 1:
#             self.setFlag(QGraphicsItem.ItemIsMovable, True)
#         self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
#         self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
#         self.setAcceptHoverEvents(True)
#         self.setZValue(11)
#         self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#
#     def hoverEnterEvent(self, event):
#         self.setPath(self.square)
#         self.setBrush(Qt.red)
#         super(GripItem, self).hoverEnterEvent(event)
#
#     def hoverLeaveEvent(self, event):
#         self.setPath(self.circle)
#         self.setBrush(Qt.green)
#         super(GripItem, self).hoverLeaveEvent(event)
#
#     def itemChange(self, change, value):
#         if change == QGraphicsItem.ItemPositionChange and self.isEnabled():
#             self.m_annotation_item.movePoint(self.m_index, value)
#         return super(GripItem, self).itemChange(change, value)

# class rect(QGraphicsRectItem):
#     def __init__(self, lastpos):
#         super(rect, self).__init__()
#         self.setFlag(QGraphicsItem.ItemIsMovable, True)
#         self.setFlag(QGraphicsItem.ItemIsSelectable, True)
#         self.setAcceptHoverEvents(True)
#         pen = QPen(Qt.green)
#         pen.setWidth(2)
#         pen.setCosmetic(True)
#         self.setPen(pen)
#         self.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
#         self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
#         self.lastpos = lastpos
#         self.pos = []
#         self.rect_point = []
#         self.m_items = []
#         self.view = MyGraphicsView()
#     def move_rect(self, point):
#         self.pos = point
#         point_use = [[self.lastpos.x(), self.pos.x()], [self.lastpos.y(), self.pos.y()]]
#         self.setRect(QRectF(QPointF(min(point_use[0]), min(point_use[1])), QPointF(max(point_use[0]), max(point_use[1]))))
#
#     def movePoint(self, i, p):
#         if 0 <= i < len(self.rect_point):
#             self.rect_point[i] = self.mapFromScene(p)
#             rect_use = [[self.rect_point[0].x(), self.rect_point[1].x()], [self.rect_point[0].y(), self.rect_point[1].y()]]
#             if i == 0:
#                 self.setRect(QRectF(QPointF(min(rect_use[0]), min(rect_use[1])), QPointF(max(rect_use[0]), max(rect_use[1]))))
#             else:
#                 self.setRect(QRectF(QPointF(min(rect_use[0]), min(rect_use[1])), QPointF(max(rect_use[0]), max(rect_use[1]))))
#
#     def move_item(self, index, pos):
#         if 0 <= index < len(self.m_items):
#             item = self.m_items[index]
#             item.setEnabled(False)
#             item.setPos(pos)
#             item.setEnabled(True)
#
#     def addPoint(self, p):
#         self.rect_point = p
#         self.setRect(QRectF(p[0], p[1]))
#         for i in range(len(p)):
#             item = GripItem(self, i, 1)
#             self.scene().addItem(item)
#             self.m_items.append(item)
#             item.setPos(self.rect_point[i])
#
#     def itemChange(self, change, value):
#         if change == QGraphicsItem.ItemPositionHasChanged:
#             for i, point in enumerate(self.rect_point):
#                 self.move_item(i, self.mapToScene(point))
#         return super(rect, self).itemChange(change, value)
#
#     def hoverEnterEvent(self, event):
#         self.setBrush(QtGui.QColor(0, 100, 100, 100))
#         super(rect, self).hoverEnterEvent(event)
#
#     def hoverLeaveEvent(self, event):
#         self.setBrush(QtGui.QBrush(Qt.NoBrush))
#         super(rect, self).hoverLeaveEvent(event)