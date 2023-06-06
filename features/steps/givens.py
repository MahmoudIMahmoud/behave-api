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
    path = path.replace('<', u'{').replace('>', u'}')
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

@given(u'Set the request parameters')
def set_request_params(context):
    """
    """
    context.request_url = context.request_url.replace('<','{').replace('>','}')
    _builder.set_url(context,context.request_url)
    params = context.table
    # import pdb
    # pdb.set_trace()
    resolve = context.vars.resolve
    resolved_params = {resolve(param['param']): resolve(param['value']) for param in params}
    context.request_params = resolved_params
    # context.request_url = resolve(context.request_url,resolved_params)
    context.request_url = context.request_url.format(**resolved_params)