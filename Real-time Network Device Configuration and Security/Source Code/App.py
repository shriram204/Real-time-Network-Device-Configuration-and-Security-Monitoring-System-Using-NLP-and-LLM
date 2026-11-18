from flask import Flask, render_template, request from ai_engine import generate_commands
from deploy_config import deploy from monitor import monitor
from scheduler import start_scheduler # ← ADD THIS import io
import sys
app = Flask(	name	)
@app.route("/", methods=["GET", "POST"]) def home():
output = "" commands = ""
if request.method == "POST": intent = request.form["intent"] if "check" in intent.lower():
alerts = monitor() if alerts:
output = "\n".join(alerts) else:
output = "No intrusions detected." else:
commands = generate_commands(intent) deploy(commands)
alerts = monitor() if alerts:
output = "\n".join(alerts)
else:
 
output = "Configuration applied. No intrusions detected."
return render_template("index.html", output=output, commands=commands) if 	name	== "	main	":
start_scheduler() # ← PASTE IT HERE app.run(debug=True)
