import QtQuick

Window {
  id: janela
  width: 740
  height: 740
  visible: true
  title: qsTr("First APP")

  Rectangle {
    id: page
    anchors.fill: parent

    Text {
      id: texto
      anchors.horizontalCenter: page.horizontalCenter
      y: 30
      font.pointSize: 24
      font.bold: true
      text: qsTr("First APP")

      MouseArea {
        id: mouseArea
        anchors.fill: parent
      }
      states: State {
        name: "down"
        when: mouseArea.pressed === true
        PropertyChanges {
          texto {
            y: 30
            rotation: 180
            color: "red"
          }
        }
      }
      transitions: Transition {
        from: ""
        to: "down"
        reversible: true
        ParallelAnimation {

          NumberAnimation {
            properties: "y,rotation"
            duration: 500
            easing.type: Easing.InOutQuad
          }
          ColorAnimation {
            duration: 500
          }
        }
      }
    }
  }
  Grid {
    id: colorPicker
    x: 4
    anchors.bottom: page.bottom
    anchors.bottomMargin: 4
    rows: 2
    columns: 3
    spacing: 3

    Cell {
      cellColor: "red"
      onClicked: texto.color = cellColor
    }
    Cell {
      cellColor: "green"
      onClicked: texto.color = cellColor
    }
    Cell {
      cellColor: "blue"
      onClicked: texto.color = cellColor
    }
    Cell {
      cellColor: "yellow"
      onClicked: texto.color = cellColor
    }
    Cell {
      cellColor: "steelblue"
      onClicked: texto.color = cellColor
    }
    Cell {
      cellColor: "black"
      onClicked: texto.color = cellColor
    }
  }
}
