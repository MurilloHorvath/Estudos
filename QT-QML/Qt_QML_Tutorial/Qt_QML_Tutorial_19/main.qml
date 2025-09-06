import QtQuick 2.15
import QtQuick.Window 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 19 Sequential Animation")

  Rectangle {
    id: myRect
    width: 200
    height: 200
    color: "#FF0000"
  }

  SequentialAnimation {
    id: mySeqAnimation
    running: true
    loops: Animation.Infinite

    NumberAnimation {
      target: myRect
      properties: "width"
      from: 200
      to: 300
      duration: 2000
      easing.type: Easing.InOutQuad
    }

    NumberAnimation {
      target: myRect
      properties: "height"
      from: 200
      to: 300
      duration: 2000
      easing.type: Easing.InOutQuad
    }

    NumberAnimation {
      target: myRect
      properties: "width"
      from: 300
      to: 200
      duration: 2000
      easing.type: Easing.InOutQuad
    }

    NumberAnimation {
      target: myRect
      properties: "height"
      from: 300
      to: 200
      duration: 2000
      easing.type: Easing.InOutQuad
    }
  }
}
