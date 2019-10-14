import json
import psycopg2

if __name__ == '__main__':

    with open('Baltback/config_files/db_config.json') as db_json:
        db_dict = dict(json.load(db_json))
        conn = psycopg2.connect(dbname=db_dict.get("NAME"),
                                user=db_dict.get("USER"),
                                password=db_dict.get("PASSWORD"),
                                host=db_dict.get("HOST"))
        cursor = conn.cursor()
        with open('Baltback/apps/news/res/news.json') as news_json:
            d = dict(json.load(news_json))

            i = 0
            cursor.execute("set datestyle = dmy;")
            for news in d.get("news"):
                cursor.execute("insert into news_news values (%d, '%s', '%s', '%s');" %
                               (i,
                                news.get("title"),
                                news.get("text"),
                                news.get("pub_date")))
                i += 1
            conn.commit()
            cursor.close()
            conn.close()
