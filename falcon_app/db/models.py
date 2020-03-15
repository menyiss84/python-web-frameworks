import json
import django
django.setup()

from django.db.models import Model, BooleanField, CharField, URLField, DateTimeField


class Customer(Model):
    name = CharField(max_length=100, db_index=True)
    domain = URLField(max_length=255, null=True)
    join_date = DateTimeField(auto_created=True, auto_now_add=True, null=True)
    is_active = BooleanField(default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.domain,
            'join_date': self.join_date,
            'is_active': self.is_active
        }

    def to_json(self):
        return json.dumps(self.to_dict())
