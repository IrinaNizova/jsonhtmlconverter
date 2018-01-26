import json


def load_source_data(path):
    with open(path) as f:
        return json.loads(f.read())


def get_tag_open(string):
    result = ''
    tag_and_id = string.split('#')
    if len(tag_and_id) > 1:
        result += ' id="{}"'.format(tag_and_id[1])
        string = tag_and_id[0]
    classes = [s for s in string.split('.')[1:]]
    if classes:
        result = ' class="{}"'.format(" ".join(classes)) + result
        string = string.split('.')[0]
    return string + result


def escape_html(content):
    return content.replace('<', '&lt;').replace('>', '&gt;')


def insert_data_to_html(data):
    result = ''

    for tag in data:
        if isinstance(data[tag], list):
            content = create_ul_list(data[tag])
        else:
            content = data[tag]
        result += '<{tag_open}>{content}</{tag}>'.format(content=escape_html(content),
                                                         tag_open=get_tag_open(tag), tag=tag.split('.')[0])
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


