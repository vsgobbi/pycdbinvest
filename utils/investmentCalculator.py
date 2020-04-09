from datetime import timedelta
from models.apiModel import Dynamo
from validators.apiValidators import ApiValidators


class InvestmentCalculator(object):

    @classmethod
    def calculateUnitPrice(cls, initDate, endDate):
        annual = float('%.16f' % (1 / 252))
        calculatedDays = []
        daysInterval = cls.calculateDaysInterval(initDate, endDate)

        for i in range(daysInterval):

            currentDate = initDate + timedelta(days=i)

            lastTradePrice = Dynamo.getLastTradePriceByDate(
                dtDate=ApiValidators.unformattedDate(currentDate)
            )

            if not lastTradePrice:
                continue

            cdiK = float("%.2f" % float(lastTradePrice))
            cdbRate = 103.5

            tCdiK = float("%.8f" % (((cdiK / 100) + 1) ** annual - 1))

            tCdiAcumulado = (1 ** (i * daysInterval)) * (1 + tCdiK * (cdbRate / 100))
            tCdiAcumulado = float("%.16f" % tCdiAcumulado)

            unitPrice = 1000 * tCdiAcumulado
            calculatedDays.append({"date": currentDate.strftime("%Y-%m-%d"), "unitPrice": float("%.8f" % unitPrice)})

        return calculatedDays

    @classmethod
    def calculateDaysInterval(cls, initDate, actualDate):
        try:
            daysInterval = (actualDate - initDate).days
            return daysInterval
        except Exception as err:
            return {"error": "Couldn't calculate days interval: {}".format(err)}
