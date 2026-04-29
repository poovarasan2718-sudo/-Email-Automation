document.getElementById("form").addEventListener("submit", function(e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const subject = document.getElementById("subject").value;
    const message = document.getElementById("message").value;

    const result = document.getElementById("result");
    result.innerText = "Sending...";

    fetch("/send", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            subject: subject,
            message: message
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            result.innerText = "✅ " + data.message;
        } else {
            result.innerText = "❌ " + data.message;
        }
    })
    .catch(() => {
        result.innerText = "❌ Error sending email";
    });
});