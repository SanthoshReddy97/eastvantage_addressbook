from fastapi import HTTPException
from geopy.distance import geodesic
from sqlalchemy import text

from app.address_book.models import Address
from app.address_book.schemas import AddressCreate, AddressUpdate
from app.api.config.db import get_db


class AddressService:
    """
        AddressService is initiated with db and is used to do db operations.

        Methods:
            create
            update
            delete
            get
            get_using_geodesic

        * In get method we are using RAW SQL query to get the addresses less than the given distance.
        * In get_using_geodesic method we are fetching all the addresses from db then filtering out with using
            geopy library.
    """

    def __init__(self):
        self.db = next(get_db())

    def create(self, address: AddressCreate):
        new_address = Address(
            address=address.address,
            landmark=address.landmark,
            latitude=address.latitude,
            longitude=address.longitude
        )

        self.db.add(new_address)
        self.db.commit()
        self.db.refresh(new_address)
        return new_address

    def update(self, address_id, address_update: AddressUpdate):
        address = self.db.query(Address).get(address_id)
        if not address:
            raise HTTPException(status_code=404, detail="Address not found")

        if address_update.landmark is not None:
            address.landmark = address_update.landmark
        if address_update.address is not None:
            address.address = address_update.address
        if address_update.latitude is not None:
            address.latitude = address_update.latitude
        if address_update.longitude is not None:
            address.longitude = address_update.longitude

        self.db.commit()
        self.db.refresh(address)
        return address

    def delete(self, address_id):
        address = self.db.query(Address).get(address_id)
        if not address:
            raise HTTPException(status_code=404, detail="Address not found")

        self.db.delete(address)
        self.db.commit()
        return {"message": "Address deleted"}

    def get(self, latitude: float, longitude: float, distance: float):
        query = text(
            f"SELECT id, address, landmark, latitude, longitude, (3959 * acos(cos(radians({latitude})) * cos(radians("
            f"latitude)) * cos(radians(longitude) - radians({longitude})) + sin(radians({latitude})) * sin(radians("
            f"latitude)))) AS distance FROM addresses WHERE distance < {distance} ORDER BY distance;"
        )

        result = self.db.execute(query).all()
        addresses = [
            {
                "id": row.id,
                "address": row.address,
                "landmark": row.landmark,
                "latitude": row.latitude,
                "longitude": row.longitude
            } for row in result]
        return addresses

    def get_using_geodesic(self, latitude: float, longitude: float, distance: float):
        addresses = self.db.query(Address).all()
        addresses_within_distance = []
        user_coords = (latitude, longitude)

        for address in addresses:
            address_coords = (address.latitude, address.longitude)
            address_distance = geodesic(user_coords, address_coords).km
            if address_distance <= distance:
                addresses_within_distance.append(address)

        return addresses_within_distance
