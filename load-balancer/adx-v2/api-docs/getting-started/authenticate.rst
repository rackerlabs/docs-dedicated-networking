.. _authenticate-to-identity-service:

Authenticate
-------------------------------------------------

Whether you use cURL, a REST client, or a command line client (CLI) to send requests 
to the |apiservice|, you need an authentication token to include in the ``X-Auth-Token`` 
header of each API request.

With a valid token, you can send API requests to any of the API service endpoints that you 
are authorized to use. The authentication response includes a token expiration date. When a token 
expires, you can send another authentication request to get a new one.
 
.. include:: ../common-gs/auth-using-curl.rst


