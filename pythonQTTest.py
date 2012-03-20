import sys
import math
from PyQt4 import QtCore, QtGui, QtDeclarative


class MalFeld(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MalFeld, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.green
        self.image = QtGui.QImage()
        self.lastPoint = QtCore.QPoint()
        
        

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):
        #if self.width() > self.image.width() or self.height() > self.image.height():
        self.resizeImage(self.image, QtCore.QSize(self.width(), self.height()))
        self.update()
        super(MalFeld, self).resizeEvent(event)


    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)
        self.image = newImage


    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth
    

    def circstar(self, zack, aussenr, innenr):
        painter = QtGui.QPainter(self);
        #painter.setPen(QtCore.Qt.blue);
        #painter.setFont(QtGui.QFont("Arial", 30));
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, "Qt");
        
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
                QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        step = 6.28/zack;
        summe = 0
        lastX=aussenr+math.sin(step * summe)*aussenr
        lastY=aussenr+math.cos(step * summe)*aussenr
        while summe <= zack:
            
            x = aussenr+math.sin(step * summe)*aussenr
            y = aussenr+math.cos(step * summe)*aussenr
            xin = aussenr+math.sin(step/2+step * summe)*innenr
            yin = aussenr+math.cos(step/2+step * summe)*innenr
            painter.drawLine(lastX,lastY,x,y)
            painter.drawLine(x,y,xin,yin)
            lastX=xin
            lastY=yin
            summe = summe+1
        self.update()
            
        
    def malMal(self):
        painter = QtGui.QPainter(self);
        painter.setPen(QtCore.Qt.blue);
        painter.setFont(QtGui.QFont("Arial", 30));
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, "Qt");
        print("Hallo Welt!")
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
                QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        #painter.drawLine(10,10, 500,10)
        #painter.drawLine(500,10,500 ,500)
        #painter.drawLine(500,500, 10,500)
        #painter.drawLine(10,500, 10,10)
        #painter.drawRect(10,10,500,500)

        painter.drawEllipse(100,100,500,500)
        painter.drawEllipse(200,150,30,30)
        painter.drawEllipse(400,150,30,30)
        self.modified = True
        rad = self.myPenWidth / 2 + 2
        
        min_cx = 0
        min_cy = 0
        max_iterationen = 100
        y = 0;
        max_betrags_quadrat = 4
        #for xn in xrange(0,500):
        #    cx = min_cx + xn
        #    for yn in xrange(0,500):
        #        #cy = min_cy + yn
        #        #iterationswert = self.punkt_iteration(cx,cy,max_betrags_quadrat, max_iterationen)
        #        #farb_wert = self.choose_color(iterationswert ,max_iterationen)
        #        #painter.setPen(farb_wert)
        #        #painter.drawPoint(xn,yn)
        #        q = xn*xn + yn*yn
        #        if(q > 4):
        #            painter.setPen(QtCore.Qt.white)
        #        else:
        #            painter.setPen(QtCore.Qt.black)
        #        painter.drawPoint(xn,yn)
        self.update()
    def punkt_iteration (self,cx,cy,max_betrags_quadrat, max_iter):
        betrag_quadrat = 0
        itera = 0
        x = 0
        y = 0
        while ( betrag_quadrat <= max_betrags_quadrat ) and ( itera < max_iter ):
            xt = x * x - y * y + cx
            yt = 2 * x * y + cy
            x = xt
            y = yt
            itera = itera + 1
            betrag_quadrat = x * x + y * y
        return itera
    def choose_color(self,iterationswert ,max_iterationen):
        return QtGui.QColor(iterationswert)
    def drawSEvent(self):
        self.circstar(1000, 300, 10)
        self.circstar(100, 200, 10)
        
        


class Sternchen(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(Sternchen,self).__init__(parent)
        self.saveAsActs = []

        self.malFeld = MalFeld(self)
        self.setCentralWidget(self.malFeld)
        self.malFeld.show()

        #self.createActions()
        #self.createMenus()
        

        self.setWindowTitle("PyQT Test")
        self.resize(500, 500)
        self.button = QtGui.QPushButton("Hello World",self)
        self.button.show()
        self.connect(self.button,QtCore.SIGNAL("clicked()"),self.malFeld.drawSEvent)
        

        


if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    #w=QtGui.QLabel("Hello World")
    #w.setGeometry(300,300,500,300)
    #w.show()
    sternchen = Sternchen()
    sternchen.show()
    app.exec_()
