import langchainScrapper
import Aimodel
from flask import Flask, request
import wikipedia.exceptions
import urllib.error

app = Flask(__name__)


@app.route("/pred")
def user():
    return "I like"


@app.route("/linkContent", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        genLink = data["generateLink"]
        genLink = langchainScrapper.procesLink(genLink)
        genLink = Aimodel.summerize(genLink)
        genLink = Aimodel.format_to_points(genLink)
        return genLink
    except wikipedia.exceptions.PageError as e:
        return {"error": "Wikipedia page error: " + str(e)}, 500
    except urllib.error.URLError as e:
        return {"error": "URL error: " + str(e)}, 500
    except Exception as e:
        return {"error": "An unexpected error occurred: The link exceeds max limit of text" + str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
