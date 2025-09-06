import QtQuick
import QtQuick.Window
import QtQuick.Controls
import QtQuick.Dialogs

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 13")

  Row{
    spacing: 20
    anchors.centerIn: parent

    Button{
      id: myButton_Information
      //anchors.centerIn: parent
      text: "information"
      onClicked: {
        myMessageDialog_Information.open()
      }
    }

    Button{
      id: myButton_Warning
      //anchors.centerIn: parent
      text: "warning"
      onClicked: {
        myMessageDialog_Warning.open()
      }
    }

    Button{
      id: myButton_Critical
      //anchors.centerIn: parent
      text: "critical"
      onClicked: {
        myMessageDialog_Critical.open()
      }
    }

    Button{
      id: myButton_Custom
      //anchors.centerIn: parent
      text: "custom"
      onClicked: {
        myMessageDialog_Custom.open()
      }
    }
  }

  MessageDialog{
    id: myMessageDialog_Custom
    text: "Custom Message Dialog Box"
    title: "Qt QML Custom MessageBox"
    //icon: StandardIcon.information
    buttons: MessageDialog.Yes | MessageDialog.No | MessageDialog.Help | MessageDialog.Ok
    onAccepted: {
      console.log("Ok, Button Clicked.")
    }
  }

  MessageDialog{
    id: myMessageDialog_Information
    text: "Information Message Dialog Box"
    title: "Qt QML Information MessageBox"
    //icon: StandardIcon.information
    buttons: MessageDialog.Yes
    onAccepted: {
      console.log("Ok, Button Clicked.")
    }
  }

  MessageDialog{
    id: myMessageDialog_Warning
    text: "Warning Message Dialog Box"
    title: "Qt QML Warning MessageBox"
    //icon: StandardIcon.Warning
    buttons: MessageDialog.Ok
    onAccepted: {
      console.log("Warning Ok, Button Clicked.")
    }
  }

  MessageDialog{
    id: myMessageDialog_Critical
    text: "Critical Message Dialog Box"
    title: "Qt QML Critical MessageBox"
    //icon: StandardIcon.Critical
    buttons: MessageDialog.Ok
    onAccepted: {
      console.log("Critical Ok, Button Clicked.")
    }
  }
}
