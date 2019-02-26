import psql_json_script as json
import psql_xml_script as xml
import psql_csv_script as csv
import mongodb_xml_script as mongo_xml
import mongodb_json_script as mongo_json
import mongo_csv_script as mongo_csv


def load_all():
    xml.main()
    json.main()
    csv.main()
    mongo_xml.main()
    mongo_json.main()
    mongo_csv.main()


def switch(choice):
    switcher = {
        'psql_xml': xml.main,
        'psql_json': json.main,
        'psql_csv': csv.main,
        'all': load_all,
        'mongo xml': mongo_xml.main,
        'mongo_json': mongo_json.main,
        'mongo_csv': mongo_csv.main
    }

    func = switcher.get(choice, lambda: "Invalid choice")
    return func()


if __name__ == "__main__":
    print('Enter :')
    x = input()

    switch(x)
