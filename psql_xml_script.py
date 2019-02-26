import psycopg2
import xml.etree.ElementTree as ET


def parseXML(file):
    # відкриваємо файл на читання і парсимо дерево
    tree = ET.parse(file)
    # отримуємо кореневий елемент XML документу
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
    # оголошуємо строку підключення до бази у PostgreSQL
    conn_string = "host='localhost' dbname='labs' user='kate'"
    # Виводимо строку
    print("Connecting to database\n ->%s" % (conn_string))
    # отримуємо підключення, якщо воно невдале, бібліотека кине виключення
    conn = psycopg2.connect(conn_string)
    # conn.cursor повертає обʼєкт курсору - за допомогою його можна виконувати запити
    cursor = conn.cursor()
    print("Connected!\n")
    # проходимо через всі елементи XML документу

    # parseXML('dataset.xml')
    for i in parseXML('data/dataset.xml'):
        query_string = """
            INSERT INTO jobs_xml(id, company_name, job_title, longitude, latitude) VALUES
            ('{0}', '{1}', '{2}', '{3}', '{4}');
            """
        query = query_string.format(i['id'],
                                    i['company_name'],
                                    i['job_title'],
                                    i['longitude'],
                                    i['latitude'])
        print(query)
        # і записуємо у базу
        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
