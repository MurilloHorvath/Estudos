import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 05 TextField Control")

  TextField{
    id: myTextField
    width: 500
    height: 50
    anchors.centerIn: parent
    placeholderText: "enter text here"
    font.pointSize: 20

    //validator: RegularExpressionValidator{regularExpression: /[0-9]+/}
    //echoMode: "Password"
    //passwordCharacter: "*"

    color: "#574b90" // set your font color

    onTextChanged: {
      console.log("Text Changed Data; ", myTextField.text)
    }

    background: Rectangle{
      border.color: myTextField.activeFocus ? "#e15f41" : "#c44569"
      border.width: 2
      radius: 5
    }
  }
}
