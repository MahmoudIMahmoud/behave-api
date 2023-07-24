# All the predifined steps

## Given
```python
-  @given('a request url {url}')
-  @given('a request json payload')
-  @given('request headers')
-  @given('request parameters')
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
```
