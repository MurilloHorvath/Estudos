// version qt 6.2
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Dialogs 1.3

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 16 Folder Dialogs")

    Button{
        id:myButton
        width: 100
        height: 50
        text: "click"
        anchors.centerIn: parent
        onClicked:{
            myFolderDialog.open()
        }
    }
    FolderDialog {
        id:myFolderDialog
        title: "select"
        onAccepted:{
            console.log(myFolderDialog)
        }

    }
}
