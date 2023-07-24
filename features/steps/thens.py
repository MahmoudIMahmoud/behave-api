import pdb
from behave import *
from helpers.rendering import *
import os
import jsonschema
from jsonpath import jsonpath
import json  
import curl
import re


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


@then(u'extract response part {json_path_expr} as {var_name}')
@then(u'keep response part {json_path_expr} in {var_name}')
def Keep_response_part(context, json_path_expr, var_name):
    """
    It extracts a json path from the response and save it to the variable name.
    The saved variable can be accessed for reading by ${var_name} like jmeter.
    """
    results=jsonpath(context.response.json(), json_path_expr)
    context.correlation_storage[var_name]=results[0]
    context.vars.add(var_name,results[0])


@then(u'extract a response header {header} as {var_name}')
def extract_a_response_header(context, header, var_name):
    """
    It extracts a heder's part from the response and save it to the variable name.
    The saved variable can be accessed for reading by ${var_name} like jmeter.
    """
    headers = context.response.headers
    results=headers[header]  #Extract a header 
    context.correlation_storage[var_name]=results[var_name]
    context.vars.add(var_name,results[var_name])

@then(u'extract a response regex {regex} as {var_name}')
def extract_a_response_header(context, regex, var_name):
    """
    Extract a regex from the response and save it to the variable name
    """
    rsponse_text = context.response.text
    match = re.search(regex,rsponse_text)
    result = match.group(1)
    context.correlation_storage[var_name]=result
    context.vars.add(var_name,result)


@then(u'debug response')
def Debug_response(context):
    """
    This step is used to debug the api call it self by printing the curl form of the sent request.
    And gives a pdp debug console.
    """
    pdb.set_trace()
    print(curl.parse(context.response))


@then(u'dump curl formatted request')
def Debug_response(context):
    """
    This step is used to debug the api call by printing the curl form of the sent request.
    This step must be called after the request is sent.
    """
    # pdb.set_trace()
    print(curl.parse(context.response))

@then(u'dump response')
def dump_response(context):
    """
    This step is used to debug the api call it self by printing the curl form of thesent request.
    """
    # pdb.set_trace()
    print("=============================================")
    print("=============Response dump===================")
    print("The request:",curl.parse(context.response))
    print("status code:",context.response.status_code)
    print("message:",context.response.ok)
    print("content:",context.response.content)
    print("Text:",context.response.text)
    print("headers:",context.response.headers)
    print("\n============================================")
    print("=============================================")

