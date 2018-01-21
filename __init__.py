import json


def load_source_data(path):
    with open(path) as f:
        return json.loads(f.read())


def insert_data_to_html(data):
    tags = list(data.keys())
    return "<li><{tag_title}>{title}</{tag_title}><{tag_body}>{body}</{tag_body}></li>".\
        format(title=data[tags[0]], body=data[tags[1]], tag_title=tags[0], tag_body=tags[1])


def convert_json_to_html(path='source.json'):
    notices = load_source_data(path)
    return create_ul_list(notices)

def create_ul_list(notices):
    result = ""
    for notice in notices:
        result += insert_data_to_html(notice)
    return "<ul>" + result + "</ul>"


if __name__ == '__main__':
    convert_json_to_html()


