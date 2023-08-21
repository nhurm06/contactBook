#!/usr/bin/env python3
'''
Unit tests for serializers

'''

from unittest import TestCase
import ast
from serializers.serializer import Serializer
from contacts import Contact


class TestjsonSerializer(TestCase):
    def test_decode(self):
        data = "test.json"
        actual = [x.name for x in Serializer("json").decode(data)]
        expected = ["Sheena Serrano"]
        if (self.assertEqual(actual, expected)):
            self.fail()

    def test_encode(self):
        data = Contact(name="Sheena Serrano")
        actual = Serializer("json").encode(data)
        expected = '{"name": "Sheena Serrano", "address": null, "phone": null}'
        if (self.assertEqual(actual, expected)):
            self.fail()


class TestcsvSerializer(TestCase):
    def test_decode(self):
        data = "test.csv"
        actual = [x.name for x in Serializer("csv").decode(data)]
        expected = ["John Smith"]
        if (self.assertEqual(actual, expected)):
            self.fail()
S
    def test_encode(self):
        data = [Contact(name="Sheena Serrano")]
        actual = Serializer("csv").encode(data)
        expected = ast.literal_eval('[{"name": "Sheena Serrano", "address": None, "phone": None}]')
        if (self.assertEqual(actual, expected)):
            self.fail()
