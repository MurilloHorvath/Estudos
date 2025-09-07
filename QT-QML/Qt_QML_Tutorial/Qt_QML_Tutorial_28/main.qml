import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 28 SplitView Control")

  SplitView {
    id: mySplitView1
    anchors.fill: parent
    orientation: Qt.Vertical

    Rectangle {
      SplitView.minimumWidth: 150
      SplitView.minimumHeight: 50
      width: 200
      color: "#FF0000"
      Text {
        id: text1
        text: qsTr("first view")
        anchors.centerIn: parent
        color: "white"
        font.bold: true
        font.pointSize: 15
      }
    }
    Rectangle {
      SplitView.minimumWidth: 150
      SplitView.minimumHeight: 50
      SplitView {
        id: mySplitView2
        anchors.fill: parent
        orientation: Qt.Horizontal
        Rectangle {
          SplitView.minimumWidth: 150
          SplitView.minimumHeight: 50
          width: 200
          color: "dark green"
          Text {
            id: text31
            text: qsTr("second view")
            anchors.centerIn: parent
            color: "white"
            font.bold: true
            font.pointSize: 15
          }
        }
        Rectangle {
          SplitView.minimumWidth: 150
          SplitView.minimumHeight: 50
          width: 200
          color: "light green"
          Text {
            id: text32
            text: qsTr("second view")
            anchors.centerIn: parent
            color: "white"
            font.bold: true
            font.pointSize: 15
          }
        }
      }
    }
    Rectangle {
      SplitView.minimumWidth: 150
      SplitView.minimumHeight: 50
      width: 200
      color: "#0000FF"
      Text {
        id: text3
        text: qsTr("third view")
        anchors.centerIn: parent
        color: "white"
        font.bold: true
        font.pointSize: 15
      }
    }
  }
}
