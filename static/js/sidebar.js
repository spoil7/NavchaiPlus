document.addEventListener("DOMContentLoaded", () => {

    const groups = document.querySelectorAll(".menu-group");

    groups.forEach(group => {

        const button = group.querySelector(".menu-group-toggle");

        button.addEventListener("click", () => {

            if (group.classList.contains("open")) {
                group.classList.remove("open");
                return;
            }

            groups.forEach(item => item.classList.remove("open"));

            group.classList.add("open");

        });

    });

});