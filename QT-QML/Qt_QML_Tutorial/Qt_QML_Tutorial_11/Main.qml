import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 11 ProgressBar Control")

  Column{
    spacing: 20
    anchors.centerIn: parent

    ProgressBar{
      id: myProgressBar
      width: 300
      value: 75
      from: 0
      to: 750

      onValueChanged: {
        console.log("progressBar Valeu : ", value)
      }
    }

    Row{
      spacing: 20
      Button{
        id: myButton_Inc
        text: "Increase"
        onClicked: {
          if(myProgressBar.value < myProgressBar.to){
            myProgressBar.value += 15
          }
        }
      }
      Button{
        id: myButton_Dec
        text: "Decrease"
        onClicked: {
          if(myProgressBar.value > myProgressBar.from){
            myProgressBar.value -= 15
          }
        }
      }
    }

    Text {
      id: myText
      text: "Progress: " + Math.round((myProgressBar.value * 100) / myProgressBar.to) + " %"
      font.pointSize: 15
    }
  }
}
