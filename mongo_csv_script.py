import pymongo
import csv


def main():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.labs
    jobs_csv_collection = db.jobs_csv

    csvfile = open('./data/dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip headers
    csvreader.__next__()

    for i in csvreader:
        jobs_csv_collection.insert({
            "id": i[0],
            "company_name": i[1],
            "job_title": i[2],
            "longitude": i[3],
            "latitude": i[4]
        })


if __name__ == "__main__":
    main()
