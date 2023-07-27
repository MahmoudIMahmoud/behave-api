Feature: API to add a new pet to the store.

Background:Set background data for the scenarios
    Given data setup
        |param  |value|
        |mypetid|  2  |

    Scenario: Add a new pet to collection.
        Given a request call url baseurl
            And a request path /pet/
            And the request payload is petbody
            #/body/pet.template
            And payload inputs
                |Name         |Value|
                |id           |0  |
                |category_name|Cat  |
                |pet_name     |Selia|
            And the request headers template is basicheader
                # |param  |value |
                # |Content-Type|application/json|
                # |Accept|application/json|
        When the request sends POST
        Then the response status is 200
        And  Assert response matches the schema petaddscema
            And  the response json at $.name is equal to "Selia"  
            And  the response json at $.status is equal to "available"
            And  keep response part $.name in petname
            And  keep response part $.id in added_pet_id
            And  extract a response regex id":\s*(\d+), as pet_id_rgx
            And  dump response


Scenario: Get an existing pet working
    Given  request parameters
            |param  |value  |
            |petid  |${pet_id_rgx}    |
    And a request url https://petstore.swagger.io/v2/pet/${petid}
        And  request headers
            |param  |value              |
            |accept |application/json   |
        When the request sends GET
        Then the response status is 200
        And  debug response


Scenario: Get an existing pet working versions2
    Given a request url https://petstore.swagger.io/v2/pet/${added_pet_id}
        And  request headers
            |param  |value              |
            |accept |application/json   |
        When the request sends GET
        Then debug response
        Then the response status is 200
