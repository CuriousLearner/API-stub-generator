import os
import pytest
import json

from .utils import FIXTURE_DIR
from src.serialize_data import get_json_from_endpoints


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "proposed_endpoints.md"))
def test_data_serialization(datafiles):
    lines = datafiles.listdir()[0].read()

    json_data = json.dumps(get_json_from_endpoints(lines), sort_keys=True)

    expected_json = json.dumps(
        [
            {
                "description": "Login to the app",
                "request_body": {"email": "john@example.com", "password": "123456"},
                "response_body": {
                    "email": "john@example.com",
                    "last_name": "Doe",
                    "first_name": "John",
                    "auth_token": "qduvpuMvqZUx4Emcpevp.RaGnPgoGZKvGBUHDuivwkvFQowYcwFq.FUGArGvzzfeGe",
                    "phone_number": "+123423423423",
                    "id": "e59d2c4f-ef3f-4455-aa41-c70af8c4e2df",
                },
                "endpoint": "/api/users/login",
                "method": "POST",
            }
        ],
        sort_keys=True,
    )

    assert json_data == expected_json
