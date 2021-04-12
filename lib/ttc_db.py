import sqlite3

ttc = Ttc_Price()
a = ttc.New_Soup()

conn = sqlite3.connect("TTC.db")
sour = conn.cursor()
try:
    sour.execute('DROP TABLE TTC_price')
    conn.commit()
except:
    pass


sqll = '''
        create table TTC_price(id integer primary key autoincrement,
        last_seen integer,
         item_name text,
         item_place text,
         sigle_price integer,
         total_price integer
        )
        '''
sour.execute(sqll)
conn.commit()

for item in a:
    for index in range(len(item)):
        item[index] = '"'+item[index]+'"'
    sql = '''insert into TTC_price(
            last_seen, item_name, item_place, sigle_price, total_price)
            values(%s)'''%','.join(item)
    sour.execute(sql)

conn.commit()
sour.close()
conn.close()