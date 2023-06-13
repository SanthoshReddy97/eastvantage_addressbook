from sqlalchemy import Column, Integer, String, Float
from app.api.config.db import Base


class Address(Base):
    """
        Address table stores all the addresses.
        Ideally in real world approach we can add userId as foreign key and assign this address to user.
        Columns:
            id: int
            address: str
            landmark: str
            latitude: float
            longitude: float
    """
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    landmark = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
