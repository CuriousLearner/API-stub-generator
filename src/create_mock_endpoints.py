from __future__ import annotations

import json
import re
import unicodedata
from typing import Any


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    return re.sub(r"[-\s]+", "_", value)


def generate_code_for_single_mock_api_route(endpoint_data: dict[str, Any]) -> str:
    if not endpoint_data["endpoint"] or not endpoint_data["method"]:
        return ""
    output_data = "@app.route('" + str(endpoint_data["endpoint"]) + "'"
    output_data += ", methods=['" + str(endpoint_data["method"]) + "'])\n"
    output_data += "def " + slugify(str(endpoint_data["description"])) + "():\n"
    output_data += (
        "    return Response(json.dumps(" + str(json.dumps(endpoint_data["response_body"], sort_keys=True)) + "), "
    )
    output_data += "mimetype='application/json; charset=utf-8')\n"
    output_data += "\n\n"
    return output_data


def create_mock_api_endpoints(json_filename: str = "endpoints_data.json", filename: str = "app.py") -> None:
    with open(json_filename) as json_file:
        data: list[dict[str, Any]] = json.load(json_file)
    generated_code_list = [
        "import json\n",
        "\n",
        "from flask import Flask, Response\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n\n",
    ]
    for endpoint_data in data:
        generated_code_list.append(generate_code_for_single_mock_api_route(endpoint_data))

    generated_code_list.extend(['if __name__ == "__main__":\n', "    app.run()"])
    with open(filename, "w") as outfile:
        outfile.write("".join(generated_code_list))
        print("Run `python app.py` to host your app")


if __name__ == "__main__":
    create_mock_api_endpoints()
