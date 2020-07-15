from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsItem
from PyQt5.QtGui import QPainterPath, QCursor
from PyQt5.QtCore import Qt, QRectF

class My_gripItem(QGraphicsPathItem):
    def __init__(self, annotation_item, index, type=0):
        super(My_gripItem, self).__init__()
        self.m_annotation_item = annotation_item
        self.m_index = index
        self.circle = QPainterPath()
        self.circle.addEllipse(QRectF(-4, -4, 8, 8))
        self.square = QPainterPath()
        self.square.addRect(QRectF(-4, -4, 8, 8))
        self.setPath(self.circle)
        self.setBrush(Qt.green)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        if type == 1:
            self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.setAcceptHoverEvents(True)
        self.setZValue(11)
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def hoverEnterEvent(self, event):
        self.setPath(self.square)
        self.setBrush(Qt.red)
        super(My_gripItem, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setPath(self.circle)
        self.setBrush(Qt.green)
        super(My_gripItem, self).hoverLeaveEvent(event)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange and self.isEnabled():
            self.m_annotation_item.movePoint(self.m_index, value)
        return super(My_gripItem, self).itemChange(change, value)