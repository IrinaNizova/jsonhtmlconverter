import json


def load_source_data(path):
    with open(path) as f:
        return json.loads(f.read())


def insert_data_to_html(data):
    result = ''
    for tag in data:
        if isinstance(data[tag], list):
            content = create_ul_list(data[tag])
        else:
            content = data[tag]
        result += '<{tag}>{content}</{tag}>'.format(content=content, tag=tag)
    return result


def create_ul_list(notices):

    result = ""
    if not isinstance(notices, list):
        result += insert_data_to_html(notices)
    else:
        for notice in notices:
            result += '<li>' + insert_data_to_html(notice)+ '</li>'
        result = "<ul>" + result + "</ul>"

    return result


def convert_json_to_html(path='source.json'):
    notices = load_source_data(path)
    return create_ul_list(notices)


if __name__ == '__main__':
    print(convert_json_to_html('source_inserted.json'))


