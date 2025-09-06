import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("tutorial 17 Property Animation")

    Rectangle{
        id: myRectangle1
        width: 100
        height: 100
        color: "#FF0000"

        PropertyAnimation on x{
            from: 0
            to: width - myRectangle1.width
            duration: 2000
            easing.type: Easing.InBounce
        }
    }

    Rectangle{
        id: myRectangle2
        width: 100
        height: 100
        color: "#00FF00"

        PropertyAnimation on y{
            from: 0
            to: height - myRectangle2.height
            duration: 2000
            easing.type: Easing.OutBounce
        }
    }
    Rectangle{
        id: myRectangle3
        width: 100
        height: 100
        color: "#0000FF"

        anchors.centerIn: parent

        PropertyAnimation on rotation {
            from: 0
            to: 360
            loops: Animation.Infinite
            duration: 2000
            easing.type: Easing.InOutBounce
        }
    }
}
