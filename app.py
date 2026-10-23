from flask import Flask, request, session, redirect
import sqlite3, random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "final_exact_opay"
DB = "bank.db"
def get_db():
    c = sqlite3.connect(DB)
    c.row_factory = sqlite3.Row
    return c
con = sqlite3.connect(DB)
con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, fullname TEXT, acct TEXT UNIQUE, phone TEXT, pin TEXT, balance REAL)")
con.execute("CREATE TABLE IF NOT EXISTS trans (id INTEGER PRIMARY KEY, sender TEXT, recv TEXT, rname TEXT, amount REAL, bank TEXT, tdate TEXT, status TEXT, trx_id TEXT, sess_id TEXT)")
try:
    if not con.execute("SELECT * FROM users WHERE acct='1000000001'").fetchone():
        con.execute("INSERT INTO users (fullname,acct,phone,pin,balance) VALUES (?,?,?,?,?)", ("ABDULRAHMAN","1000000001","08011111111","123456",32.87))
except:
    pass
con.commit()
con.close()
def page(body):
    return f"""
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box;font-family:Inter,sans-serif}}
body{{background:#e9ecea;display:flex;justify-content:center}}
.phone{{width:100%;max-width:390px;background:#f7f8f7;min-height:100vh;position:relative;padding-bottom:90px}}
.status{{background:#00a85f;color:#fff;display:flex;justify-content:space-between;padding:14px 20px 6px;font-size:14px;font-weight:600}}
.green{{background:#00a85f;padding:10px 18px 46px;color:#fff;border-radius:0 0 26px 26px}}
.hi{{font-weight:800;font-size:15px}}.bal-lbl{{font-size:15px;margin-top:10px;font-weight:600}}
.bal-num{{font-size:38px;font-weight:900;margin-top:2px}}
.add{{position:absolute;right:18px;top:96px;background:#fff;color:#00a85f;border-radius:24px;padding:9px 16px;font-weight:800;font-size:14px;border:none;box-shadow:0 4px 12px rgba(0,0,0,.15)}}
.white-actions{{margin:-28px 12px 0;background:#fff;border-radius:20px;display:flex;justify-content:space-around;padding:18px 8px;box-shadow:0 8px 24px rgba(0,0,0,.08)}}
.a{{text-align:center}}.a-ic{{width:54px;height:54px;border-radius:16px;background:#e7f6ec;display:flex;align-items:center;justify-content:center;margin:0 auto 8px;color:#00a85f;font-size:24px;font-weight:900}}
.a-txt{{font-size:13px;font-weight:700}}
.card{{background:#fff;margin:14px 12px 0;border-radius:18px;padding:14px}}
.t-head{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}}
.t-title{{font-weight:800;font-size:15px}}.see{{color:#00a85f;font-size:12px;font-weight:700}}
.tr{{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid #f1f1f1}}
.tr-l{{display:flex;gap:10px;align-items:center}}
.tr-ico{{width:38px;height:38px;border-radius:50%;background:#e6f5eb;display:flex;align-items:center;justify-content:center;color:#00a85f;font-weight:900}}
.tr-name{{font-weight:700;font-size:13.5px}}.tr-sub{{font-size:11.5px;color:#777;margin-top:2px}}.tr-amt{{font-weight:800;font-size:13.5px}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px 4px}}
.g{{text-align:center}}.g-ic{{width:48px;height:48px;border-radius:14px;margin:0 auto 6px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#fff;font-weight:800}}
.g-t{{font-size:11px;font-weight:600;color:#222}}
.christ{{background:#0a7a46;border-radius:16px;color:#fff;padding:14px;display:flex;justify-content:space-between;align-items:center}}
.bottom{{position:fixed;bottom:0;left:50%;transform:translateX(-50%);width:100%;max-width:390px;background:#fff;display:flex;justify-content:space-around;padding:10px 0 16px;border-top:1px solid #eee}}
.b{{text-align:center;font-size:11px;color:#888}}.b.active{{color:#00a85f;font-weight:800}}
.inp{{width:100%;padding:14px;border:1px solid #e0e0e0;border-radius:12px;margin-top:10px;font-size:14px}}
.btn{{width:100%;padding:14px;background:#00a85f;color:#fff;border:none;border-radius:12px;margin-top:14px;font-weight:800;font-size:15px}}
</style></head><body><div class='phone'>{body}
<div class='bottom'><div class='b active'>Home</div><div class='b'>Rewards</div><div class='b'>Finance</div><div class='b'>Cards</div><div class='b'>Me</div></div></div></body></html>
"""
@app.route("/")
def r(): return redirect("/signup")
@app.route("/signup")
def signup():
    b = "<div style='background:#00a85f;min-height:100vh;padding:22px;display:flex;align-items:center'><div style='background:#fff;width:100%;border-radius:22px;padding:22px'><h2 style='color:#00a85f'>AB BANK</h2><p style='font-size:13px;color:#666;margin:8px 0'>Create Account - 3 fields only</p><form method='POST' action='/dosignup'><input name='fullname' placeholder='Full Name e.g Abdulrahman' required class='inp'><input name='phone' placeholder='Phone Number' required class='inp'><input name='pin' type='password' placeholder='Create PIN e.g 123456' required class='inp'><button class='btn'>CREATE ACCOUNT + N2000 BONUS</button></form><p style='text-align:center;margin-top:12px;font-size:13px'><a href='/login' style='color:#00a85f'>Already have? Login</a></p></div></div>"
    return page(b)
@app.route("/dosignup", methods=["POST"])
def dosignup():
    fn=request.form["fullname"]; ph=request.form["phone"]; pin=request.form["pin"]
    acct=str(random.randint(1000000000,9999999999))
    con=get_db(); con.execute("INSERT INTO users (fullname,acct,phone,pin,balance) VALUES (?,?,?,?,?)",(fn,acct,ph,pin,2000)); con.commit(); con.close()
    b = f"<div style='background:#00a85f;min-height:100vh;padding:22px;display:flex;align-items:center'><div style='background:#fff;width:100%;border-radius:22px;padding:22px;text-align:center'><h3>Account Created!</h3><p>{fn}</p><div style='background:#eaf8ef;padding:12px;border-radius:12px;margin:12px 0'><div>Account No</div><div style='font-size:22px;font-weight:900;color:#00a85f'>{acct}</div><div>N2000 Bonus</div></div><a href='/login' style='display:block;background:#00a85f;color:#fff;padding:14px;border-radius:12px;text-decoration:none;font-weight:800'>Login Now</a></div></div>"
    return page(b)
@app.route("/login")
def login():
    b = "<div style='background:#00a85f;min-height:100vh;padding:22px;display:flex;align-items:center'><div style='background:#fff;width:100%;border-radius:22px;padding:22px'><h2>Login</h2><p style='font-size:12px;color:#666'>Demo: 1000000001 / 123456 = N32.87</p><form method='POST' action='/dologin'><input name='acct' value='1000000001' required class='inp'><input name='pin' type='password' value='123456' required class='inp'><button class='btn'>LOGIN</button></form></div></div>"
    return page(b)
@app.route("/dologin", methods=["POST"])
def dologin():
    a=request.form["acct"]; p=request.form["pin"]
    con=get_db(); u=con.execute("SELECT * FROM users WHERE acct=? AND pin=?",(a,p)).fetchone(); con.close()
    if not u: return page("<div style='padding:40px;text-align:center'>Wrong PIN<br><a href='/login'>Back</a></div>")
    session["uid"]=u["id"]; session["acct"]=u["acct"]
    return redirect("/dashboard")
@app.route("/dashboard")
def dashboard():
    if "uid" not in session: return redirect("/login")
    con=get_db(); u=con.execute("SELECT * FROM users WHERE id=?",(session["uid"],)).fetchone(); tx=con.execute("SELECT * FROM trans WHERE sender=? ORDER BY id DESC LIMIT 5",(u["acct"],)).fetchall(); con.close()
    bal="{:,.2f}".format(u["balance"]); name=(u["fullname"] or "ABDULRAHMAN").upper()
    if tx:
        rows=""
        for t in tx:
            col="#e00000" if "Failed" in t["status"] else "#00a85f"
            amt_txt=f"- N{t['amount']:,.2f}" if "Failed" in t["status"] or True else f"N{t['amount']}"
            rows+=f"<div class='tr' onclick=location.href='/receipt/{t['id']}'><div class='tr-l'><div class='tr-ico'>↓</div><div><div class='tr-name'>{t['rname']}</div><div class='tr-sub'>{t['tdate']} • {t['status']}</div></div></div><div class='tr-amt' style='color:{col}'>{amt_txt}</div></div>"
    else:
        rows="""
<div class='tr'><div class='tr-l'><div class='tr-ico'>↓</div><div><div class='tr-name'>Transfer to Chinedu</div><div class='tr-sub'>Today • 10:24 AM • Successful</div></div></div><div class='tr-amt' style='color:#e00000'>- N5,000.00</div></div>
<div class='tr'><div class='tr-l'><div class='tr-ico'>↑</div><div><div class='tr-name'>Transfer from Aisha</div><div class='tr-sub'>Yesterday • 04:12 PM • Successful</div></div></div><div class='tr-amt' style='color:#00a85f'>+ N10,000.00</div></div>
"""
    body = f"""
<div class='status'><span>9:41</span><span>📶 85</span></div>
<div class='green'><div class='hi'>HI, {name}</div><div class='bal-lbl'>Available Balance</div><div class='bal-num'>N{bal}</div><button class='add' onclick=location.href='/add'>+ Add Money</button></div>
<div class='white-actions'>
<div class='a' onclick=location.href='/to_bank'><div class='a-ic'>☰</div><div class='a-txt'>To AB</div></div>
<div class='a' onclick=location.href='/to_bank'><div class='a-ic'>🏛</div><div class='a-txt'>To Bank</div></div>
<div class='a' onclick=location.href='/to_bank'><div class='a-ic'>⬇</div><div class='a-txt'>Withdraw</div></div>
</div>
<div class='card'><div class='t-head'><div class='t-title'>Transaction History</div><div class='see'>See all ></div></div>{rows}</div>
<div class='card'><div class='grid'>
<div class='g'><div class='g-ic' style='background:#ffcc2a'>📞</div><div class='g-t'>Airtime</div></div>
<div class='g'><div class='g-ic' style='background:#3b82f6'>📱</div><div class='g-t'>Data</div></div>
<div class='g'><div class='g-ic' style='background:#fb923c'>🏈</div><div class='g-t'>Data</div></div>
<div class='g'><div class='g-ic' style='background:#fb923c'>📺</div><div class='g-t'>Betting</div></div>
<div class='g'><div class='g-ic' style='background:#fdba74'>TV</div><div class='g-t'>TV</div></div>
<div class='g'><div class='g-ic' style='background:#60a5fa'>🛡</div><div class='g-t'>SafeBox</div></div>
<div class='g'><div class='g-ic' style='background:#60a5fa'>⚙</div><div class='g-t'>SafeBox</div></div>
<div class='g'><div class='g-ic' style='background:#4ade80'>🐖</div><div class='g-t'>Spend & Save</div></div>
<div class='g'><div class='g-ic' style='background:#c084fc'>🎁</div><div class='g-t'>Invitation</div></div>
<div class='g'><div class='g-ic' style='background:#e5e7eb;color:#555'>•••</div><div class='g-t'>More</div></div>
</div></div>
<div class='card' style='padding:0;overflow:hidden;border:none'><div class='christ'><div><div style='font-weight:900'>❄ Christmas Target</div><div style='font-size:11px;margin-top:4px'>Save towards Christmas 🎄 • Target: N50,000 • 28% saved</div></div><div style='font-size:26px'>🎁</div></div></div>
"""
    return page(body)
@app.route("/to_bank")
def to_bank():
    b = "<div style='background:#fff;padding:14px'><span onclick=location.href='/dashboard'><b>← Back</b></span> <b style='margin-left:10px'>To Bank</b></div><div class='card'><div style='background:#eaf8ef;padding:10px;border-radius:10px;font-size:12px;color:#0a7a46'><b>Logic:</b> Balance >= Amount = Successful<br>Balance < Amount = Declined<br>Both show REAL Transaction ID + Session ID + Date/Time</div><form method='POST' action='/dotransfer'><input name='acct' placeholder='Account Number (10 digits)' required class='inp'><select name='bank' class='inp'><option>OPay</option><option>UBA</option><option>First Bank</option><option>GTB</option><option selected>AB BANK</option></select><input name='name' placeholder='Beneficiary Name e.g Chinedu' required class='inp'><input name='amount' type='number' step='0.01' placeholder='Amount e.g 10' required class='inp'><button class='btn'>Transfer Now - Generate REAL Receipt</button></form></div>"
    return page(b)
@app.route("/dotransfer", methods=["POST"])
def dotransfer():
    if "uid" not in session: return redirect("/login")
    recv=request.form["acct"]; bank=request.form["bank"]; rname=request.form["name"]; amt=float(request.form["amount"] or 0)
    con=get_db(); u=con.execute("SELECT * FROM users WHERE id=?",(session["uid"],)).fetchone()
    now=datetime.now(); tdate=now.strftime("%d %b %Y, %I:%M:%S %p")
    trx_id=now.strftime("%Y%m%d")+str(random.randint(10000000,99999999))+str(random.randint(1000,9999))
    sess_id=str(random.randint(1000000000000000,9999999999999999))+str(random.randint(100000000000,999999999999))
    if u["balance"]>=amt and amt>0:
        status="Successful"; con.execute("UPDATE users SET balance=balance-? WHERE id=?",(amt,session["uid"]))
    else:
        status="Failed - Declined - Insufficient Funds"
    con.execute("INSERT INTO trans (sender,recv,rname,amount,bank,tdate,status,trx_id,sess_id) VALUES (?,?,?,?,?,?,?,?,?)",(u["acct"],recv,rname,amt,bank,tdate,status,trx_id,sess_id))
    tid=con.execute("SELECT last_insert_rowid()").fetchone()[0]
    con.commit(); con.close()
    return redirect(f"/receipt/{tid}")
@app.route("/receipt/<int:tid>")
def receipt(tid):
    con=get_db(); t=con.execute("SELECT * FROM trans WHERE id=?",(tid,)).fetchone(); con.close()
    if not t: return redirect("/dashboard")
    ok="Successful" in t["status"]; color="#00a85f" if ok else "#d32f2f"; icon="✓" if ok else "✕"
    b = f"""
<div style='background:#fff;min-height:100vh;padding:20px;text-align:center'>
<div style='width:78px;height:78px;background:{color};border-radius:50%;margin:28px auto;display:flex;align-items:center;justify-content:center;color:#fff;font-size:36px;font-weight:900'>{icon}</div>
<div style='font-weight:800;font-size:15px'>{t['status']}</div>
<div style='font-size:36px;font-weight:900;margin-top:10px'>N{t['amount']:,.2f}</div>
<div style='color:#666;font-size:13px;margin-top:6px'>To {t['rname']} - {t['bank']}</div>
<div style='background:#f9fafb;border-radius:18px;padding:16px;margin-top:24px;text-align:left;font-size:13px;border:1px solid #eee'>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Beneficiary</span><b>{t['rname']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Account Number</span><b>{t['recv']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Bank</span><b>{t['bank']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Amount</span><b>N{t['amount']:,.2f}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Date & Time</span><b style='font-size:11px'>{t['tdate']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Transaction ID</span><b style='font-size:11px'>{t['trx_id']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0;border-bottom:1px solid #eee'><span style='color:#777'>Session ID</span><b style='font-size:9px;word-break:break-all'>{t['sess_id']}</b></div>
<div style='display:flex;justify-content:space-between;padding:11px 0'><span style='color:#777'>Status</span><b style='color:{color}'>{t['status']}</b></div>
</div>
<button onclick=location.href='/dashboard' style='width:100%;padding:15px;background:{color};color:#fff;border:none;border-radius:12px;margin-top:16px;font-weight:800'>Done</button>
</div>
"""
    return page(b)
@app.route("/add")
def add():
    if "uid" not in session: return redirect("/login")
    con=get_db(); con.execute("UPDATE users SET balance=balance+5000 WHERE id=?",(session["uid"],)); con.commit(); con.close()
    return redirect("/dashboard")
@app.route("/airtime")
@app.route("/data")
@app.route("/betting")
@app.route("/tv")
@app.route("/safebox")
@app.route("/spend")
@app.route("/invitation")
@app.route("/more")
@app.route("/rewards")
@app.route("/finance")
@app.route("/cards")
@app.route("/me")
def generic():
    return page("<div class='card' style='margin-top:40px;text-align:center'><h3>Feature Working</h3><br><a href='/dashboard'>Back</a></div>")
import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
