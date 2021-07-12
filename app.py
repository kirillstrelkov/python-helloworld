import json
import logging
import os

from flask import Flask

app = Flask(__name__)

LOGGER = logging.getLogger(name=None)
LOGGER.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = logging.FileHandler(os.path.join(os.path.dirname(__file__), "app.log"))

formatter = logging.Formatter("%(asctime)s, %(name)s %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

LOGGER.addHandler(fh)
LOGGER.addHandler(ch)


@app.route("/")
def hello():
    return "Hello My World!"


@app.route("/status")
def status():
    logging.getLogger("status").debug("endpoint was reached")

    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype="application/json",
    )

    return response


@app.route("/metrics")
def metrcis():
    logging.getLogger("metrics").debug("endpoint was reached")

    response = app.response_class(
        response=json.dumps(
            {
                "status": "success",
                "code": 0,
                "data": {"UserCount": 140, "UserCountActive": 23},
            }
        ),
        status=200,
        mimetype="application/json",
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
