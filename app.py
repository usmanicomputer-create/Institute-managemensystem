from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        student_class = request.form["class"]
        father = request.form["father"]
        fees = request.form["fees"]
        status = request.form["status"]

        with open("students.txt", "a") as file:
            file.write(f"{name},{student_class},{father},{fees},{status}\n")

        message = "✅ Record Saved Successfully!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
