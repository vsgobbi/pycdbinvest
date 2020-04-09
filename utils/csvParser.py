from io import StringIO
from csv import reader, DictReader
from time import sleep
from models.apiModel import Dynamo
from boto3 import resource


class PopulateDynamo:

    def __init__(self):
        self.s3 = resource("s3")
        pass

    def readFromS3(self, bucketName, fileName):
        self.obj = self.s3.Object(bucketName, fileName)
        return self.obj.get()["Body"].read()

    def readCsv(self):
        csvPath = "./CDI_Prices.csv"
        with open(csvPath, "r") as csvFile:
            items = reader(csvFile, delimiter=",")
        for item in items:
            print(item)

    def loadToJson(self, csvBuffer, fieldsName):
        if not isinstance(csvBuffer, bytes or str):
            return "invalid csvBuffer"
        csvBuffer = DictReader(StringIO(csvBuffer.decode()), fieldsName)
        for index, rows in enumerate(csvBuffer):
            if index == 0:
                continue
            print(dict(rows))
            item = dict(rows)
            Dynamo.put_Item(item=item, table_name="datedPrice")
            sleep(0.5)



obj = PopulateDynamo()
content = obj.readFromS3(bucketName="cdiprices", fileName="CDI_Prices.csv")
print(obj.loadToJson(content, fieldsName=("sSecurityName", "dtDate", "dLastTradePrice")))

# print(Dynamo.getLastTradePriceByDate(dtDate="02/12/2019"))
# print(obj.extractJsonItem("./CDI_Prices.json"))
