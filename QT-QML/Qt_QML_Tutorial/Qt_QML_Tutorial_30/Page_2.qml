import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Item {
id: myPage2
Rectangle{
  anchors.fill: parent
  anchors.centerIn: parent
  color: "green"

  Column{
    anchors.centerIn: parent
    spacing: 10

    Text {
      id: text2
      font.bold: true
      font.pointSize: 20
      color: "white"
      text: qsTr("page 2")
    }

    Button{
      text: "Go to page 1"
      Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
      onClicked: {
        mySwipeView.currentIndex = 0
      }
    }
    Button{
      text: "Go to page 3"
      Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
      onClicked: {
        mySwipeView.currentIndex = 2
      }
    }
  }
}
}
