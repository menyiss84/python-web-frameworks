from django.core.wsgi import get_wsgi_application
get_wsgi_application()

from api.customer_resource import CustomerResource
import falcon

app = falcon.API()
app.add_route("/customer", CustomerResource())
app.add_route("/customer/{customer_id:int}", CustomerResource())


# Use this if you want to debug via pycharm
# from wsgiref import simple_server
# if __name__ == '__main__':
#     import os
#     with simple_server.make_server('', os.getenv('PORT', 5000), app) as httpd:
#         httpd.serve_forever()
