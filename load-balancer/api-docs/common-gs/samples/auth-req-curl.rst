.. _auth-curl-request:

.. code:: console

	  $ curl https://identity.api.rackspacecloud.com/v2.0/tokens \
	         -X POST \
	         -d '{"auth":{"RAX-KSKEY:apiKeyCredentials":{"username":"$APIAccessUserName","apiKey":"$apiKey"}}}' \
	         -H "Content-type: application/json" | python -m json.tool
