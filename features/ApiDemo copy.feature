Feature: API to add a new pet to the store.

    Scenario: Add a new pet to collection.
        Given a request call url baseurl
            And a request path /pet
            And the request payload is petbody
            #/body/pet.template
            And payload inputs
                |Name         |Value|
                |id           |135  |
                |category_name|Cat  |
                |pet_name     |Selia|
        When the request sends POST
        Then the response status is 200
        And  Assert response matches the schema petaddscema
            # And the response json matches
            #     """
            #     {
            #         "id": 123,
            #         "category": {
            #             "id": 0,
            #             "name": "Cat"
            #         },
            #         "name": "Selia",
            #         "photoUrls": [
            #             "string"
            #         ],
            #         "tags": [
            #             {
            #             "id": 0,
            #             "name": "string"
            #             }
            #         ],
            #         "status": "available"
            #     }
            #     """
            And  the response json at $.name is equal to "Selia"  
            And  the response json at $.status is equal to "available"
            And  keep response part $.name in petname
            # And  Keep response part
#     Scenario: Update an existing pet
#     Given  a request url https://petstore.swagger.io/v2/pet
#         And a request json payload
#         """
#         {
#             "id": 0,
#             "category": {
#                 "id": 0,
#                 "name": "string"
#             },
#             "name": "doggie",
#             "photoUrls": [
#                 "string"
#             ],
#             "tags": [
#                 {
#                 "id": 0,
#                 "name": "string"
#                 }
#             ],
#             "status": "available"
#         }
#         """ 
#         When the request sends PUT
#         Then the response status is 200



# Scenario: Get an existing pet working
#     Given  a request url https://petstore.swagger.io/v2/pet/{petid}
#     And  request parameters
#             |param  |value  |
#             |petid  |123    |
#     # And a request url https://petstore.swagger.io/v2/pet/<petid>
#     # And  request parameters
#             # |petid |  123 |
#             # | param    | value   |
#             # | petid    | 123     |
#         And  request headers
#             |param  |value              |
#             |accept |application/json   |
#         When the request sends GET
#         Then the response status is 200


#     Scenario: Get an existing pet
#     Given  a request url https://petstore.swagger.io/v2/pet/<petid>
#     # And  request parameters
#             # |param  |value  |
#             # |petid  |123    |
#             |petid |  
#             |123   |
#     # And a request url https://petstore.swagger.io/v2/pet/<petid>
#     # And  request parameters
#             # |petid |  123 |
#             # | param    | value   |
#             # | petid    | 123     |
#         And  request headers
#             |param  |value              |
#             |accept |application/json   |
#         When the request sends GET
#         Then the response status is 200

