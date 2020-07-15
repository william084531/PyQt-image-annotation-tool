from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PyQt5.QtGui import QPen, QCursor, QColor, QBrush
from PyQt5.QtCore import Qt, QRectF, QPointF
from .My_gripItem import My_gripItem

class My_rectitem(QGraphicsRectItem):
    def __init__(self, lastpos):
        super(My_rectitem, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setAcceptHoverEvents(True)
        pen = QPen(Qt.green)
        pen.setWidth(2)
        pen.setCosmetic(True)
        self.setPen(pen)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.lastpos = lastpos
        self.pos = []
        self.rect_point = []
        self.m_items = []

    def move_rect(self, point):
        self.pos = point
        point_use = [[self.lastpos.x(), self.pos.x()], [self.lastpos.y(), self.pos.y()]]
        self.setRect(QRectF(QPointF(min(point_use[0]), min(point_use[1])), QPointF(max(point_use[0]), max(point_use[1]))))

    def movePoint(self, i, p):
        if 0 <= i < len(self.rect_point):
            self.rect_point[i] = self.mapFromScene(p)
            rect_use = [[self.rect_point[0].x(), self.rect_point[1].x()], [self.rect_point[0].y(), self.rect_point[1].y()]]
            if i == 0:
                self.setRect(QRectF(QPointF(min(rect_use[0]), min(rect_use[1])), QPointF(max(rect_use[0]), max(rect_use[1]))))
            else:
                self.setRect(QRectF(QPointF(min(rect_use[0]), min(rect_use[1])), QPointF(max(rect_use[0]), max(rect_use[1]))))
            print("move_item", rect_use)

    def move_item(self, index, pos):
        if 0 <= index < len(self.m_items):
            item = self.m_items[index]
            item.setEnabled(False)
            item.setPos(pos)
            item.setEnabled(True)

    def addPoint(self, p):
        self.rect_point = p
        self.setRect(QRectF(p[0], p[1]))
        for i in range(len(p)):
            item = My_gripItem(self, i, 1)
            self.scene().addItem(item)
            self.m_items.append(item)
            item.setPos(self.rect_point[i])

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged:
            for i, point in enumerate(self.rect_point):
                self.move_item(i, self.mapToScene(point))
        return super(My_rectitem, self).itemChange(change, value)

    def hoverEnterEvent(self, event):
        self.setBrush(QColor(0, 100, 100, 100))
        super(My_rectitem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(QBrush(Qt.NoBrush))
        super(My_rectitem, self).hoverLeaveEvent(event)