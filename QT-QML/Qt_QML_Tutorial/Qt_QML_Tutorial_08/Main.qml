import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 08")

  SpinBox{
    id: mySpinBox
    anchors.centerIn: parent
    from: 0 // valor minimo
    to: 100// valor maximo
    stepSize: 10
    editable: true
    width: 200
    height: 50

    validator: IntValidator{
      bottom: mySpinBox.from
      top: mySpinBox.to
    }

    onValueChanged: {
      console.log("SpinBox Value Is : ", mySpinBox.value)
    }

    background: Rectangle{
      border.color: "#1e272e"
      border.width: 5
      radius: 25
    }
  }
}

