import pymongo
import xml.etree.ElementTree as ET


def parseXML(file):
    tree = ET.parse(file)
    root = tree.getroot()
    result = []
    for record in root.findall('record'):
        result.append({
            'id': record.find('id').text,
            'company_name': record.find('company_name').text,
            'job_title': record.find('job_title').text,
            'longitude': record.find('longitude').text,
            'latitude': record.find('latitude').text
        })
    return result


def main():
    # створимо клієнт для доступу до Mongo
    client = pymongo.MongoClient('localhost', 27017)
    # оберемо базу даних - labs
    db = client.labs
    # оберемо, з якою колекцією ми хочемо працювати - db.users_xml
    users_xml_collection = db.jobs_xml
    for i in parseXML('data/dataset.xml'):
        # вставимо дані
        users_xml_collection.insert({
            "id": i["id"],
            "company_name": i["company_name"],
            "job_title": i["job_title"],
            "longitude": i["longitude"],
            "latitude": i["latitude"]
        })


if __name__ == "__main__":
    main()
