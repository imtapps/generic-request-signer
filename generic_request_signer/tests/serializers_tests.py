from decimal import Decimal
from unittest import TestCase
import datetime
from generic_request_signer.serializer import JsonSerializer


class TestSerializers(TestCase):

    def test_serialize_date(self):
        data = '{"date": "1900-01-31"}'
        serialized_data = JsonSerializer().serialize(data)
        self.assertEqual(serialized_data, {"date": datetime.datetime(1900, 1, 31)})

    def test_serialize_decimal(self):
        data = '{"amount": 123.45}'
        serialized_data = JsonSerializer().serialize(data)
        val = '123.45'
        self.assertEqual(serialized_data, {"amount": Decimal(val)})

