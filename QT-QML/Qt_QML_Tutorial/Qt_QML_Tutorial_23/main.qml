import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 23 Row Layout")

  Rectangle {
    id: mySquare
    width: parent.width / 2
    height: parent.height / 2
    anchors.centerIn: parent
    border.color: "blue"
    border.width: 3

    RowLayout {
      anchors.centerIn: parent
      spacing: 5

      Rectangle {
        id: myRect1
        Layout.preferredWidth: mySquare.width / 5
        Layout.preferredHeight: mySquare.height / 5
        Layout.alignment: Qt.AlignTop
        //Layout.fillHeight: true
        color: "green"
        Text {
          id: text1
          anchors.centerIn: parent
          color: "#FFFFFF"
          text: qsTr("Rect 1")
        }
      }
      Rectangle {
        id: myRect2
        Layout.preferredWidth: mySquare.width / 4
        Layout.preferredHeight: mySquare.height / 4
        Layout.alignment: Qt.AlignBottom
        color: "blue"
        Text {
          id: text2
          anchors.centerIn: parent
          color: "#FFFFFF"
          text: qsTr("Rect 2")
        }
      }
      Rectangle {
        id: myRect3
        Layout.preferredWidth: mySquare.width / 3
        Layout.preferredHeight: mySquare.height / 3
        color: "red"
        Text {
          id: text3
          anchors.centerIn: parent
          color: "#FFFFFF"
          text: qsTr("Rect 3")
        }
      }
    }
  }
}
