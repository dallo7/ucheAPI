import langchainScrapper
import Aimodel
from flask import Flask, request

app = Flask(__name__)


@app.route("/pred")
def user():
    return "I like"


@app.route("/linkContent", methods=["POST"])
def create_user():
    data = request.get_json()

    genLink = data["generateLink"]

    genLink = langchainScrapper.procesLink(genLink)
    print(genLink)

    genLink = Aimodel.summerize(genLink)

    print(genLink)

    genLink = Aimodel.format_to_points(genLink)

    return genLink


if __name__ == "__main__":
    app.run(debug=True)


