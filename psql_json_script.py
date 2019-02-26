import psycopg2
import json


def main():
    conn_string = "host='localhost' dbname='labs' user='kate'"
    print("Connecting to database\n ->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")

    for i in json.loads(open('./data/dataset.json').read()):
        query_string = """
            INSERT INTO jobs_json(id, company_name, job_title, longitude, latitude) VALUES
            ('{0}', '{1}', '{2}', '{3}', '{4}');
            """
        query = query_string.format(i['id'],
                                    i['company_name'],
                                    i['job_title'],
                                    i['longitude'],
                                    i['latitude'])
        print(query)

        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
