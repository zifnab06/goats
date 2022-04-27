from const import lists

from flask import Flask, abort
import random
app = Flask(__name__)


@app.route("/")
@app.route("/<string:thing>")
def main(thing="goats"):
    print(thing)
    if thing not in lists:
        return abort(404)
    return random.choice(lists[thing])

