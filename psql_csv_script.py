import psycopg2
import csv


def main():
    conn_string = "host='localhost' dbname='labs' user='kate'"
    print("Connecting to database\n ->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")

    csvfile = open('./data/dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip headers
    csvreader.__next__()

    for i in csvreader:
        query_string = """
            INSERT INTO jobs_csv(id, company_name, job_title, longitude, latitude) VALUES
            ('{0}', '{1}', '{2}', '{3}', '{4}');
            """
        query = query_string.format(i[0], i[1], i[2], i[3], i[4])
        print(query)

        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
