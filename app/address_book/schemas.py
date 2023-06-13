from pydantic import BaseModel, confloat, validator


"""
    These are the pydantic schemas created to add basic validation to the request body sent by user.
    Here we also used validator decorator to create a custom validator which will check if the co-ordinates are 
    of float value or not.
"""


class AddressCreate(BaseModel):
    address: str
    landmark: str
    latitude: confloat(ge=-90, le=90)
    longitude: confloat(ge=-180, le=180)

    @validator('latitude', 'longitude')
    def validate_coordinates(cls, value):
        if not isinstance(value, float):
            raise ValueError('Latitude/Longitude should be specified in decimal values')
        return value


class AddressUpdate(BaseModel):
    address: str = None
    landmark: str = None
    latitude: confloat(ge=-90, le=90) = None
    longitude: confloat(ge=-180, le=180) = None

    @validator('latitude', 'longitude')
    def validate_coordinates(cls, value):
        if not isinstance(value, float):
            raise ValueError('Latitude/Longitude should be specified in decimal values')
        return value
