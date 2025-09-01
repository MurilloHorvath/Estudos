import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 03")

  CheckBox{
    id: myCheckBox
    checked: true
    anchors.centerIn: parent
    width: 400
    height: 100

    Text{
      id: myCheckBoxText
      text: "check box"
      font.pointSize: 15
      font.bold: true
      color: "#38ada9"
      x:((myCheckBoxindicator.x + myCheckBoxindicator.width) + 10)
      y:((myCheckBox.height - myCheckBoxText.height) / 2)
    }

    onCheckedChanged: {
      console.log("CheckBox Status : " + checked)
    }

    background: Rectangle{
      border.width: 5
      border.color: "blue"
    }

    indicator: Rectangle{
      id: myCheckBoxindicator
      implicitWidth: 50
      implicitHeight: 50
      radius: 10
      border.color: "#1e3799"
      border.width: 3
      x:10
      y:((myCheckBox.height - myCheckBoxindicator.height) / 2)
      Rectangle{
        visible: myCheckBox.checked
        color: "#60a3bc"
        border.color: "#60a3bc"
        radius: 5
        anchors.margins: 10
        anchors.fill: parent
      }
    }
  }
}
