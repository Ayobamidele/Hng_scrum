from fastapi import FastAPI, status
from api.v1.routes import api_version_one
from api.utils import success_response

from fastapi.middleware.cors import CORSMiddleware



origins = [
	"http://localhost:8000"
]

app = FastAPI()
app.include_router(api_version_one)



app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
def home():
    return success_response(
		status_code=status.HTTP_200_OK,
		message=f"Hey There👋. Welcome to HNF SCRUM.",
    )

