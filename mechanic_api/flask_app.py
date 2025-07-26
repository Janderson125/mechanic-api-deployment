import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

from app import create_app
from app.config import ProductionConfig

# You can override ProductionConfig attributes from environment variables if needed
app = create_app(ProductionConfig)

# DO NOT include app.run() here, as Render will use Gunicorn to serve the app.
