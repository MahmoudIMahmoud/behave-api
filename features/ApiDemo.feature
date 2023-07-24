Feature: API to add a new pet to the store.

    Scenario: Add a new pet to collection.
        # Given a request call url site
        Given a request url https://petstore.swagger.io/v2/pet

            And a request json payload
                """
                {
                    "id": 0,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },
                    "name": "doggie",
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                        "id": 0,
                        "name": "string"
                        }
                    ],
                    "status": "available"
                    }
                """
        When the request sends POST
        Then the response status is 200
            And the response json matches
                """
                {
                    "id": 9223372036854766000,
                    "category": {
                        "id": 0,
                        "name": "string"
                    },
                    "name": "doggie",
                    "photoUrls": [
                        "string"
                    ],
                    "tags": [
                        {
                        "id": 0,
                        "name": "string"
                        }
                    ],
                    "status": "available"
                }
                """
            And  the response json at $.name is equal to "doggie"  
            And  the response json at $.status is equal to "available"

    
    Scenario: Update an existing pet
    Given  a request url https://petstore.swagger.io/v2/pet
        And a request json payload
        """
        {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                "id": 0,
                "name": "string"
                }
            ],
            "status": "available"
        }
        """ 
        When the request sends PUT
        Then the response status is 200



Scenario: Get an existing pet working
    Given  a request url https://petstore.swagger.io/v2/pet/{petid}
    And  request parameters
            |param  |value  |
            |petid  |123    |
    # And a request url https://petstore.swagger.io/v2/pet/<petid>
    # And  request parameters
            # |petid |  123 |
            # | param    | value   |
            # | petid    | 123     |
        And  request headers
            |param  |value              |
            |accept |application/json   |
        When the request sends GET
        Then the response status is 200


    Scenario: Get an existing pet
    Given  a request url https://petstore.swagger.io/v2/pet/<petid>
    # And  request parameters
            # |param  |value  |
            # |petid  |123    |
            |petid |  
            |123   |
    # And a request url https://petstore.swagger.io/v2/pet/<petid>
    # And  request parameters
            # |petid |  123 |
            # | param    | value   |
            # | petid    | 123     |
        And  request headers
            |param  |value              |
            |accept |application/json   |
        When the request sends GET
        Then the response status is 200

