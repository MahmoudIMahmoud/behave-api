Feature: Launch Order entry process

Scenario: Send a bad json format
    Given a request url http://localhost:8086/processManagement/v4/processFlow
    And a request json payload
    """
    A JSON WITH INVALID  FORMAT SHOULD BE HERE.
    """
    When the request sends POST
    Then the response status is 400
    And the response json at $.reason is equal to "invalid request body"

 
Scenario Outline: eating
  #==with product offering and offer valid and eligible and configuration session not created
    Given a request url "http://localhost:8086/processManagement/v4/processFlow"
    And a request json at "relatedEntity" list at "@type" is equal to "ProductOffering"
    And  set the payload as 
        """
        Parametrised
        """ 
        |type|valid|
        |offer|eligible|
    And the offer is valid
    And offer is eligible
    And the configuration session is not created
    #And the configuration session status is "Not Created" #suggested
    When the request sends "POST"
    Then the response status is "201" 
    And the response json at "nextTaskToBePerformed" list at "title" is equal to"OrderEntry.selectOffer"
    And the response json at "nextTaskToBePerformed" list at "title" is equal to "OrderEntry.cancelOrder"
    And the response json at description is equal to "Configuration session is not created, try later"
    
    #== with product offering
    Given a request url "http://localhost:8086/processManagement/v4/processFlow"
    And a request json at "relatedEntity" list at "@type" is equal to "ProductOffering"
    And the offer is valid 
    And the offer is eligible 
    And the configuration session was created
    #And the configuration session status is "Created"  #Suggested
    When the request sends "POST"
    Then the response status is "201" 
    And the response json at "nextTaskToBePerformed" list at "title" is equal to"OrderEntry.confirmConfiguration"
    And the response json at "nextTaskToBePerformed" list at "title" is equal to "OrderEntry.cancelOrder"