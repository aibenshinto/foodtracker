# schemas.py
from pydantic import BaseModel
from typing import Optional

class PhoneRequest(BaseModel):
    phone: str

class OTPVerifyRequest(BaseModel):
    phone: str
    otp: str

class UserProfileBase(BaseModel):
    image_url: Optional[str] = None
    name: Optional[str] = None
    phone_number: str
    age: Optional[int] = None
    gender: Optional[str] = None
    activity_level: str
    height: Optional[float] = None
    height_unit: Optional[str] = None
    weight: Optional[float] = None
    weight_unit: Optional[str] = None
    goal_type: Optional[str] = None
    goal_type_1: Optional[str] = None
    goal_weight: Optional[float] = None

class UserProfileCreate(UserProfileBase):
    id: int

class UserProfileResponse(BaseModel):
    id: int
    flag: bool
