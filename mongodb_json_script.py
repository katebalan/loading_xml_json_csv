import pymongo
import json


def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.labs
    jobs_json_collection = db.jobs_json

    for i in json.loads(open('./data/dataset.json').read()):
        jobs_json_collection.insert(i)


if __name__ == "__main__":
    main()
