Feature: API to Launch orderEntry process.
#https://portail.agir.orange.com/browse/IPCEIS-233
#IPCEI_OM_Sprint1_verify that the process flow "orderEntry" was triggered succesfully

    Scenario: Launch orderEntry process
        Given a request url https://httpbin.org/post
            And a request json payload
                """
                {
                    "processFlowSpecification": "OrderEntry",
                    "channel": [
                        {   
                        "id": "001",             
                        "name": "SHOP"
                        }
                    ],
                    "relatedParty": [
                        {
                        "id": "231-mf4",
                        "name": "Abir",
                        "role": "customer",
                        "@referredType": "individual"
                        }
                    ],
                    "@type": "processFlow"
                }
                """
        When the request sends POST
        Then the response status is 201
        # And  the response json at $.name is equal to "doggie"
        # And  the response json at $.status is equal to "available"