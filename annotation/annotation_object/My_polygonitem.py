from PyQt5.QtWidgets import QGraphicsPolygonItem, QGraphicsItem
from PyQt5.QtGui import QPen, QCursor, QPolygonF, QColor, QBrush, QPainter
from PyQt5.QtCore import Qt
from .My_gripItem import My_gripItem

class My_polygonitem(QGraphicsPolygonItem):
    def __init__(self, parent=None):
        super(My_polygonitem, self).__init__(parent)
        self.m_points = []
        self.setZValue(10)
        pen = QPen(Qt.green)
        pen.setWidth(2)
        pen.setCosmetic(True)
        self.setPen(pen)
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.m_items = []
        self.poly_item = []

    def number_of_points(self):
        return len(self.m_items)


    def addPoint(self, p):
        if self.m_points == []:
            self.m_points = p
            self.setPolygon(QPolygonF(self.m_points))
            for i in range(len(self.m_points)):
                item = My_gripItem(self, i, 1)
                self.scene().addItem(item)
                self.m_items.append(item)
                item.setPos(self.m_points[i])

    def movePoint(self, i, p):
        if 0 <= i < len(self.m_points):
            self.m_points[i] = self.mapFromScene(p)
            self.setPolygon(QPolygonF(self.m_points))
            print("move_item", self.m_points)

    def move_item(self, index, pos):
        if 0 <= index < len(self.m_items):
            item = self.m_items[index]
            item.setEnabled(False)
            item.setPos(pos)
            item.setEnabled(True)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for i, point in enumerate(self.m_points):
                self.move_item(i, self.mapToScene(point))
        return super(My_polygonitem, self).itemChange(change, value)

    def hoverEnterEvent(self, event):
        self.setBrush(QColor(0, 100, 100, 100))
        super(My_polygonitem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(Qt.NoBrush))
        super(My_polygonitem, self).hoverLeaveEvent(event)
