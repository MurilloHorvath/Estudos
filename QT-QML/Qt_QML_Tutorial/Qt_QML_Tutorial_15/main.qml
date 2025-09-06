import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 15 File Dialog")

    Button{
        id: myButton
        text:"click"
        onClicked:{
            myFileDialog.open()
        }
    }

    FileDialog{
        id:myFileDialog
        folder: shortcuts.pictures
        modality: Qt.applicationModal
        selectMultiple: true
        nameFilters: ["Images file (*.jpg *.png)"]
        onAccepted:{
            console.log(fileUrl)
            console.log(fileUrls)
        }
    }
}
