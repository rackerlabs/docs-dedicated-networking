.. _authentication-ovw: 

==============
Authentication
==============

Each REST request against the |product name| service requires the inclusion of a specific 
authorization token, supplied in the ``X-Auth-Token`` HTTP header. Customers obtain this 
token by first using the Rackspace Cloud Identity service and supplying a valid user name 
and API access key.

To authenticate, you submit a ``POST/v2.0/tokens`` request, presenting valid Rackspace 
customer credentials in the message body to a Rackspace authentication endpoint.

.. _auth-credentials:

Get your credentials
~~~~~~~~~~~~~~~~~~~~

You can use either of the following sets of credentials:

-  Your user name and password

-  Your user name and API key

Your user name and password are the ones that you use to log in to the 
`Rackspace Cloud control panel`_. After you are logged in, you can use the Rackspace 
Cloud Control Panel to obtain your API key.


..  note:: 
    If you authenticate with username and password credentials, you can use multi-factor 
    authentication to add an additional level of account security. This feature is not 
    implemented for username and API credentials. For more information, 
    see :rax-devdocs:
    `Multi-factor authentication<cloud-identity/v2/developer-guide/#document-authentication-info/use-mfa-ops>`  
    in the *Cloud Identity Client Developer Guide*.

.. _Rackspace Cloud control panel: https://mycloud.rackspace.com/


.. _auth-global:

Use the Global Authentication Endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the following global endpoint to authenticate with the Rackspace Cloud Identity service:

``https://identity.api.rackspacecloud.com/v2.0/``


.. _send-credentials:

Send your credentials to your authentication endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have your credentials and the authentication endpoint, you have 
everything you need to authenticate by using the Rackspace Cloud Identity service.

You can use `cURL`_ to perform the authentication process in two steps: get a token, and 
send the token to a service.

.. _cURL: http://curl.haxx.se/

#. Get an authentication token by providing your user name and either your API key or 
   your password. Following are examples of both approaches:

   **Example: User name and API key**

   .. code::  

        curl -X POST https://auth.api.rackspacecloud.com/v2.0/tokens -d 
    	'{ "auth":{ "RAX-KSKEY:apiKeyCredentials":{ "username":"yourUserName", "apiKey":"yourApiKey" } } }' -H "Content-type: application/json"


	**Example: User name and password**

	.. code::  

    	curl -X POST https://auth.api.rackspacecloud.com/v2.0/tokens -d
    	'{"auth":{"passwordCredentials":{"username":"yourUserName","password":"yourPassword"}}}' -H "Content-type: application/json"


#. Review the authentication response.

   -  Successful authentication returns a token that you can use as evidence that your 
      identity has already been authenticated along with a service catalog, which lists 
      the endpoints that you can use for Rackspace Cloud services. To use the token, pass 
      it to other services as an `X-Auth-Token` header.

   -  If the Identity service returns a returns a 401 message with a request for 
      additional credentials, your account requires 
      :rax-devdocs:`Multi-factor authentication<cloud-identity/v2/developer-guide/#document-authentication-info/use-mfa-ops>`. 
      To complete the authentication process, submit a second **POST tokens** request 
      with these multi-factor authentication credentials:

   -  The session ID value returned in the `WWW-Authenticate: OS-MF sessionId` header 
      parameter that is included in the response to the initial authentication request.

   -  The passcode from the mobile phone associated with your user account.
          
   **Example: Authentication request with multi-factor authentication credentials**

   .. code::  

    	$curl https://identity.api.rackspacecloud.com/v2.0/tokens \
    	-X POST \
    	-d '{"auth": {"RAX-AUTH:passcodeCredentials": {"passcode":"1411594"}}}'\
    	-H "X-SessionId: $SESSION_ID" \
    	-H "Content-Type: application/json" --verbose | python -m json.tool


#. Use the authentication token to send a **GET** request to a service that you want to use.

   The following example shows how to pass an authentication token to the |apiservice| by 
   using the token and |product name| endpoint that was returned in the service catalog.

   **Example: cURL get distros request: JSON**

   .. code::  

    	curl -i -X GET https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/distros -d  \
    	-H "X-Auth-Token: yourAuthToken" \
		-H "Accept: application/json"\
		-H "Content-type: application/json"


   Authentication tokens are typically valid for 24 hours. Applications should be designed 
   to re-authenticate after receiving a 401 (Unauthorized) response from a service endpoint. 

   .. note:: 
    	
    	If you are programmatically parsing an authentication response, be aware that 
    	service names are stable for the life of the particular service and can be used as 
    	keys. You should also be aware that a user's service catalog can include multiple 
    	uniquely named services that perform similar functions. In Cloud Identity 2.0, 
    	the service type attribute can be used as a key by which to recognize similar 
    	services. For more information about the service catalog, see 
    	:rax-devguide:`Identity API Developer Guide <v2/docs-cloud-identity>`. 
    	
