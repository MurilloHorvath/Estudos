import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5
import QtQuick.Layouts 1.3

Window {
  width: 640
  height: 480
  visible: true
  title: qsTr("Tutorial 30 SwipeView Control")

  SwipeView {
    id: mySwipeView
    anchors.fill: parent
    currentIndex: 0

    orientation: Qt.Horizontal

    Page_1 {}
    Page_2 {}
    Page_3 {}
  }

  PageIndicator {
    id: myIndicator
    count: mySwipeView.count
    currentIndex: mySwipeView.currentIndex

    anchors.bottom: mySwipeView.bottom
    anchors.horizontalCenter: parent.horizontalCenter

    interactive: true

    onCurrentIndexChanged: {
      mySwipeView.currentIndex = currentIndex
    }
  }
}
