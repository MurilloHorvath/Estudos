import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 31 Resource Collection FIles (.qrc)")


    Image {
        id: myDrone1
        source: "qrc:/images/drone1.jpeg"
        width: parent.width
        height: parent.height
    }
}
