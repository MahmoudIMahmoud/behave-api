import json
import pdb
from behave import *
from helpers import test
from helpers.rendering import *
import os
import behave_restful._lang_imp.request_builder as _builder


@given(u'a request call url {url}')
def a_request_call_url_impl(context, url):
    _builder.set_url(context, context.config.userdata.get(url))

@given(u'a request path {path}')
def a_request_path_impl(context, path):
    # path = path.replace('<', u'{').replace('>', u'}')
    _builder.set_url(context, context.request_url+path)

@given (u'the request payload is {payload_file_path}')
def the_request_payload_is(context, payload_file_path):
    if not('/' in payload_file_path):
        payload_file_path = context.templatemapper.get(payload_file_path).data
    filePath= context.config.userdata.get('templateBaseDirectoy')
    filePath = os.path.abspath(filePath)+'/templates'
    filePath = filePath+payload_file_path
    tmplateStr = openTemplate(filePath)
    context.payloadStrTemplate = tmplateStr


@given(u'payload inputs')
def payload_inputs(context):
    tbl = context.table
    valuesDictionary= {}
    for row in tbl.rows: valuesDictionary[row[0]]=row[1]
    #copy the correlation values to be considered when creating the payload.
    for key,value in context.correlation_storage.items():
        valuesDictionary[key]=value
    #Rendering the templated payload using all the values from the correlation and data table.
    renderedPayload = render_the_template(context.payloadStrTemplate,**valuesDictionary)
    _builder.set_json_payload(context, renderedPayload)

@given(u'set the url parameters')
@given(u'set the request parameters')
def set_request_params(context):
    """
    To handle the evaluation of parameters in the url and update the url.
    Example:
        http://example.com/some/path/${xyz}
      and given xyz value is 376
      the url will be updated like that:
        http://example.com/some/path/376
    """
    # context.request_url = context.request_url.replace('<','${').replace('>','}')
    _builder.set_url(context,context.request_url)
    params = context.table
    # import pdb
    # pdb.set_trace()
    resolve = context.vars.resolve
    resolved_params = {resolve(param['param']): resolve(param['value']) for param in params}
    # context.request_params = resolved_params
    # context.request_url = resolve(context.request_url,resolved_params)
    context.request_url = context.request_url.format(**resolved_params)

@given(u'data setup')
def data_setup(context):
    # pdb.set_trace()
    data_set = context.table
    resolver = context.vars.resolve
    data_set = {resolver(param['param']): resolver(param['value']) for param in data_set}
    context.vars.add_vars(data_set)
    print("data_setup")



#Set headers using correlation strorage.
# @given('the request headers template')
# def step_impl(context):
#     print("Setting headers")
    # _builder.set_request_headers(context, context.text)
    # import pdb
    # pdb.set_trace()
    # print("debugging")
    # table = context.table
    # rows = table.rows
    # print(table)
    # headers = context.table
    # # import pdb
    # # pdb.set_trace()
    # resolve = context.vars.resolve
    # resolved_headers = {resolve(headers['param']): resolve(headers['value']) for param in headers}

@given (u'the request headers template is {header_file_path}')
@given (u"the request headers' template is {header_file_path}")
def the_request_header_is(context, header_file_path):
    """
    This step is used to load the headers from template file. 
    """
    import pdb; pdb.set_trace()
    if not('/' in header_file_path):
        header_file_path = context.templatemapper.get(header_file_path).data
    filePath= context.config.userdata.get('templateBaseDirectoy')
    filePath = os.path.abspath(filePath)+'/templates'
    filePath = filePath+header_file_path
    tmplateStr = openTemplate(filePath)
    context.headerStrTemplate = tmplateStr
    context.request_headers =json.loads(tmplateStr)
    # if not (context.request_headers):
    #     context.request_headers =json.loads(tmplateStr)
    # else :
    #     context.request_headers.update(json.loads(tmplateStr))

@given(u'header inputs')
def header_inputs(context):
    # tbl = context.table
    # valuesDictionary= {}
    data_set = context.table
    resolver = context.vars.resolve
    valuesDictionary= {resolver(param['param']): resolver(param['value']) for param in data_set}
    renderedheader = render_the_template(context.headerStrTemplate,**valuesDictionary)
    # context.request_headers=(renderedheader)
    context.request_headers=renderedheader
