Feature: test demo
  Scenario: create product in cpib
    Given   a request call url descoBase
    And a request path /product
    And  request headers
      |param           |value             |
      |Content-Type    |application/json  |
      |Accept          |*/*               |
      |Accept-Encoding |gzip, deflate, br |
      |Connection      |keep-alive        |
    And the request payload is body
    And random id generated in poi_id
    And payload inputs
      |Name            |Value             |
      |product_order_id|${poi_id}         |
    When the request sends POST
    Then  dump response
    Then the response status is 201