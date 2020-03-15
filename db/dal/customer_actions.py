from db.models import Customer


def get_customer(**kwargs):
    return Customer.objects.get(**kwargs)


def create_customer(**kwargs):
    customer = Customer(**kwargs)
    customer.save()
    return customer


def update_customer(customer_id, **kwargs):
    Customer.objects.filter(id=customer_id).update(**kwargs)
    return get_customer(customer_id=customer_id)


def delete_customer(customer_id):
    Customer.objects.delete(id=customer_id)
