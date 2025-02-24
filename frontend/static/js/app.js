document.getElementById("resume-form").addEventListener("submit", async (event) => {
    event.preventDefault(); // Stop form from reloading page

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        skills: document.getElementById("skills").value,
        experience: document.getElementById("experience").value,
        education: document.getElementById("education").value,
        template: document.getElementById("template").value
    };

    console.log("DEBUG: Sending JSON Data ->", JSON.stringify(data));

    try {
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",  // ✅ Set proper Content-Type
            },
            body: JSON.stringify(data)
        });

        console.log("DEBUG: Response Status ->", response.status);

        if (response.ok) {
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement("a");
            link.href = url;
            link.download = "resume.pdf";
            link.click();
        } else {
            const errorText = await response.text();
            console.error("DEBUG: Server Error ->", errorText);
            document.getElementById("output").innerText = `Error: ${errorText}`;
        }
    } catch (error) {
        console.error("DEBUG: Fetch Error ->", error);
        document.getElementById("output").innerText = `Error: ${error.message}`;
    }
});
