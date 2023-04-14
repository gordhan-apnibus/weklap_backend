from fastapi import FastAPI
from apis.excel_apis import router as excel_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include the Excel API router
app.include_router(excel_router, prefix="/excel")