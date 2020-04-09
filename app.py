from flask import Flask, request
from utils.investmentCalculator import InvestmentCalculator
from validators.apiValidators import ApiValidators
from validators.apiResponses import ApiMessages
from models.apiModel import Dynamo

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return ApiMessages.successMessage(
        "message",
        "Welcome to cdb Invest API"
    )


@app.route("/api/v1", methods=["POST"])
def post():
    cdbRate = request.json["cdbRate"]
    investmentDate = request.json["investmentDate"]
    currentDate = request.json["currentDate"]

    if not cdbRate:
        return ApiMessages.badRequestMessage("missing cdbRate parameter")

    if cdbRate and not isinstance(cdbRate, float):
        return ApiMessages.badRequestMessage("invalid data type of cdbRate parameter, ex: 103.5 must be integer")

    if not investmentDate:
        return ApiMessages.badRequestMessage("missing investmentDate parameter")

    if not currentDate:
        return ApiMessages.badRequestMessage("missing currentDate parameter")

    if investmentDate and not ApiValidators.isDateISO8601(investmentDate):
        return ApiMessages.badRequestMessage("invalid format of investmentDate parameter, ex: 2016-11-14")

    if currentDate and not ApiValidators.isDateISO8601(currentDate):
        return ApiMessages.badRequestMessage("invalid format of currentDate parameter, ex: 2016-12-26")

    investmentDate = ApiValidators.formattedDate(investmentDate)
    currentDate = ApiValidators.formattedDate(currentDate)

    caculatedValues = InvestmentCalculator.calculateUnitPrice(investmentDate, currentDate)

    if caculatedValues:
        return ApiMessages.successMessage(item=caculatedValues)


@app.route("/api/v1", methods=["GET"])
def get():
    queryStringDtDate = request.args.get("dtDate")

    if not queryStringDtDate:
        return ApiMessages.successMessage(
            "message",
            "Use query string 'dtDate' filter to get data. "
            "For example: dtDate=2019-04-29.",
        )

    if not ApiValidators.isDateISO8601(queryStringDtDate):
        return ApiMessages.badRequestMessage("invalid format of currentDate parameter, ex: 2016-12-26.")

    queryStringDtDate = ApiValidators.toISO8601(queryStringDtDate)
    dtDate = ApiValidators.unformattedDate(queryStringDtDate)
    lastTradePrice = Dynamo.getLastTradePriceByDate(dtDate)

    if not lastTradePrice:
        return ApiMessages.notFoundMessage("object not found")

    return ApiMessages.successMessage(message="lastTradePrice", item=lastTradePrice)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
