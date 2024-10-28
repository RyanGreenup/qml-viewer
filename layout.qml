import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "QML Layout with Sidebars"

    RowLayout {
        anchors.fill: parent

        ColumnLayout {
            Layout.fillHeight: true
            Layout.preferredWidth: 200 // Width for the left sidebar

            // First Sidebar: List with a Search Bar
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
                }
            }
        }

        ColumnLayout {
            Layout.fillHeight: true
            Layout.preferredWidth: 200 // Width for the center sidebar

            // Second Sidebar: Simulated Tree Structure
            TextField {
                placeholderText: "Search Tree (Simulated)"
                Layout.fillWidth: true
            }

            // For demonstration, a nested list to simulate a tree structure
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
                    }

                    // Simulate sub-items indentation
                    ListView {
                        visible: index === 3 // Display sub-items only for "Child 3"
                        model: ListModel {
                            ListElement { name: "Subchild 3.1" }
                            ListElement { name: "Subchild 3.2" }
                        }
                        delegate: Text {
                            text: "    " + model.name // Indent sub-items
                        }
                    }
                }
            }
        }

        ColumnLayout {
            Layout.fillHeight: true
            Layout.preferredWidth: 200 // Width for the right sidebar

            // Third Sidebar: Another List with a Search Bar
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
                }
            }
        }

        ColumnLayout {
            Layout.fillHeight: true
            Layout.preferredWidth: 200 // Width for the right side fields

            // Right Side Text Fields
            TextField {
                placeholderText: "Small Text Field"
                Layout.fillWidth: true
                Layout.preferredHeight: 40 // Smaller height for the top field
            }

            TextArea {
                placeholderText: "Large Text Area"
                Layout.fillWidth: true
                Layout.fillHeight: true // Takes remaining space
                Layout.minimumHeight: 80 // Minimum height for usability
            }
        }
    }
}

