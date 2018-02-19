import json

HTTP_VERBS = ('GET', 'POST', 'HEAD', 'OPTIONS', 'PUT', 'PATCH', 'DELETE')


def get_single_endpoint_detail(lines):
    endpoint_details = {
        "endpoint": str(),
        "method": str(),
        "description": str(),
        "request_body": str(),
        "response_body": str()
    }
    lines_iterator = iter(lines)
    for line in lines_iterator:
        if not line or line == '```':
            continue
        if line.startswith('##'):
            endpoint_details["description"] = line.split('## ')[1]
            continue
        if line.startswith(HTTP_VERBS):
            method, endpoint = line.split(' ')[:2]
            endpoint_details["endpoint"] = endpoint
            endpoint_details["method"] = method
            continue
        if line.startswith('__Example__'):
            json_data = parse_and_get_json_from_subsequent_lines(lines_iterator)
            try:
                endpoint_details["request_body"] = json.loads(json_data)
            except ValueError as e:
                print("Error in parsing request_body of {}: {}".format(
                    endpoint_details['endpoint'], e)
                )
                print("Invalid JSON: {}".format(json_data))
                return None
            continue
        if line.startswith('__Response__'):
            json_data = parse_and_get_json_from_subsequent_lines(lines_iterator)
            try:
                endpoint_details["response_body"] = json.loads(json_data)
            except ValueError as e:
                print("Error in parsing response_body of {}: {}".format(
                    endpoint_details['endpoint'], e)
                )
                print("Invalid JSON: {}".format(json_data))
                return None
            continue
    return endpoint_details


def parse_and_get_json_from_subsequent_lines(lines_iterator):
    try:
        next_line = next(lines_iterator)
    except StopIteration:
        return ''
    while next_line != '```json':
        try:
            next_line = next(lines_iterator)
        except StopIteration:
            return ''
    # Skip the row having starting json tag
    next_line = next(lines_iterator)
    array_of_json_statements = list()
    while next_line != '```':
        array_of_json_statements.append(next_line)
        try:
            next_line = next(lines_iterator)
        except StopIteration:
            pass

    json_statements = ''.join(array_of_json_statements)
    json_statements = json_statements.replace("...", "")
    return json_statements


def get_json_from_endpoints(lines):
    all_lines = lines.split('\n')
    next_endpoint_starting_location = [
        i for i, line in enumerate(all_lines) if line.startswith('##')
    ]
    endpoint_json_list = list()
    for x in range(len(next_endpoint_starting_location)):
        starting_point = next_endpoint_starting_location[x]
        try:
            ending_point = next_endpoint_starting_location[x + 1] - 1
        except IndexError:
            # This is the end of the file
            ending_point = None
        valid_data = get_single_endpoint_detail(all_lines[starting_point:ending_point])
        if not valid_data:
            continue
        endpoint_json_list.append(valid_data)
    return endpoint_json_list


def generate_json_from_docs_file(filename='proposed_endpoints.md'):
    lines = None
    with open(filename, 'r') as endpoint_file:
        lines = endpoint_file.read()
    json_data = get_json_from_endpoints(lines)

    with open('endpoints_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    generate_json_from_docs_file()
