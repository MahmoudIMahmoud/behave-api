from behave import *
from helpers.rendering import *
import os
import jsonschema
from jsonpath import jsonpath
import json  

@then(u'Assert response matches the schema {schema_ref}')
def Assert_response_matches_the_schema(context, schema_ref):
    json_body = context.response.json()
    if not('/' in schema_ref):
        schema_file_path = context.templatemapper.get(schema_ref).data
    filePath= context.config.userdata.get('templateBaseDirectoy')
    filePath = os.path.abspath(filePath)+'/templates'
    filePath = filePath+schema_file_path
    schemaFile = openTemplate(filePath) # Reuse the function as is.
    # Validate args are both objects not strings.
    jsonschema.validate(json_body, json.loads(schemaFile))


@then(u'Keep response part {json_path_expr} in {var_name}')
def Keep_response_part(context, json_path_expr, var_name):
    results=jsonpath(context.response.json(), json_path_expr)
    context.correlation_storage[var_name]=results[0]
