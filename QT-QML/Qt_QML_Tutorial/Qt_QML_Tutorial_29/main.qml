import QtQuick 2.5
import QtQuick.Window 2.5
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 29 StackView Control")

  StackView {
    id: myStackView
    anchors.fill: parent
    initialItem: "qrc:/page1.qml"
  }
}
