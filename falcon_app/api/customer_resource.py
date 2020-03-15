import falcon as falcon
from db.dal import customer_actions


class CustomerResource:
    def on_get(self, req, resp, customer_id=None):
        resp.status = falcon.HTTP_200
        try:
            customer = customer_actions.get_customer(customer_id=customer_id)
            resp.add_header({'Content-Type': 'application/json'})
            resp.media = customer.to_dict()
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.content = {"error": str(e)}

    def on_delete(self, req, resp, customer_id=None):
        try:
            customer_actions.delete_customer(customer_id=customer_id)
            resp.media = {"success": True}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.content = {"error": str(e)}

    def on_put(self, req, resp, customer_id=None):
        resp.status = falcon.HTTP_200
        try:
            customer_data_to_update = req.media
            customer = customer_actions.update_customer(customer_id, **customer_data_to_update)
            resp.add_header({'Content-Type': 'application/json'})
            resp.media = customer.to_dict()
        except Exception as e:
            print(e)
            resp.status = falcon.HTTP_500
            resp.content = {"error": str(e)}

    def on_post(self, req, resp, customer_id=None):
        resp.status = falcon.HTTP_200
        try:
            customer_data = req.media
            customer = customer_actions.create_customer(**customer_data)
            resp.add_header({'Content-Type': 'application/json'})
            resp.media = customer.to_dict()
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.content = {"error": str(e)}