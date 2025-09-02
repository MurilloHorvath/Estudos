import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Dialogs

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 14")

  Button{
    id: myButton
    text: "click"
    font: myFontDialog.font
    onClicked: {
      myFontDialog.open()
    }
  }

  FontDialog{
    id: myFontDialog
    onAccepted: {
      console.log("Weight : " + myFontDialog.font.weight)
      console.log("Is Bold : " + myFontDialog.font.bold)
      console.log("Is Italic : " + myFontDialog.font.italic)
      console.log("Is Strikeout : " + myFontDialog.font.strikeout)
      console.log("Is underline : " + myFontDialog.font.underline)
      console.log("Family : " + myFontDialog.font.family)
      console.log("Font Size : " + myFontDialog.font.pointSize)
    }
  }
}
