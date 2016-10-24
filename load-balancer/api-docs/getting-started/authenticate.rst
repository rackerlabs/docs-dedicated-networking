.. _authenticate-to-identity-service:

============
Authenticate
============

Whether you use cURL, a REST client, or a command-line client (CLI) to send
requests  to the |apiservice|, you need an authentication token to include in
the ``X-Auth-Token``  header of each API request.  You get a token by
submitting an authentication request with valid account credentials to the
following Rackspace Cloud Identity API service endpoint:

.. code::

       https://identity.api.rackspacecloud.com/v2.0

With a valid token, you can send API requests to any of the API service
endpoints that you  are authorized to use. The authentication response
includes a token expiration date. When a token  expires, you can send another
authentication request to get a new one.

.. note::
     For more information about authentication tokens, see the following
     topics in the Rackspace Cloud Identity developer documentation.

     - :rax-devdocs:`Authentication token operations
       <cloud-identity/v2/api-reference/token-operations/#authentication-token>`

       The examples in the Getting Started Guide show how to authenticate by
       using username and API key credentials, which is a more secure way to
       communicate with API services. The authentication token operations
       reference describes other types of credentials that you can use for
       authentication, for example multi-factor authentication passcode.

     - :rax-devdocs:`Manage authentication tokens
       <cloud-identity/v2/getting-started/manage-auth-tokens/#manage-authentication-tokens>`

.. include:: ../common-gs/auth-using-curl.rst
