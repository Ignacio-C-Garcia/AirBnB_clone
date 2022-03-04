"""Amenity module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City"""
    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
