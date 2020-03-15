import os

from django.core.wsgi import get_wsgi_application
get_wsgi_application()

from api.customer_resource import CustomerResource
import falcon

app = falcon.API()
app.add_route("/customer", CustomerResource())
app.add_route("/customer/{customer_id}", CustomerResource())


# Normally this would run under gunicorn and not from a python module
# from wsgiref import simple_server
# if __name__ == '__main__':
#     with simple_server.make_server('', os.getenv('PORT', 5000), app) as httpd:
#         httpd.serve_forever()
