Authenticate
------------

In order to successfully generate a valid Authentication Token, you must
perform the following steps.

1.  Log into your `My
    Rackspace <https://my.rackspace.com/portal/auth/login>`__ with your
    MyRackspace Account number, Username and Password.

    -  **Username and API key** To retrieve your MyRackspace API access Username
       and API Key, you must follow the following steps:

        -  On the top menu next to MyRackspace logo, you will find the
           Account option. Click and view dropdown, select ``User List``
        -  Once in ``User List`` page, under Active Users tab select your
           user account.
        -  Below API Access header, you will have your API access Username.
        -  You will also see your hidden API key. Go ahead and click on show
           to see your API key.

2.  Once you have all required information, go ahead and submit a POST
    call to identity’s tokens url as shown in the following cURL example:

**Use your API Access Username and API key:**

.. code:: javascript

    curl https://identity.api.rackspacecloud.com/v2.0/tokens  \
     -X POST \
     -d '{"auth":{"RAX-KSKEY:apiKeyCredentials":{"username":"yourUserName","apiKey":"yourPassword"}}}' \
     -H "Content-type: application/json" | python -m json.tool

3.  Check the `authentication
    response <https://developer.rackspace.com/docs/cloud-identity/v2/developer-guide/#samp-auth-resp>`__.
    
    -  If you get a successful response, use the information in the
       authentication response `to submit an API
       request <https://developer.rackspace.com/docs/cloud-identity/v2/developer-guide/#submit-an-api-request>`__.
    -  If you get an unsuccessful response, review the response message and
       the following error message descriptions to determine next steps.

.. code::

    400 Invalid request body: unable to parse Auth data. Please review XML or JSON formatting



Review the authentication request for syntax or coding errors. If you
are using cURL, see `How cURL commands work <https://developer.rackspace.com/docs/cloud-identity/v2/developer-guide/#how-curl-commands-work>`__.


    You can find additional error message information in the `Token
    operations API
    reference <https://developer.rackspace.com/docs/cloud-identity/v2/developer-guide/#token-operations>`__.
