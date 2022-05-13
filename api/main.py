import uvicorn
from frameworks_and_drivers.web.fastapi_router import app as fastapi_app

uvicorn.run(app=fastapi_app, host="0.0.0.0", port=80)
