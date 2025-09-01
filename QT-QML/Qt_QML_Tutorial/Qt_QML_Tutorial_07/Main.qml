import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 07")

  Row{
    anchors.centerIn: parent
    spacing: 30
    RadioButton{
      id: myRadioButton_1
      text: "Option 1"
      font.pointSize: 20
      font.bold: true
      height: 60

      background: Rectangle{
        border.width: 3
        border.color: "#2c3a47"
        radius: 5
      }

      indicator: Rectangle{
        id: myRadioButtonIndicator_1
        implicitWidth: 40
        implicitHeight: 40
        radius: width / 2
        x: 10
        y: ((myRadioButton_1.height - myRadioButtonIndicator_1.height) / 2)
        color: myRadioButton_1.checked ? "#eab543" : "transparent"
        anchors.margins: 5
        border.color: "#b33771"
        border.width: 3
      }

      onCheckedChanged: {
        console.log("Option 1 Status Changed to: ", myRadioButton_1.checked)
      }
    }
    RadioButton{
      id: myRadioButton_2
      text: "Option 2"
      font.pointSize: 20
      font.bold: true
      height: 60

      background: Rectangle{
        border.width: 3
        border.color: "#2c3a47"
        radius: 5
      }
      indicator: Rectangle{
        id: myRadioButtonIndicator_2
        implicitWidth: 40
        implicitHeight: 40
        radius: width / 2
        x: 10
        y: ((myRadioButton_2.height - myRadioButtonIndicator_2.height) / 2)
        color: myRadioButton_2.checked ? "#eab543" : "transparent"
        anchors.margins: 5
        border.color: "#b33771"
        border.width: 3
      }

      onCheckedChanged: {
        console.log("Option 2 Status Changed to: ", myRadioButton_2.checked)
      }
    }
    RadioButton{
      id: myRadioButton_3
      text: "Option 3"
      font.pointSize: 20
      font.bold: true
      height: 60

      background: Rectangle{
        border.width: 3
        border.color: "#2c3a47"
        radius: 5
      }

      indicator: Rectangle{
        id: myRadioButtonIndicator_3
        implicitWidth: 40
        implicitHeight: 40
        radius: width / 2
        x: 10
        y: ((myRadioButton_3.height - myRadioButtonIndicator_3.height) / 2)
        color: myRadioButton_3.checked ? "#eab543" : "transparent"
        anchors.margins: 5
        border.color: "#b33771"
        border.width: 3
      }

      onCheckedChanged: {
        console.log("Option 3 Status Changed to: ", myRadioButton_3.checked)
      }
    }
  }
}
