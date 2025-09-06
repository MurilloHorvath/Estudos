import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 22 Column Layout")

  ColumnLayout {
    anchors.centerIn: parent
    spacing: 10

    Rectangle {
      id: myRect_1
      Layout.preferredWidth: 50
      Layout.preferredHeight: 50
      Layout.alignment: Qt.AlignCenter
      //Layout.fillWidth: true
      color: "orange"
      Text {
        id: myRect_1_Text
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 1")
      }
    }

    Rectangle {
      id: myRect_2
      Layout.preferredWidth: 75
      Layout.preferredHeight: 75
      Layout.alignment: Qt.AlignRight
      color: "green"
      Text {
        id: myRect_2_Text
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 2")
      }
    }

    Rectangle {
      id: myRect_3
      Layout.preferredWidth: 100
      Layout.preferredHeight: 100
      Layout.alignment: Qt.AlignLeft
      color: "blue"
      Text {
        id: myRect_3_Text
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 3")
      }
    }

    Rectangle {
      id: myRect_4
      Layout.preferredWidth: 125
      Layout.preferredHeight: 125
      Layout.alignment: Qt.AlignCenter
      color: "red"
      Text {
        id: myRect_4_Text
        anchors.centerIn: parent
        color: "#FFFFFF"
        text: qsTr("Rect 4")
      }
    }
  }
}
