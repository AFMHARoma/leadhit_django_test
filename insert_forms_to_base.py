import json

from pymongo import MongoClient


def main():
    client = MongoClient('mongodb://admin:admin@mongo:27017')
    db = client.leadhit_test
    coll = db.forms_templates

    with open('forms_to_base.json', 'r') as f:
        forms_list_to_load = json.load(f)

    for item in forms_list_to_load:
        coll.insert_one(item)

    client.close()


if __name__ == '__main__':
    main()
