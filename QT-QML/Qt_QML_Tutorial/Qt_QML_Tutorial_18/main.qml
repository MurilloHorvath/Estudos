import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Shapes 1.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 18 Path Animation")

  Shape {
    id: myShape
    width: parent
    height: parent

    ShapePath {
      strokeColor: "#00FF00"
      strokeWidth: 2
      fillColor: "#FF0000"

      startX: 50
      startY: 50

      PathLine {
        x: 590
        y: 50
      }
      PathLine {
        x: 590
        y: 430
      }
      PathLine {
        x: 50
        y: 430
      }
      PathLine {
        x: 50
        y: 50
      }
    }
  }

  Rectangle {
    id: myCircle
    width: 20
    height: 20
    radius: myCircle.height / 2
    color: "#0000FF"
    x: 50
    y: 50
  }

  Path {
    id: myPath
    startX: 50
    startY: 50

    PathLine {
      x: 590
      y: 50
    }
    PathLine {
      x: 590
      y: 430
    }
    PathLine {
      x: 50
      y: 430
    }
    PathLine {
      x: 50
      y: 50
    }
  }

  PathAnimation {
    id: myPathAnimation
    target: myCircle
    path: myPath
    duration: 5000
    loops: Animation.Infinite
    running: true
  }
}
