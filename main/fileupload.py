#pip install python-multipart
#pip install boto3


from fastapi import APIRouter ,UploadFile , File
import boto3
from botocore.exceptions import ClientError


route = APIRouter()

s3 = boto3.client('s3')

@route.post("/upload/resume",status_code = 201)
def upload_resume(resume: UploadFile = File(...,media_type="application/pdf")):
    #file size checking
    s3.upload_fileobj(resume, "BUCKET_NAME", "OBJECT_NAME")
    return "Resume Uploaded Successfully"