from django.http import JsonResponse
from django.views import View
from django.db.models import Q
from django.forms.models import model_to_dict
from .services import get_params_types
from pymongo import MongoClient
import pprint


class TemplatesViews(View):

    def post(self, request):
        filter_query = []
        client = MongoClient('mongodb://admin:admin@mongo:27017')
        collection = client.leadhit_test.forms_templates

        form_fields_types = get_params_types(request.GET)

        for k, v in form_fields_types.items():
            filter_query.append({'name_field': k, 'type_field': v})
        forms_list = list(collection.aggregate([
            {
                "$match": {
                    "fields": {
                        "$in": filter_query
                    },
                    '$expr': {
                        '$eq': [
                            {'$size': '$fields'},
                            {"$size": {"$setIntersection": [filter_query, "$fields"]}}
                        ]
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "name": 1,
                    "matching_fields_number": {
                        "$size": '$fields',
                    },

                }
            },
            {"$sort": {'matching_fields_number': -1}},
            {'$limit': 1}
        ]))
        client.close()

        best_form_template = forms_list[0] if forms_list else None

        return JsonResponse(best_form_template or form_fields_types or {})
