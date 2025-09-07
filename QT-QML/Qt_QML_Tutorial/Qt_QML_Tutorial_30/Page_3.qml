import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Item {
  id: myPage3
  Rectangle {
    anchors.fill: parent
    anchors.centerIn: parent
    color: "blue"

    Column {
      anchors.centerIn: parent
      spacing: 10

      Text {
        id: text3
        font.bold: true
        font.pointSize: 20
        color: "white"
        text: qsTr("page 3")
      }

      Button {
        text: "Go to page 2"
        Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        onClicked: {
          mySwipeView.currentIndex = 1
        }
      }
      Button {
        text: "Go to page 1"
        Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
        onClicked: {
          mySwipeView.currentIndex = 0
        }
      }
    }
  }
}
