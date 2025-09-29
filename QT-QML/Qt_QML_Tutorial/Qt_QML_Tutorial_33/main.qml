import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.3
import "."

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Tutorial 33 Dark mode and light mode in application")

    AppTheme{
        id: appTheme
    }

    Component.onCompleted: appTheme.setLightTheme()

    Rectangle{
        width: parent.width
        height: parent.height
        color: appTheme.backgroundcolor

        Switch{
            id:themeSwitch
            text: themeSwitch.checked ? "Dark Mode" : "Light Mode"
            anchors.top: parent.top
            checked: false
            anchors.horizontalCenter: parent.horizontalCenter

            contentItem: Text {
                text: themeSwitch.text
                color: appTheme.textcolor
                verticalAlignment: Text.AlignVCenter
                leftPadding: themeSwitch.indicator.width + themeSwitch.spacing
                font.pointSize: 15
            }

            onCheckedChanged:{
                if(checked){
                    appTheme.setDarkTheme()
                }
                else{
                    appTheme.setLightTheme()
                }
            }
        }

        ColumnLayout{
            anchors.centerIn: parent
            Text {
                id: myText
                text: qsTr("teste dark mode and light mode")
                Layout.preferredWidth: 200
                Layout.preferredHeight: 100
                Layout.alignment: Qt.AlignHCenter
                color: appTheme.textcolor
                font.pointSize: 20
            }

            Button{
                id: myButton
                Layout.preferredWidth: 200
                Layout.preferredHeight: 100
                Layout.alignment: Qt.AlignHCenter

                Text {
                    text: "teste"
                    color: appTheme.buttontextcolor
                    anchors.fill: parent
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }

                background: Rectangle{
                    color: appTheme.buttonbackgroundcolor
                    radius: 20
                }
            }
        }
    }
}
