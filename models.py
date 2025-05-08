# models.py
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=True)
    name = Column(String, nullable=True)
    phone_number = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    activity_level = Column(String)
    height = Column(Float, nullable=True)
    height_unit = Column(String, nullable=True)
    weight = Column(Float, nullable=True)
    weight_unit = Column(String, nullable=True)
    bmi = Column(Float, nullable=True)
    goal_type = Column(String, nullable=True)
    goal_type_1 = Column(String, nullable=True)
    goal_weight = Column(Float, nullable=True)
    flag = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    otp = Column(String, nullable=True)
