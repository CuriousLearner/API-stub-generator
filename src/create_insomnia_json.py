import copy
import datetime
import json
import time
import uuid


def random_id():
    return uuid.uuid4().hex


def current_timestamp():
    return int(round(time.time() * 1000))


def current_date():
    date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    return date[:-3] + "Z"


wrk_id = random_id()

base_json = {
    "_type": "export",
    "__export_format": 4,
    "__export_date": current_date(),
    "__export_source": "insomnia.desktop.app:v7.1.1",
    "resources": [
        {
            "_id": f"wrk_{wrk_id}",
            "created": current_timestamp(),
            "description": "",
            "modified": current_timestamp(),
            "name": "Stub API",
            "parentId": "null",
            "_type": "workspace"
        },
        {
            "_id": f"env_{random_id()}",
            "color": "null",
            "created": current_timestamp(),
            "data": {},
            "dataPropertyOrder": "null",
            "isPrivate": "false",
            "modified": current_timestamp(),
            "name": "Base Environment",
            "parentId": f"wrk_{wrk_id}",
            "_type": "environment"
        },
    ]
}


base_request_resource = {
    "_id": "",
    "authentication": {},
    "body": {},
    "created": current_timestamp(),
    "description": "",
    "headers": [],
    "isPrivate": "false",
    "method": "",
    "modified": current_timestamp(),
    "name": "",
    "parameters": [],
    "parentId": f"wrk_{wrk_id}",
    "url": "",
    "_type": "request"
}


def create_json(list_of_endpoints):
    for endpoint in list_of_endpoints:
        request_resource = copy.deepcopy(base_request_resource)
        request_resource["_id"] = f"req_{random_id()}"
        request_resource["method"] = endpoint["method"]
        if endpoint["request_body"] != "":
            request_resource["body"]["mimetype"] = "application/json"
            request_resource["body"]["text"] = json.dumps(
                endpoint["request_body"], indent=2
            )
        request_resource["name"] = endpoint["description"]
        request_resource["url"] = endpoint["endpoint"]
        base_json["resources"].append(request_resource)
    return base_json


def create_insomnia_api_endpoints(
    json_filename="endpoints_data.json", filename="endpoints_data_insomnia.json"
):
    data = None
    with open(json_filename, "r") as json_file:
        data = json.load(json_file)
    final_json = create_json(data)
    with open(filename, "w") as outfile:
        json.dump(final_json, outfile)


if __name__ == "__main__":
    create_insomnia_api_endpoints()
