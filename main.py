import csv

from flask import Flask, render_template, request, url_for

app = Flask(__name__)


csv_file = "./templates/form_data.txt"
FIELD_NAMES = [
    "first-name",
    "last-name",
    "dob",
    "gender",
    "emplyment-status",
    "salary",
    "email",
    "pan-number",
    "region",
    "city",
    "state",
    "street-address",
    "postal-code",
]


def save_csv(text):
    with open(csv_file, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow(text)


def read_csv():
    try:
        with open(csv_file, "r", newline="") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            data = list(csv_reader)
        return header, data
    except FileNotFoundError:
        return FIELD_NAMES,["No data available."]


@app.route("/")
def homePage():
    header, data = read_csv()
    return render_template("home.html",header=header,data=data)


@app.route("/form")
def formPage():
    return render_template("index.html")


@app.route("/otp", methods=["POST", "GET"])
def otpPage():
    data = request.form.to_dict()
    save_csv(data)
    return "Data saved successfully"


if __name__ == "__main__":
    app.run(debug=True)
