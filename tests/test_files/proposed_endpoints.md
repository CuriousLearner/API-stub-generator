For api overview and usages, check out [this page](overview.md).

[TOC]

# Authorization and Authentication

All the api calls from mobile apps needs to have the following headers:

```
X-CLIENT-ID: <id-obtained-from-cms>
```

Once the user is logged in, add additional header `Authorization` like this:

```
Authorization: Token <auth-token-here>
```

`auth_token` is obtained after making the `/api/users/login` api call.


## Login to the app

```
POST /api/users/login
```

__Parameters__

Name         | Type    | Description
-------------|---------|---------------------------------------------
email        | string  | Email of recruiter or student
password     | string  | password of recruiter or student

__Example__
```json
{
    "email": "john@example.com",
    "password": "123456"
}
```

__Response__
```json
{
    "id": "e59d2c4f-ef3f-4455-aa41-c70af8c4e2df",
    "phone_number": "+123423423423",
    "auth_token": "qduvpuMvqZUx4Emcpevp.RaGnPgoGZKvGBUHDuivwkvFQowYcwFq.FUGArGvzzfeGe",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
}
```
