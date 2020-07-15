from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from .My_polygonitem import My_polygonitem
from .My_rectitem import My_rectitem
from .My_gripItem import My_gripItem
from .My_lineitem import My_lineitem
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainterPath

class image_scene(QGraphicsScene):
    def __init__(self, parent=None):
        super(image_scene, self).__init__(parent)
        self._parent = parent
        self.Polygon_flag = 0
        self.Rect_flag = 0
        self.lastpos = []
        self.polygon = []
        self.rect = []
        self.line_item_list = []
        self.Grip_item_list = []


    def enable_polygons(self):
        self.Polygon_flag = 1
        self.Rect_flag = 0

    def enable_rect(self):
        self.Rect_flag = 1
        self.Polygon_flag = 0

    def undo(self):
        # # TODO: if future need redo this function should change because it kill the last element
        # # kill point
        if len(self.polygon) >= 1:
            self.removeItem(self.itemAt(self.polygon[-1].x(), self.polygon[-1].y(), self._parent.transform()))
            self.removeItem(self.itemAt(self.polygon[-1].x(), self.polygon[-1].y(), self._parent.transform()))
            del self.polygon[-1]
            if len(self.polygon) == 1:
                self.lastpos = []
        else:
            print("can't undo")

    def delete(self):
        if self.selectedItems() != []:
            selecteditem = self.selectedItems()
            for idx in range(len(selecteditem)):
                if "muen_gripItem" in selecteditem[idx].__repr__():
                    pass
                else:
                    selecteditem = selecteditem + selecteditem[idx].m_items
            for i in selecteditem:
                self.removeItem(i)
        else:
            print("can't delete")

    def load_polygon_item(self, point):
        for i in point:
            self.polygon_item = My_polygonitem()
            self.addItem(self.polygon_item)
            self.polygon_item.addPoint(i)
            # self.polygon_item.addPoint(i)

    def load_rect_item(self, point):
        for i in point:
            self.rect_item = My_rectitem(i[0])
            self.addItem(self.rect_item)
            self.rect_item.addPoint(i)
            # self.rect_item.addPoint(i)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self._parent.canZoom = False

    def keyReleaseEvent(self, event):
        QGraphicsScene.keyReleaseEvent(self, event)
        if event.key() == Qt.Key_Control:
            self._parent.canZoom = True

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            self._parent.setDragMode(QGraphicsView.RubberBandDrag)

        if event.button() == Qt.LeftButton:
            self._parent.setDragMode(QGraphicsView.ScrollHandDrag)
            pos = event.scenePos()
            if self.Polygon_flag == 1:
                self._parent.setDragMode(QGraphicsView.NoDrag)
                # self.polygon_item cannot put in intiital
                self.polygon_item = My_polygonitem()
                # to get all point coordinate
                self.polygon.append(pos)
                # catch the last element as x, y coordinate
                if self.lastpos == []:
                    self.lastpos = [self.polygon[-1].x(), self.polygon[-1].y()]
                else:
                    self.lastpos[0] = self.polygon[-2].x()
                    self.lastpos[1] = self.polygon[-2].y()
                # add circle point in scene
                # if self._parent.import_flag == 1:
                point = My_gripItem(self.polygon_item, len(self.polygon))
                self.addItem(point)
                self.Grip_item_list.append(point)
                point.setPos(self.polygon[-1])
                self.line_Item = My_lineitem(self.polygon[-1])
                self.addItem(self.line_Item)
                self.line_item_list.append(self.line_Item)

            # elif self.Rect_flag == 1 and self.rect == [] and self._parent.import_flag == 1:
            elif self.Rect_flag == 1 and self.rect == []:
                self._parent.setDragMode(QGraphicsView.NoDrag)
                # to get all point coordinate
                self.rect.append(pos)
                self.square = My_rectitem(self.rect[0])
                self.addItem(self.square)

            # elif self.Rect_flag == 1 and self.rect != [] and self._parent.import_flag == 1:
            elif self.Rect_flag == 1 and self.rect != []:
                self.Rect_flag = 0
                pos = event.scenePos()
                self.rect.append(pos)
                self.square.addPoint(self.rect)
                print("original", self.rect)
                # TODO: save special info for this rect item use setData
                # self.square.setData(3, "test_rect")
                self.rect = []
        super(image_scene, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        QGraphicsScene.mouseReleaseEvent(self, event)
        if event.button() == Qt.LeftButton:
            self._parent.setDragMode(QGraphicsView.NoDrag)
            self._parent.setCursor(Qt.ArrowCursor)

        elif event.button() == Qt.RightButton:
            if self._parent.canZoom:
                viewBBox = self._parent.zoomStack[-1] if len(self._parent.zoomStack) else self._parent.sceneRect()
                selectionBBox = self.selectionArea().boundingRect().intersected(viewBBox)
                self.setSelectionArea(QPainterPath())  # Clear current selection area.
                if selectionBBox.isValid() and (selectionBBox != viewBBox):
                    self._parent.zoomStack.append(selectionBBox)
                    self._parent.updateViewer()
            self._parent.setDragMode(QGraphicsView.NoDrag)


    def mouseMoveEvent(self, event):
        # call basic function
        QGraphicsScene.mouseMoveEvent(self, event)
        # if self.Polygon_flag == 1 and self._parent.import_flag == 1 and self.lastpos != []:
        if self.Polygon_flag == 1 and self.lastpos != []:
            self.line_Item.move_line(event.scenePos())
        if self.Rect_flag == 1 and self.rect != []:
            self.square.move_rect(event.scenePos())


    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.Polygon_flag == 1:
                self.Polygon_flag = 0
                for i in range(len(self.Grip_item_list)):
                    self.removeItem(self.Grip_item_list[i])
                    self.removeItem(self.line_item_list[i])
                self.addItem(self.polygon_item)
                self.polygon_item.addPoint(self.polygon)
                print("original",self.polygon)
                # TODO: save special info for this polygon item use setData
                # self.polygon_item.setData(5, "test_polygon")
                # TODO: SAVE POINT IN DB
                self.polygon = []
                self.lastpos = []
        elif event.button() == Qt.RightButton:
            if self._parent.canZoom:
                self._parent.zoomStack = []  # Clear zoom stack.
                self._parent.updateViewer()
        super(image_scene, self).mouseDoubleClickEvent(event)