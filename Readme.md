# All the predifined steps

## Given
```python
-  @given('a request url {url}')
-  @given('a request json payload')
-  @given('request headers')
-  @given('request parameters')
-  @given(u'a request call url {url}')
-  @given(u'a request path {path}')
-  @given (u'the request payload is {payload_file_path}')
-  @given(u'payload inputs')
-  @given(u'set the request parameters')
-  @given(u'data setup')
-  @given('the request headers template')
```
## When
```python
-  @when('the request sends {method}')
```
## Then
```python
-  @then('the response status is {status}')
-  @then('the response json matches')
-  @then('the response json matches defined schema {schema_id}')
-  @then('the response json at {json_path} is equal to {value_str}')
-  @then('the response json at {json_path} is not equal to {value_str}')
-  @then('the response json at {json_path} starts with {value_str}')
-  @then('the response json at {json_path} ends with {value_str}')
-  @then('the response json at {json_path} contains {value_str}')
-  @then('the response json at {json_path} does not contain {value_str}')
-  @then('the response json at {json_path} is null')
-  @then('the response json at {json_path} is not null')
-  @then('the response json at {json_path} is true')
-  @then('the response json at {json_path} is false')
-  @then(u'Assert response matches the schema {schema_ref}')
-  @then(u'extract response part {json_path_expr} as {var_name}')
-  @then(u'keep response part {json_path_expr} in {var_name}')
-  @then(u'extract a response header {header} as {var_name}')
-  @then(u'extract a response regex {regex} as {var_name}')
-  @then(u'debug response')
-  @then(u'dump curl formatted request')
-  @then(u'dump response')

```
