import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15

Window{
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 08 SpinBox Control")

  SpinBox{
    id: mySpinBox
    anchors.centerIn: parent
    from: 0
    to: 100
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
      color: "lightsteelblue"
      border.color: "darkblue"
      border.width: 2
      radius: 25
    }
  }
}
