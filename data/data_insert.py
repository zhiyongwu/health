import json
from apps import db


def save_data_to_db():
    with open("data/data.jl") as file:
        for line in file:
            data = json.loads(line)
            name = data['name']
            value = data['value']
            alias = data['alias']
            sql = "insert into food_purine (`name`,`value`,`alias`) values ('%s','%s','%s') " % (name, value, alias)
            print(sql)
            cursor = db.cursor()
            cursor.execute(sql)
            for each in cursor:
                print(each)
            cursor.connection.commit()
            cursor.close()


if __name__ == '__main__':
    save_data_to_db()
