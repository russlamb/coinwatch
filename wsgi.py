#!flask/bin/python
from app import app
import os

# uwsgi -s /tmp/yourapplication.sock --manage-script-name --mount /yourapplication=myapp:app
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)