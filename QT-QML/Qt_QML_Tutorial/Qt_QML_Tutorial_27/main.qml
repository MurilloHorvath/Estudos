import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.3

Window {
  id: myWindow
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 27 ScrollView Control")

  ScrollView {
    anchors.fill: parent

    ScrollBar.horizontal.policy: ScrollBar.AlwaysOn
    ScrollBar.vertical.policy: ScrollBar.AlwaysOn

    ColumnLayout {
      spacing: 20
      width: myWindow.width

      Repeater {
        model: 50
        Rectangle {
          width: parent.width
          height: 30
          color: index % 2 == 0 ? "#FF00FF" : "#00FF00"
          Text {
            id: myText
            anchors.centerIn: parent
            text: "Rectangle : " + (index + 1)
            font.pointSize: 20
          }
        }
      }
    }
  }
}
