async function checkAttendance() {
  const name = document.getElementById("name").value;
  const attendance = document.getElementById("attendance").value;

  const response = await fetch("http://localhost:8000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, attendance })
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.result;
}
