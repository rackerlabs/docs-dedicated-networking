.. _request-and-response:

==========================
Request and response types
==========================

The |apiservice| supports JSON data serialization formats. The request
format is specified by using the ``Content-Type`` header and is required for
operations that have a request body. The response format can be specified in
requests by using the ``Accept`` header. Note that JSON is the default and only 
format for data serialization.

**Response formats**

+--------+-------------------------+---------+
| Format |   Content-Type header   | Default |
+========+=========================+=========+
| JSON   |    application/json     |   Yes   |
+--------+-------------------------+---------+
