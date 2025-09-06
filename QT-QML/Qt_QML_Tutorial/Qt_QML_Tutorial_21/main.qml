import QtQuick 2.15
import QtQuick.Window 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 21 Color Animation")

  Rectangle {
    id: myRect
    width: 200
    height: 200
    radius: height / 2
    anchors.centerIn: parent
    color: "#FF0000"
  }
  SequentialAnimation {
    loops: Animation.Infinite
    running: true

    ColorAnimation {
      target: myRect
      property: "color"
      from: "#FF0000"
      to: "#0000FF"
      duration: 2000
    }

    ColorAnimation {
      target: myRect
      property: "color"
      from: "#0000FF"
      to: "#FF0000"
      duration: 2000
    }
  }
}
