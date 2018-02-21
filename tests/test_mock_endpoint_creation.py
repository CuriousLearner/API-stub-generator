import os
import pytest
import json

from .utils import FIXTURE_DIR
from src.create_mock_endpoints import generate_code_for_single_mock_api_route


@pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'endpoints_data.json'),
)
def test_generated_code_from_serialization(datafiles):
    data = datafiles.listdir()[0].read()

    json_data = json.loads(data)
    for each_endpoint in json_data:
        generated_code = generate_code_for_single_mock_api_route(
            each_endpoint
        )
        expected_response = str(
            u'@app.route(\'/api/users/login\', methods=[\'POST\'])'
            '\ndef login_to_the_app():\n    return Response('
            'json.dumps({"auth_token": "qduvpuMvqZUx4Emcpevp.RaGnPgoGZKvGBUHDuiv'
            'wkvFQowYcwFq.FUGArGvzzfeGe", "email": "john@example.com", '
            '"first_name": "John", "id": "e59d2c4f-ef3f-4455-aa41-c70af8c4e2df"'
            ', "last_name": "Doe", "phone_number": "+123423423423"}), '
            'mimetype=\'application/json; charset=utf-8\')\n\n\n'
        )

        assert generated_code == expected_response
