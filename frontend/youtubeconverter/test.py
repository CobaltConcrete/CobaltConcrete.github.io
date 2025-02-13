import os
from supabase import create_client, Client

url: str = os.environ.get("https://suaqbnpbgidzmyshrboy.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN1YXFibnBiZ2lkem15c2hyYm95Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzcxNzE2MjQsImV4cCI6MjA1Mjc0NzYyNH0.UUPdN-dB50hcOAi0QDmFXTsMXW8bg-nUaRgduyXWjWk")
supabase: Client = create_client("https://suaqbnpbgidzmyshrboy.supabase.co", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InN1YXFibnBiZ2lkem15c2hyYm95Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzcxNzE2MjQsImV4cCI6MjA1Mjc0NzYyNH0.UUPdN-dB50hcOAi0QDmFXTsMXW8bg-nUaRgduyXWjWk")

response = supabase.table("usertable").select("*").execute()

print(response)

data = supabase.table("usertable").insert({
    "name": "John Doe",
    "age": 25,
    "genderid": 1,
    "description": "A brief description about John",
    "photo": "egphoto",
    "credits": 100,
}).execute()

print(data)