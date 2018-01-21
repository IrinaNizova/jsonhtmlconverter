import json


def load_source_data(path):
    with open(path) as f:
        return json.loads(f.read())


def insert_data_to_html(data):
    return "<h1>{0}</h1><p>{1}</p>".format(data['title'], data['body'])


def convert_json_to_html(path='source.json'):
    notices = load_source_data(path)
    result = ""
    for notice in notices:
        result += insert_data_to_html(notice)
    return result

if __name__ == '__main__':
    convert_json_to_html()


