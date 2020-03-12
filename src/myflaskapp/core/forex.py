"""Forex module"""
from forex_python.converter import CurrencyRates


CR = CurrencyRates()


def get_usd_rate():
    """
    Get list of USD/* rates
    :return: list of USD/* rates
    """

    return CR.get_rates('USD')
