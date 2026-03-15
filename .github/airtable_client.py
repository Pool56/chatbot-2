from airtable import Airtable
import os

AIRTABLE_KEY = os.getenv("AIRTABLE_KEY")
BASE_ID = os.getenv("AIRTABLE_BASE")

table = Airtable(BASE_ID,"Articles",AIRTABLE_KEY)

def save_article(title,content):

    record = {
        "Title": title,
        "Content": content
    }

    table.insert(record)
