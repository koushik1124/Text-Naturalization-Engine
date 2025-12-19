async function humanizeText() {
  const inputText = document.getElementById("inputText").value;
  const tone = document.getElementById("tone").value;
  const outputText = document.getElementById("outputText");

  if (inputText.trim().length < 20) {
    alert("Please enter at least 20 characters.");
    return;
  }

  outputText.value = "Processing...";

  try {
    const response = await fetch("http://127.0.0.1:8000/humanize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: inputText,
        tone: tone
      })
    });

    const data = await response.json();
    outputText.value = data.humanized_text;

  } catch (error) {
    outputText.value = "Error connecting to backend.";
    console.error(error);
  }
}
