#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Klasa testująca widoki."""

from django.test import TestCase
from morelia.decorators import tags


@tags(['unit'])
class ConvertNumberToStringJsonViewTest(TestCase):
    u"""Klasa testująca widok convert_number_to_string_json."""

    def test_should_return_string_when_response_is_json(self):
        u"""Test sprawdzający poprawność konwersji z int na string oraz wyświetlenie odpowiedzi w formacie json."""
        response = self.client.post('/123/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'123': 'one hundred and twenty-three'})
