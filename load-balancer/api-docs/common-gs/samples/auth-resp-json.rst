.. _auth-response-example:

.. code::

	{
		"access": {
		 "serviceCatalog": [],
		 "user": {
			 "RAX-AUTH:defaultRegion": "",
			 "roles": [
				 {
					 "name": "<role_name:string>"
				 },
			 ],
			 "name": "<username:string>",
			 "id": "<username:string>"
		 },
		 "token": {
			 "expires": "2016-07-13T03:57:39.236Z",
			 "RAX-AUTH:authenticatedBy": [
				 "PASSWORD"
			 ],
			 "id": "<auth-token:string>"
		 }
		}
	}
