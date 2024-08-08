from pydantic import BaseModel


class Geo(BaseModel):
    lat: str| None = None
    lng: str| None = None


class Address(BaseModel):
    street: str| None = None
    suite: str| None = None
    city: str| None = None
    zipcode: str| None = None
    geo: Geo| None = None


class Company(BaseModel):
    name: str| None = None
    catchPhrase: str| None = None
    bs: str| None = None


class UserModel(BaseModel):
    id: str | None = None
    name: str | None = None
    username: str| None = None
    email: str| None = None
    address: Address| None = None
    phone: str| None = None
    website: str| None = None
    company: Company| None = None
