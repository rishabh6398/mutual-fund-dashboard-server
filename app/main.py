from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import origins
from .fund import router as fund_router
from .auth import router as auth_router
from .purchase import router as purchase_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(fund_router)
app.include_router(purchase_router)
app.include_router(auth_router)
