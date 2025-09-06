import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 04 ComboBox Control")

  ComboBox{
    id: myComboBox
    width: 400
    height: 70
    anchors.centerIn: parent
    currentIndex: 0
    model: myComboboxListModel

    ListModel{
      id: myComboboxListModel
      ListElement{key: "Option 1"}
      ListElement{key: "Option 2"}
      ListElement{key: "Option 3"}
      ListElement{key: "Option 4"}
    }

    contentItem: Text {
      color: "#FFFFFF"
      text: myComboBox.displayText
      font.pointSize: 16
      font.bold: true
      verticalAlignment: Text.AlignVCenter
      horizontalAlignment: Text.AlignHCenter
    }

    delegate: ItemDelegate{
      width: myComboBox.width
      background: Rectangle{
        color: "#e1b12c"
        radius: 0
      }
      contentItem: Text{
        color: "#4cd137"
        text: modelData
        font.pointSize: 14
        font.bold: true
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
      }
    }

    onActivated: {
      console.log("Selected Text : ", myComboBox.currentText)
      console.log("Selected Index : ", myComboBox.currentIndex)
    }

    background: Rectangle{
      gradient: Gradient{
        GradientStop {position: 0.0; color:"#e84118"}
        GradientStop {position: 1.0; color:"#2f3640"}
      }
      radius: 10
    }
  }
}
