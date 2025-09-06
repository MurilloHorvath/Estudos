import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3
    

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 14")

    Column{
        Button{
            id: myBytton
            text: "Click"
            onClicked:{
                myColorDialog.open()
            }
        }
        Rectangle {
            id: myRect
            width: 200
            height: 200
        }
    }

    ColorDialog{
        id: myColorDialog
        title: "select color"
        onAccepted:{
            myRect.color = myColorDialog.color
        }
    }
}
