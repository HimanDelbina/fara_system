var tabButtons = document.querySelectorAll(".sec_tab_top .button_container button");
var tabPanels = document.querySelectorAll(".sec_tab_down .tab_panel");



function showPanel(panelIndex, colorCode) {
    tabButtons.forEach(function (node) {
        // node.style.backgroundColor = "";
        node.style.color = "";
        node.style.fontWeight = "";
    });
    // tabButtons[panelIndex].style.backgroundColor = colorCode;
    tabButtons[panelIndex].style.color = "black";
    tabButtons[panelIndex].style.fontWeight = "bold";
    tabPanels.forEach(function (node) {
        node.style.display = "none";
    });
    tabPanels[panelIndex].style.display = "block";
    tabPanels[panelIndex].style.backgroundColor =colorCode;
}
showPanel(2,'#FFFFFF')