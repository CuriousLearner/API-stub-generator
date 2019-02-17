# API Stub Generator

[![Build Status](https://travis-ci.org/CuriousLearner/API-stub-generator.svg?branch=master)](https://travis-ci.org/CuriousLearner/API-stub-generator)

Mock proposed API endpoints with stub.

## Inspiration

I'm a lazy programmer. Basically, if you would tell me that I've to do the same task without applying my brain over and over again, I'll try to automate it with code (if I can xD)

The proposed API docs I write, have to be then mocked for APP / Front-End Developers so that they're not blocked by actual API calls. Later they can replace these stubs with actual API calls. With more requirements coming in, the proposed endpoint changes over time and the stubs have to be updated. I found myself in a viscous circle of keeping the both up to date which wastes my dev cycles (where I can work on generating actual endpoints) & thus created this small utility to help me.

## Setup

Clone the repo & `cd` to it:

```
git clone https://github.com/CuriousLearner/API-stub-generator.git && cd API-stub-generator
```

Install pipenv

```
[sudo] pip install pipenv
```

Install all dependencies using pipenv

```
pipenv install
```

## Usage

Run `pipenv run python serialize_data.py` to generate JSON file named `endpoints_data.json`. One can specify the path of the proposed endpoints docs  using `--file-path` option in the above command.

Run `pipenv run python create_mock_endpoints.py` to generate `app.py` with all the code for the Mocked end points.

Run `pipenv run python app.py` & hit any endpoint that you defined in the `proposed_endpoints.md` doc.


## GET - SET - GO

- Avoiding the viscous circle of updating docs and stubs in three easy steps.

## GET ready with `serialize_data.py`

This script parses the `proposed_endpoints.md` file and generates a JSON file `endpoints_data.json` listing all the endpoints to be generated.

## SET with `create_mock_endpoints.py`

This script parses the JSON file `endpoints_data.json` and generates `app.py` file containing simple flask app with all the endpoints.

## GO with `app.py`

Just do a `python app.py` and your API endpoints are now live on [http://localhost:5000](http://localhost:5000)
