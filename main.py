from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
URL = "https://whatsapp.com/channel/0029VbByKJx7j6g3ipNHh23N"

@app.route('/cek')
def cek_channel():
    try:
        res = requests.get(URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        page_text = soup.get_text()
        
        has_divine = "divine" in page_text.lower()
        has_eternal = "eternal" in page_text.lower()
        
        return jsonify({
            "status": "success",
            "text": page_text[:500], # Mengambil cuplikan pesan
            "alarm": has_divine or has_eternal,
            "trigger": "Divine/Eternal Ditemukan" if (has_divine or has_eternal) else "Aman"
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
