// know we can write javascript code
// to add functionality in it for expanding

const ExpandingFlexCard = document.querySelectorAll(".expanding-flex-cards");

ExpandingFlexCard.forEach((efEl) => {
    efEl
        .querySelectorAll(".expanding-flex-cards-item:not(active)")
        .forEach((item) => {
            item.addEventListener("click", function (e) {
                e.preventDefault();
                efEl
                    .querySelector(".expanding-flex-cards-item.active")
                    .classList.remove("active");
                this.classList.add("active");
            });
        });
});