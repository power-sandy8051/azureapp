from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/analyse", methods=["GET", "POST"])
def analyse():
    f = request.files['excelFile']
    f.save(f.filename)
    df = pd.read_excel(f.filename, header=10)
    vmName = df.columns[1].split(",")[0].upper()
    df.columns = ["time", "percentage"]
    df.time = pd.to_datetime(df.time)
    df = df.set_index('time')
    df.plot(figsize=(10,3), title=f"CPU Utilization for VM Name: {vmName}")
    plt.savefig(f'static/{vmName}.png')
    return redirect(url_for('index'))



@app.route('/graphs')
def graphs():
    return render_template('graph.html', files=[i for i in os.listdir('static') if i.endswith(".png")])



if __name__ == "__main__":
    app.run(debug=True)