import QtQuick
import QtQuick.Window
import QtQuick.Controls

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 09 Switch Control")

  Switch{
    id: mySwich
    text: qsTr("Switch")

    indicator: Rectangle{
      implicitWidth: 50
      implicitHeight: 25
      x: mySwich.leftPadding
      y: parent.height / 2 - height / 2
      radius: 15
      color: mySwich.checked ? "#341f97" : "#ffffff"
      border.color: mySwich.checked ? "#341f97" : "#222f3e"

      Rectangle{
        x: mySwich.checked ? parent.width - width : 0
        width: 25
        height: 25
        radius: 15
        color: mySwich.down ? "#222f3e" : "#ffffff"
        border.color: mySwich.checked ? (mySwich.down ? "#341f97" : "#ff9f43" ) : "#888888"
      }
    }

    contentItem: Text{
      text: mySwich.text
      //font: mySwich.font
      font.pointSize: 20
      color: mySwich.down ? "#00d2d3" : "#2e86de"
      verticalAlignment: Text.AlignVCenter
      leftPadding: mySwich.indicator.width + mySwich.spacing
    }

    onCheckedChanged: {
      console.log("Switch value : ", checked)
    }
  }
}
