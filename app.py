from flask import Flask, request, render_template_string
import sqlite3, os
app = Flask(_name_)
DB='bookings.db'
def init_db():
    con=sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS bookings (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, pickup TEXT, drop_loc TEXT, package TEXT, timing TEXT, start_date TEXT, created TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    con.close()
init_db()

HTML='''
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Azam & Sons - Luxury Coaster Booking Faisalabad</title>
<style>body{font-family:sans-serif;background:#111;color:#fff;margin:0;padding:20px} .card{background:#222;padding:20px;border-radius:15px;max-width:500px;margin:auto;border:1px solid gold} input,select{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:none} button{background:gold;color:#000;padding:14px;width:100%;border:none;border-radius:10px;font-weight:bold;font-size:18px} h1{color:gold;text-align:center}</style></head><body>
<h1>🚌 AZAM & SONS</h1><p style="text-align:center">Faisalabad Luxury Coaster Service</p>
<div class="card">
<form method="POST" action="/book">
<input name="name" placeholder="Naam" required>
<input name="phone" placeholder="Phone / WhatsApp" required>
<input name="pickup" placeholder="Pickup Location" required>
<input name="drop_loc" placeholder="Drop Location" required>
<select name="package"><option>One Way - Faisalabad</option><option>Full Day - 12 Hours</option><option>Wedding Package</option><option>Out of City</option></select>
<select name="timing"><option>Morning</option><option>Evening</option><option>Night</option></select>
<input name="start_date" type="date" required>
<button type="submit">BOOK NOW - WhatsApp Confirm</button>
</form>
</div>
<p style="text-align:center;margin-top:20px">📞 0300-1234567 | Premium 4x4 Coasters</p>
</body></html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/book', methods=['POST'])
def book():
    con=sqlite3.connect(DB)
    con.execute("INSERT INTO bookings (name,phone,pickup,drop_loc,package,timing,start_date) VALUES(?,?,?,?,?,?,?)",
                (request.form['name'],request.form['phone'],request.form['pickup'],request.form['drop_loc'],request.form['package'],request.form['timing'],request.form['start_date']))
    con.commit(); con.close()
    return f"<h1 style='text-align:center;margin-top:50px'>Shukriya {request.form['name']}! Booking Confirm hai. Hum WhatsApp pe rabta karenge. <br><br><a href='/'>Wapas</a></h1>"

if _name_=='_main_':
    app.run(host='0.0.0.0', port=5000)
