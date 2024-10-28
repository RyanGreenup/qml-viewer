import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "QML Layout with Sidebars"

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        // Container for padding
        Rectangle {
            Layout.fillWidth: true
            color: "transparent"
            // Use implicit height to accommodate its children
            implicitHeight: rowLayout.implicitHeight
            RowLayout {
                id: rowLayout
                anchors.fill: parent
                spacing: 10

                // Top Search Bar
                TextField {
                    placeholderText: "Global Search"
                    Layout.fillWidth: true
                }

                // Dropdown Dialog
                ComboBox {
                    Layout.preferredWidth: 150
                    model: ["Option 1", "Option 2", "Option 3"]
                }
            }
        }

        SplitView {
            Layout.fillWidth: true
            Layout.fillHeight: true
            orientation: Qt.Horizontal

            // First Sidebar
            Item {
                implicitWidth: 0
                SplitView.preferredWidth: 200
                SplitView.minimumWidth: 50

                ColumnLayout {
                    anchors.fill: parent
                    // First Sidebar content (unchanged)
                    TextField {
                        placeholderText: "Search List 1"
                        Layout.fillWidth: true
                    }
                    ListView {
                        Layout.fillHeight: true
                        model: ListModel {
                            ListElement { name: "Item 1" }
                            ListElement { name: "Item 2" }
                            ListElement { name: "Item 3" }
                        }
                        delegate: Text {
                            text: model.name
                            padding: 8
                        }
                    }
                }
            }

            // Second Sidebar
            Item {
                implicitWidth: 0
                SplitView.preferredWidth: 200
                SplitView.minimumWidth: 50

                ColumnLayout {
                    anchors.fill: parent
                    // Second Sidebar content (unchanged)
                    TextField {
                        placeholderText: "Search Tree (Simulated)"
                        Layout.fillWidth: true
                    }
                    ListView {
                        Layout.fillHeight: true
                        model: ListModel {
                            ListElement { name: "Root" }
                            ListElement { name: "Child 1" }
                            ListElement { name: "Child 2" }
                            ListElement { name: "Child 3" }
                        }
                        delegate: Column {
                            Text {
                                text: model.name
                                padding: 8
                            }
                            ListView {
                                visible: index === 3
                                model: ListModel {
                                    ListElement { name: "Subchild 3.1" }
                                    ListElement { name: "Subchild 3.2" }
                                }
                                delegate: Text {
                                    text: "    " + model.name
                                    padding: 8
                                }
                            }
                        }
                    }
                }
            }

            // Third Sidebar
            Item {
                implicitWidth: 0
                SplitView.preferredWidth: 200
                SplitView.minimumWidth: 50

                ColumnLayout {
                    anchors.fill: parent
                    // Third Sidebar content (unchanged)
                    TextField {
                        placeholderText: "Search List 2"
                        Layout.fillWidth: true
                    }
                    ListView {
                        Layout.fillHeight: true
                        model: ListModel {
                            ListElement { name: "Item A" }
                            ListElement { name: "Item B" }
                            ListElement { name: "Item C" }
                        }
                        delegate: Text {
                            text: model.name
                            padding: 8
                        }
                    }
                }
            }

            // Right Side Text Fields (unchanged)
            ColumnLayout {
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.minimumWidth: 200

                TextField {
                    placeholderText: "Small Text Field"
                    Layout.fillWidth: true
                    Layout.preferredHeight: 40
                }

                TextArea {
                    placeholderText: "Large Text Area"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    Layout.minimumHeight: 80
                }
            }
        }
    }
}

