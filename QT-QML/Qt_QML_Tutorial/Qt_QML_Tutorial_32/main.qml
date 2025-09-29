import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 32 Image")

    Image {
        id: myDrone1
        source: "qrc:/images/drone1.jpeg"
        width: parent.width
        height: parent.height
        //mirror: true
        //mirrorVercally: true
        //sourceClipRect: Qt.rect(10,10,100,100)
        //smooth: true
        //mipmap:true
        //fillMode: Image.PreserveAspectFit
        //fillMode: Image.Tile
        //fillMode: Image.TileHorizontally
        //fillMode: Image.TileVertically
    }
}
