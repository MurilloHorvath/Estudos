import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 24 Grid Layout")

  GridLayout {
    anchors.centerIn: parent
    columns: 2

    Rectangle {
      id: myRect1
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
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
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
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
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      Layout.columnSpan: 2
      Layout.fillWidth: true
      color: "red"
      Text {
        id: text3
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 3")
      }
    }
    Rectangle {
      id: myRect4
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      Layout.rowSpan: 2
      Layout.fillHeight: true
      color: "grey"
      Text {
        id: text4
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 4")
      }
    }
    Rectangle {
      id: myRect5
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      color: "pink"
      Text {
        id: text5
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 5")
      }
    }
    Rectangle {
      id: myRect6
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      color: "purple"
      Text {
        id: text6
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 6")
      }
    }
    Rectangle {
      id: myRect7
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      Layout.columnSpan: 2
      Layout.alignment: Qt.AlignCenter
      color: "black"
      Text {
        id: text7
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 7")
      }
    }
  }
}
