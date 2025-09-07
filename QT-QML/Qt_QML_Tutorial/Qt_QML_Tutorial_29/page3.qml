import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.3

Rectangle {
  width: 200
  height: 200
  color: "blue"

  ColumnLayout {
    anchors.fill: parent
    spacing: 20

    Text {
      id: textPage1
      text: qsTr("page 3")
      font.pointSize: 20
    }
    Button {
      id: myButton1
      text: "go page 1"
      onClicked: {
        myStackView.pop(2)
      }
    }
    Button {
      id: myButton2
      text: "go page 2"
      onClicked: {
        myStackView.push("page2.qml")
      }
    }
  }
}
