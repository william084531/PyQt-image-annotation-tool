from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsItem, QStyleOptionGraphicsItem
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt

class My_lineitem(QGraphicsLineItem):
    def __init__(self, lastpos):
        super(My_lineitem, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        pen = QPen(Qt.green)
        pen.setWidth(2)
        pen.setCosmetic(True)
        self.setPen(pen)
        self.lastpos = lastpos
        self.pos = None



    def move_line(self, point):
        self.pos = point
        self.setLine(self.pos.x(), self.pos.y(), self.lastpos.x(), self.lastpos.y())


