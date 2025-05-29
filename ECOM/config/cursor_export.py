from db import DBConnection

def export_to_file(query, filename):
    conn = DBConnection().connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    with open(filename, 'w') as f:
        for row in data:
            f.write(','.join(map(str, row)) + '\n')

    conn.close()

