# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import UserProfile
from database import get_db
from schemas import *
from utils import send_otp
from fastapi.responses import JSONResponse

from database import Base, engine
Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.post("/login/")
def login(data: PhoneRequest,db: Session = Depends(get_db)):
    otp = send_otp(data.phone)

    user = db.query(UserProfile).filter_by(phone_number=data.phone).first()        # Check if user already exists
    if not user:
        user = UserProfile(phone_number=data.phone, otp=otp)
        db.add(user)
    else:
        user.otp = otp                                                            # Update existing user's OTP
    
    db.commit()

    return {"message": f"OTP sent to {data.phone}"}

@app.post("/login_verify/")
def login_verify(data: OTPVerifyRequest, db: Session = Depends(get_db)):
   user = db.query(UserProfile).filter_by(phone_number=data.phone).first()
   
   if not user or user.otp!=data.otp:
       raise HTTPException(status_code=400, detail="Invalid OTP")
   
   user.otp= None
   db.commit()
   print(user.otp)
   return {"id": user.id, "flag": user.flag}       
       

@app.post("/profile/")
def register_profile(data: UserProfileCreate, db: Session = Depends(get_db)):
    user = db.query(UserProfile).filter_by(id=data.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.flag:
        raise HTTPException(status_code=200, detail="Profile already completed")

    for field, value in data.dict(exclude={"id"}).items():
        setattr(user, field, value)

    # BMI calculation
    h = user.height
    if user.height_unit == 'cm':
        h = h / 100
    elif user.height_unit == 'ft':
        h = h * 0.3048

    w = user.weight
    if user.weight_unit == 'lb':
        w = w * 0.453592

    if h and w:
        user.bmi = w / (h ** 2)

    user.flag = True
    db.commit()
    db.refresh(user)

    return {"message":"Profile updated successfully"}
