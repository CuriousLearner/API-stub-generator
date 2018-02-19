# API Stub Generator

[![Build Status](https://travis-ci.org/CuriousLearner/api-stub.svg?branch=master)](https://travis-ci.org/CuriousLearner/api-stub)

Mock proposed API endpoints with stub.

## Inspiration

I'm a lazy programmer. Basically, if you would tell me that I've to do the same task without applying my brain over and over again, I'll try to automate it with code (if I can xD)

The proposed API docs I write, have to be then mocked for APP / Front-End Developers so that they're not blocked by actual API calls. Later they can replace these stubs with actual API calls. With more requirements coming in, the proposed endpoint changes over time and the stubs have to be updated. I found myself in a viscous circle of keeping the both up to date which wastes my dev cycles (where I can work on generating actual endpoints) & thus created this small utility to help me.

## GET - SET - GO

- Avoiding the viscous circle of updating docs and stubs in three easy steps.

## GET ready with `serialize_data.py`

This script parses the `proposed_endpoints.md` file and generates a JSON file `endpoints_data.json` listing all the endpoints to be generated.

## SET with `create_mock_endpoints.py`

This script parses the JSON file `endpoints_data.json` and generates `app.py` file containing simple flask app with all the endpoints.

## GO with `app.py`

Just do a `python app.py` and your API endpoints are now live on [http://localhost:5000](http://localhost:5000)
