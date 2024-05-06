from fastapi import FastAPI, Request, Form, HTTPException,Header,Depends ,status
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2AuthorizationCodeBearer
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from sqlalchemy import create_engine, Column, Integer, String,LargeBinary,DateTime,BigInteger,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
import uvicorn
import httpx,json
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
import google.generativeai as genai
from pydantic import BaseModel
from typing import Optional
from datetime import date
from sqlalchemy.sql import func

headers={'api_key':'a5d759ef-abb3-4204-8be3-190f13155abf'}
DATABASE_URL = "postgresql://athish:#portal123@demopost.postgres.database.azure.com:5432/postgres"
<<<<<<< HEAD
=======


DATABASE_URL = "postgresql://portaladmission_9hl7_user:KBqP20RogZ5S2rQ58gAVSbnesDRBwP1l@dpg-coq6mbdjm4es73aga62g-a/portaladmission_9hl7"

>>>>>>> 886b09829b94fbacf12b7cff745e66934e759682
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Student_Eligibility(Base):
    __tablename__ = "student_eligibility"
    created_date=Column(Date, server_default=func.current_date())

    email_id=Column(String,primary_key=True, index=True)
    ph_no = Column(BigInteger)
    first_subject= Column(String)
    first_subject_marks_obtained= Column(Integer)
    first_subject_total_marks= Column(Integer)
    second_subject= Column(String)
    second_subject_marks_obtained= Column(Integer)
    second_subject_total_marks= Column(Integer)  
    third_subject= Column(String)
    third_subject_marks_obtained= Column(Integer)
    third_subject_total_marks= Column(Integer) 
    fourth_subject=Column(String)
    fourth_subject_marks_obtained= Column(Integer)
    fourth_subject_total_marks= Column(Integer) 
    Stream= Column(String)
    Eligibility=Column(String)
    created_date=Column(Date, server_default=func.current_date())
class Student_Details(Base):
    __tablename__ = "student_details"        
    created_date=Column(Date, server_default=func.current_date())
    email_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    pincode = Column(Integer)
    nationality = Column(String)
    exam_center = Column(String)
    aadhar_no = Column(BigInteger)
    email = Column(String)
    gender = Column(String)
    dob = Column(Date)
    age = Column(Integer)
    religion = Column(String)
    community = Column(String)
    caste = Column(String)
    mother_tongue = Column(String)
    ph_no = Column(BigInteger)
    father_ph_no = Column(BigInteger)
    mother_ph_no = Column(BigInteger)
    father_name = Column(String)
    father_occupation = Column(String)
    father_income = Column(Integer)
    mother_name = Column(String)
    mother_occupation = Column(String)
    mother_income = Column(Integer)
    tenth_exam_name = Column(String)
    tenth_register_no = Column(BigInteger)
    tenth_passing_date = Column(Date)
    tenth_attempts = Column(Integer)
    tenth_maths_marks = Column(Integer)
    tenth_science_marks = Column(Integer)
    tenth_total_marks = Column(Integer)
    tenth_max_marks = Column(Integer)
    tenth_school_address = Column(String)
    Stream = Column(String)
    twelfth_subject1= Column(String)
    twelfth_subject1_marks_obtained = Column(Integer)
    twelfth_subject1_total_marks = Column(Integer)
    twelfth_subject2= Column(String)
    twelfth_subject2_marks_obtained = Column(Integer)
    twelfth_subject2_total_marks = Column(Integer)
    twelfth_subject3= Column(String)
    twelfth_subject3_marks_obtained = Column(Integer)
    twelfth_subject3_total_marks = Column(Integer)
    twelfth_subject4= Column(String)
    twelfth_subject4_marks_obtained = Column(Integer)
    twelfth_subject4_total_marks = Column(Integer)
    twelfth_subject5= Column(String)
    twelfth_subject5_marks_obtained = Column(Integer)
    twelfth_subject5_total_marks = Column(Integer)
    twelfth_marksheet = Column(LargeBinary)
    community_certificate = Column(LargeBinary)
    passport_photo = Column(LargeBinary)
    preference1=Column(String)
    preference2=Column(String)
    preference3=Column(String)
    preference4=Column(String)
    transaction = Column(LargeBinary)
class FormData1(BaseModel):
    email_id: Optional[str]
    ph_no: Optional[int]
    first_subject: Optional[str]
    first_subject_marks_obtained: Optional[int]
    first_subject_total_marks: Optional[int]
    second_subject: Optional[str]
    second_subject_marks_obtained: Optional[int]
    second_subject_total_marks: Optional[int]   
    third_subject: Optional[str]
    third_subject_marks_obtained: Optional[int]
    third_subject_total_marks: Optional[int]   
    fourth_subject: Optional[str]
    fourth_subject_marks_obtained: Optional[int]
    fourth_subject_total_marks: Optional[int]  
    Stream: Optional[str] 
    Eligibility: Optional[str]
class FormData2(BaseModel):
    email_id:Optional[str]
    name: Optional[str]
    address: Optional[str]
    pincode: Optional[int]
    nationality: Optional[str]
    exam_center: Optional[str]
    aadhar_no: Optional[int]
    email: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    age: Optional[int]
    religion: Optional[str]
    community: Optional[str]
    caste: Optional[str]
    mother_tongue: Optional[str]
    ph_no: Optional[int]
    father_ph_no: Optional[int]
    mother_ph_no: Optional[int]
    father_name: Optional[str]
    father_occupation: Optional[str]
    father_income: Optional[int]
    mother_name: Optional[str]
    mother_occupation: Optional[str]
    mother_income: Optional[int]
    tenth_exam_name: Optional[str]
    tenth_register_no: Optional[int]
    tenth_passing_date: Optional[date]
    tenth_attempts: Optional[int]
    tenth_maths_marks: Optional[int]
    tenth_science_marks: Optional[int]
    tenth_total_marks: Optional[int]
    tenth_max_marks: Optional[int]
    tenth_school_address: Optional[str]
    Stream: Optional[str]
    twelfth_subject1: Optional[str]
    twelfth_subject1_marks_obtained: Optional[int]
    twelfth_subject1_total_marks: Optional[int]
    twelfth_subject2: Optional[str]
    twelfth_subject2_marks_obtained : Optional[int]
    twelfth_subject2_total_marks: Optional[int]
    twelfth_subject3: Optional[str]
    twelfth_subject3_marks_obtained: Optional[int]
    twelfth_subject3_total_marks: Optional[int]
    twelfth_subject4: Optional[str]
    twelfth_subject4_marks_obtained: Optional[int]
    twelfth_subject4_total_marks: Optional[int]
    twelfth_subject5: Optional[str]
    twelfth_subject5_marks_obtained: Optional[int]
    twelfth_subject5_total_marks: Optional[int]
    twelfth_marksheet : Optional[bytes]
    community_certificate : Optional[bytes]
    passport_photo : Optional[bytes]
    preference1: Optional[str]
    preference2: Optional[str]
    preference3: Optional[str]
    preference4: Optional[str]
    transaction : Optional[bytes]
  
Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="add any string...")
app.mount("/static", StaticFiles(directory="static"), name="static")

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id='9310596698-kbh954efjos4gjcb1pv2gvreqi74u528.apps.googleusercontent.com',
    client_secret='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',
)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    user = request.session.get('user')
    if user:
        return templates.TemplateResponse("Home.html", {"request": request,"email_id":user["email"]})
    else:
        return templates.TemplateResponse("sign.html", {"request": request})
@app.get("/about", response_class=HTMLResponse)
async def read_item(request: Request):
    user = request.session.get('user')
    if user:
        return templates.TemplateResponse("about.html", {"request": request,"email_id":user["email"]})
    else:
        return templates.TemplateResponse("sign.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url,scope="openid email")


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:  
        request.session['user'] = dict(user)
    return RedirectResponse('/')

@app.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    request.session.clear()
    return RedirectResponse('read_item')

@app.get("/personal_details", response_class=HTMLResponse)
async def read_item(request: Request):
    user = request.session.get('user')
    if user:
      return templates.TemplateResponse("personaldetails.html", {"request": request,"email_id":user["email"]})
    else:
        return templates.TemplateResponse("sign.html", {"request": request})

@app.post("/personal_details",response_class=HTMLResponse)
async def stud_det_post(request:Request):
    form_data = await request.form()
    internal_api_url = "http://127.0.0.1:8000/personal_details/post"
    try:
        async with httpx.AsyncClient() as client:
            await client.post(internal_api_url,data=json.dumps(dict(form_data)),headers=headers)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return templates.TemplateResponse("success.html", {"request": request})


@app.post("/",response_class=HTMLResponse)
async def create_item(request:Request): 
    form_data = await request.form()
    internal_api_url = "http://127.0.0.1:8000/api/stu_el"
    try:
        async with httpx.AsyncClient() as client:
            await client.post(internal_api_url,data=json.dumps(dict(form_data)),headers=headers)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return templates.TemplateResponse("Home.html", {"request": request})

async def authenticate_api_key(api_key: str):
    if api_key is None:
        raise HTTPException(status_code=401, detail="API key is missing")
    if api_key != headers['api_key']:
        raise HTTPException(status_code=403, detail="Invalid API key")
    

@app.post("/api/stu_el")
async def validate_data(request:Request,form_data: FormData1):
    await authenticate_api_key(request.headers.get('api_key'))
    db = SessionLocal() 
    try:
        existing_student = db.query(Student_Eligibility).filter(Student_Eligibility.email_id == form_data.email_id).first()
        if existing_student:
            for key, value in form_data.dict().items():
                setattr(existing_student, key, value)
        else:
            new_student = Student_Eligibility(**form_data.dict())
            db.add(new_student)
        db.commit()
        db.refresh(new_student if not existing_student else existing_student)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    return {"message": "Data validated successfully", "form_data": "fwegf"}

@app.post("/personal_details/post")
async def stud_det_post(request:Request,form_data: FormData2):
    await authenticate_api_key(request.headers.get('api_key'))
    db = SessionLocal()
    try:
        existing_student = db.query(Student_Details).filter(Student_Details.email_id == form_data.email_id).first()
        if existing_student:
            for key, value in form_data.dict().items():
                setattr(existing_student, key, value)
        else:
            new_student = Student_Details(**form_data.dict())
            db.add(new_student)
        db.commit()
        db.refresh(new_student if not existing_student else existing_student)
    except Exception as e:
        raise HTTPException(status_code=401, detail="{Exception}")
    return {"message": "Data validated successfully", "form_data": "fwegf"}


# @app.post("/eligibility_api")
# async def eligibility_reason(request:Request):
#     form_data = await request.form()
#     eligibility_info="Stream:"+form_data['Stream']+"\nSubjects:"+"\n\n1:"+form_data['first_subject']+"="+form_data['first_subject_marks_obtained']+","+"\n2:"+form_data['second_subject']+"="+form_data['second_subject_marks_obtained']+","+"\n3:"+form_data['third_subject']+"="+form_data['third_subject_marks_obtained']+","+"\n4:"+form_data['fourth_subject']+"="+form_data['fourth_subject_marks_obtained']
#     genai.configure(api_key="AIzaSyC5DXjyN4Udbb9xONanYvGVL5sOrA1jaHU")
#     try:
#         generation_config = { 
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 0,
#     "max_output_tokens": 8192,
#     }
#         safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_LOW_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_LOW_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_LOW_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_LOW_AND_ABOVE"
#     },
#     ]
#         model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
#                                 generation_config=generation_config,
#                                 safety_settings=safety_settings)
#         convo = model.start_chat(history=[
#   {
#     "role": "user",
#     "parts": ["You are chatbot which only outputs the reason for a student's eligibility .This is the criteria \nThe eligibility criteria:\n\nTotal four subjects\nFor Science:\nSubjects:\n1.Maths\n2.Physics\n3.Chemistry\n4.Computer Science or Information Practices\nAll the four subjects should have more than 50%  . Maths, physics and any one in  chemistry or computer science should have more than 75%  if computer science is selected instead of information practices  or else if information practices is selected then maths ,physics and chemistry  should have more than 75%.\n\nFor Arts:\n\nSubjects:\nCategory-A:\n1.Mathematics or Business Mathematics or\nStatistics or Applied Mathematics  or Business Mathematics and\nStatistics.\nCategory-B:\n2. Commerce or Economics or Accountancy \n3. Commerce or Economics or Accountancy \n4.Computer Science or Information Practices\n\nAll the four subjects should have more than 50% . Subject-1 from category-A should have more than 75% and any two subjects from category -B should have more than 75% .If computer science is selected  instead of information practices it can be included in category-B or if information is selected it cannot be included in category-B.\n\nWith respect to the above criteria you should determine only the reason if the candidate is not eligible given the marks and stream of the candidate\nThe input format will be:\nStream:[Stream chosen]\nSubjects:\n\n1. [Subject name]=[Subject marks]\n2. [Subject name]=[Subject marks]\n3. [Subject name]=[Subject marks]\n4. [Subject name]=[Subject marks]"]
#   },
#   {
#     "role": "model",
#     "parts": ["Okay, I'm ready to analyze student eligibility based on the criteria you've provided and output the reason for ineligibility if applicable. Please input the student's information in the format you described."]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 65\n3. Chemistry = 76\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Eligible."]
#   },
#   {
#     "role": "user",
#     "parts": ["You are wrong"]
#   },
#   {
#     "role": "model",
#     "parts": ["I apologize, you are correct. I made an error in evaluating the student's eligibility. \n\nThe reason for ineligibility is: Physics score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 75\n3. Chemistry = 74\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["The reason for ineligibility is: Chemistry score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["you are wrong"]
#   },
#   {
#     "role": "model",
#     "parts": ["I apologize, you are correct. I am still under development and learning to accurately assess eligibility based on the complex criteria. \n\nThe student is eligible as per the criteria."]
#   },
#   {
#     "role": "user",
#     "parts": ["why is he eligible"]
#   },
#   {
#     "role": "model",
#     "parts": ["I apologize, I am not supposed to provide explanations, only the reason for ineligibility."]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 74\n2. Physics = 76\n3. Chemistry = 76\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["The reason for ineligibility is: Maths score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["only give me the reason dont give \"The reason for ineligibility is:\""]
#   },
#   {
#     "role": "model",
#     "parts": ["Okay, I will only provide the reason for ineligibility without the preceding statement."]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 75\n3. Chemistry = 74\n4.Information Practices = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Chemistry score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 75\n3. Chemistry = 74\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Chemistry score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["You are wrong I told you to take the maximum of chemistry and computer science if computer science is given instead of information practices"]
#   },
#   {
#     "role": "model",
#     "parts": ["I sincerely apologize for the repeated mistake. You are absolutely right, I should consider the maximum score between Chemistry and Computer Science when Computer Science is chosen. \n\nBased on the input, the student is eligible as the maximum score between Chemistry (74) and Computer Science (90) is greater than 75%."]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 75\n3. Chemistry = 74\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Eligible."]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Arts\nSubjects:\n1. Mathematics = 80\n2. Commerce = 75\n3. Accountancy = 74\n4. Computer Science = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Accountancy score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Science\nSubjects:\n1. Maths = 80\n2. Physics = 75\n3. Chemistry = 74\n4. Information Practices = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Chemistry score is less than 75%"]
#   },
#   {
#     "role": "user",
#     "parts": ["Stream: Arts\nSubjects:\n1. Mathematics = 80\n2. Commerce = 75\n3. Accountancy = 74\n4.  Information Practices = 90"]
#   },
#   {
#     "role": "model",
#     "parts": ["Accountancy score is less than 75%"]
#   },
# ])
#         convo.send_message(eligibility_info)
#         response=convo.last.text
#     except Exception as e:
#         pass
#     return {"data":response}



# if __name__=="__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
