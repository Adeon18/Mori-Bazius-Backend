import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # I LOVE PYTHON

import uvicorn
from controller.gateway_controller import App

if __name__ == '__main__':
    app = App()
    uvicorn.run(app.app, port=9000, host='0.0.0.0')
