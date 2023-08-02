document.querySelectorAll(".preview-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        const previewUrl = btn.getAttribute("data-preview-url");
        if (previewUrl) {
            const audioElement = new Audio(previewUrl);
            audioElement.play();
        }
    });
});