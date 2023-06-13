import logging

from fastapi import APIRouter, status, HTTPException
from app.address_book.schemas import AddressCreate, AddressUpdate
from app.address_book.service import AddressService

addresses_router = APIRouter()
logger = logging.getLogger("addressbook")


@addresses_router.post("/", response_description="Create a new address", status_code=status.HTTP_200_OK)
async def create_address(address: AddressCreate):
    try:
        return AddressService().create(address)
    except Exception as e:
        logger.error("Error in creating address", e)
        raise HTTPException(status_code=500, detail=str(e))


@addresses_router.patch("/{address_id}", response_description="update address", status_code=status.HTTP_200_OK)
async def update_address(address_id, address_update: AddressUpdate):
    try:
        return AddressService().update(address_id, address_update)
    except Exception as e:
        logger.error("Error in updating address", e)
        raise HTTPException(status_code=500, detail=str(e))


@addresses_router.delete("/{address_id}", response_description="delete address", status_code=status.HTTP_200_OK)
def delete_address(address_id: int):
    try:
        return AddressService().delete(address_id)
    except Exception as e:
        logger.error("Error in deleting address", e)
        raise HTTPException(status_code=500, detail=str(e))


@addresses_router.get("/", response_description="get address", status_code=status.HTTP_200_OK)
def get_addresses(latitude: float, longitude: float, distance: float):
    try:
        return AddressService().get(latitude, longitude, distance)
    except Exception as e:
        logger.error("Error in getting address", e)
        raise HTTPException(status_code=500, detail=str(e))


@addresses_router.get("/using-geodesic",
                      response_description="get address using geodesic library",
                      status_code=status.HTTP_200_OK)
def get_addresses_by_geodesic(latitude: float, longitude: float, distance: float):
    try:
        return AddressService().get_using_geodesic(latitude, longitude, distance)
    except Exception as e:
        logger.error("Error in getting address using geodesic", e)
        raise HTTPException(status_code=500, detail=str(e))
