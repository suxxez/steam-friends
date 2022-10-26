import json

from src.main import get_openapi_spec

with open("docs/openapi.json", "w") as file:
    file.write(json.dumps(get_openapi_spec()))
