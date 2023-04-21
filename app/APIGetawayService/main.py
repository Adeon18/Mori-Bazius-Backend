import uvicorn
from controller.gateway_controller import App

if __name__ == '__main__':
    app = App()
    uvicorn.run(app.app, port=8080, host='0.0.0.0')
