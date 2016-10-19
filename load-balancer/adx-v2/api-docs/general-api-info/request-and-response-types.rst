.. _request-and-response:

==========================
Request and response types
==========================

The |product name| API supports JSON data serialization formats. The request format is 
specified by using the ``Content-Type`` header and is required for operations that have a 
request body. The response format can be specified in requests either by using the 
``Accept`` header or by adding ``.json`` extension to the request URI. Note that JSON is 
the default format for data serialization.

**Response formats**

+--------+------------------+-----------------+---------+
| Format |  Accept header   | Query extension | Default |
+========+==================+=================+=========+
| JSON   | application/json | .json           | Yes     |
+--------+------------------+-----------------+---------+
