Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/flask-api/ginger/ginger.py", line 7, in <module>
    app = create_app()
  File "C:\Users\Administrator\Desktop\flask-api\ginger\app\app.py", line 20, in create_app
    register_blueprint(app)
  File "C:\Users\Administrator\Desktop\flask-api\ginger\app\app.py", line 11, in register_blueprint
    app.register_blueprint(user)
  File "C:\Users\Administrator\Envs\ginger-Rx32UybM\lib\site-packages\flask\app.py", line 64, in wrapper_func
    return f(self, *args, **kwargs)
  File "C:\Users\Administrator\Envs\ginger-Rx32UybM\lib\site-packages\flask\app.py", line 1100, in register_blueprint
    if blueprint.name in self.blueprints:
AttributeError: module 'app.api.v1.user' has no attribute 'name'
TODO: from app.api.v1 import user, book
should be:
from app.api.v1.user import user
from app.api.v1.book import book