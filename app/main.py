import uvicorn
from src.libs.api import create_app


def main():
    app = create_app()
    uvicorn.run(app, host="192.168.0.1", port=5000)


if __name__ == "__main__":
    main()
