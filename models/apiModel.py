import boto3
from boto3.dynamodb.conditions import Key, Attr


class Dynamo(object):

    dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
    table = dynamodb.Table("datedPrice")

    @classmethod
    def createNewtable(cls):
        try:
            table = cls.dynamodb.create_table(
                TableName="datedPrice",
                KeySchema=[
                    {
                        "AttributeName": "dtDate",
                        "KeyType": "HASH"
                    }
                ],
                AttributeDefinitions=[
                    {
                        "AttributeName": "dtDate",
                        "AttributeType": "S"
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            return "Table status: {}".format(table.table_status)
        except Exception as err:
            return err

    @classmethod
    def getLastTradePriceByDate(cls, dtDate):
        query = cls.table.get_item(
            Key={
                "dtDate": dtDate,
            }
        )
        if query.get("Item"):
            item = query["Item"]
            return item["dLastTradePrice"]

        return None

    @classmethod
    def scan(cls):
        return cls.table.scan()

    @classmethod
    def delete(cls, cdid, dtDate):
        return cls.table.delete_item(
            Key={
                "cdid": cdid,
                "dtDate": dtDate
            }
        )

    @classmethod
    def put_Item(cls, table_name, item):
        table = cls.dynamodb.Table(table_name)
        return table.put_item(
            Item={
                "dtDate": item["dtDate"],
                "dLastTradePrice": item["dLastTradePrice"]
            }
        )

