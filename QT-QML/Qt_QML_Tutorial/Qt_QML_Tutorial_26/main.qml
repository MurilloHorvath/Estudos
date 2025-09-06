import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 26 Repeater")

  property int index: 0

  ColumnLayout {
    y: 55
    Repeater {
      model: 5
      Rectangle {
        width: 50
        height: 50
        color: "grey"
        Text {
          id: rext1
          anchors.centerIn: parent
          color: "white"
          text: "R" + index
          font.bold: true
          font.pointSize: 10
        }
      }
    }
    Rectangle {
      width: 50
      height: 50
      radius: height / 2
      color: "dark blue"
      Text {
        anchors.centerIn: parent
        color: "white"
        text: "R0"
        font.bold: true
        font.pointSize: 10
      }
    }
  }

  RowLayout {
    Rectangle {
      width: 50
      height: 50
      radius: height / 2
      color: "dark blue"
      Text {
        anchors.centerIn: parent
        color: "white"
        text: "R0"
        font.bold: true
        font.pointSize: 10
      }
    }

    Repeater {
      model: 5
      Rectangle {
        width: 50
        height: 50
        color: "dark green"
        Text {
          id: rext2
          anchors.centerIn: parent
          color: "white"
          text: "R" + index
          font.bold: true
          font.pointSize: 10
        }
      }
    }

    Rectangle {
      width: 50
      height: 50
      radius: height / 2
      color: "dark blue"
      Text {
        anchors.centerIn: parent
        color: "white"
        text: "R0"
        font.bold: true
        font.pointSize: 10
      }
    }
  }
}
