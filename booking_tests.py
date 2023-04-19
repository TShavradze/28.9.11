from pydantic import BaseModel, Field
import pytest
import datetime as dt


class AccessTokenRequest(BaseModel):
    access_token: str = Field(...)


class Booking(BaseModel):
    firstname: str = Field(None)
    lastname: str = Field(None)
    totalprice: int = Field(...)
    depositpaid: bool = Field(...)
    checkin: dt.date = Field(None)
    checkout: dt.date = Field(None)
    additionalneeds: str = Field(...)


def test_access_token_required():
    request = {
        "access_token": "abc123"
    }
    AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_get_bookings():
    response = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "checkin": "2018-11-11",
        "checkout": "2019-11-11",
        "additionalneeds": "Breakfast"
    }

    bookings = Booking(**response)


def test_bookings_get_success():
    response = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "checkin": "2018-11-11",
        "checkout": "2019-11-11",
        "additionalneeds": "Breakfast"
    }
    bookings = Booking(**response)

    assert bookings.firstname == "Jim"
    assert bookings.lastname == "Brown"
    assert bookings.totalprice == 111
    assert bookings.depositpaid == True
    assert bookings.checkin.isoformat() == "2018-11-11"
    assert bookings.checkout.isoformat() == "2019-11-11"
    assert bookings.additionalneeds == "Breakfast"


def test_bookings_get_no_bookings():
    response = []
    bookings = [Booking(**booking) for booking in response]

    assert len(bookings) == 0


