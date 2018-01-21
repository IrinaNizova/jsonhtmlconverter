import json


def load_source_data(path):
    with open(path) as f:
        return json.loads(f.read())


def insert_data_to_html(data, tags):
    return "<{tag_title}>{title}</{tag_title}><{tag_body}>{body}</{tag_body}>".\
        format(title=data['title'], body=data['body'], tag_title=tags[0], tag_body=tags[1])


def convert_json_to_html(path='source.json', tags=('h3', 'div')):
    notices = load_source_data(path)
    result = ""
    for notice in notices:
        result += insert_data_to_html(notice, tags)
    return result

if __name__ == '__main__':
    convert_json_to_html()


