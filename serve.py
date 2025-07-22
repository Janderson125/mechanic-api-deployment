from waitress import serve
from mechanic_api.app import create_app
from mechanic_api.config import ProductionConfig

app = create_app(ProductionConfig)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
