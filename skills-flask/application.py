from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/application-form/")
def application_form():
    """ This section is the actual form that the user fills out"""
    # Nothing to see here, partner... just a render template.
    return render_template('application-form.html')


@app.route("/application", methods=['POST'])
def application_response():
    """ This section is the thank you reply user gets after submission"""

    # use request.form.get(args) for POST methods
    # for GET, it's request.get(args), args from the name="value" in html
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    salary = request.form.get("salary")
    job_title = request.form.get("job-title")

    # passing in the arguments from request.form.get(args)
    return render_template('application-response.html', first_name = first_name,
                                                        last_name = last_name,
                                                        salary = salary,
                                                        job_title = job_title)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
