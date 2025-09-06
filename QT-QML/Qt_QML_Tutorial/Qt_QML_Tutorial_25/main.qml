import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3
import QtQuick.Controls 2.5

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 25 Stack Layout")

  StackLayout {
    id: myStackLayout
    anchors.fill: parent

    currentIndex: 1

    Rectangle {
      id: myRect1
      Layout.fillWidth: true
      Layout.fillHeight: true
      color: "green"
      Label {
        text: qsTr("page 1")
        anchors.centerIn: parent
        font.pointSize: 20
        color: "white"
      }
    }

    Rectangle {
      id: myRect2
      Layout.fillWidth: true
      Layout.fillHeight: true
      color: "grey"
      Label {
        text: qsTr("page 2")
        anchors.centerIn: parent
        font.pointSize: 20
        color: "white"
      }
    }

    Rectangle {
      id: myRect3
      Layout.fillWidth: true
      Layout.fillHeight: true
      color: "blue"
      Label {
        text: qsTr("page 3")
        anchors.centerIn: parent
        font.pointSize: 20
        color: "white"
      }
    }
  }

  RowLayout {
    spacing: 10
    anchors.bottom: parent.bottom
    anchors.horizontalCenter: parent.horizontalCenter
    Button {
      id: myButton1
      text: "page 1"
      onClicked: {
        myStackLayout.currentIndex = 0
      }
    }
    Button {
      id: myButton2
      text: "page 2"
      onClicked: {
        myStackLayout.currentIndex = 1
      }
    }
    Button {
      id: myButton3
      text: "page 3"
      onClicked: {
        myStackLayout.currentIndex = 2
      }
    }
  }
}
