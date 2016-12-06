.. _auth-response-example:

.. code::

	{
		"access": {
		 "serviceCatalog": [],
		 "user": {
			 "RAX-AUTH:defaultRegion": "",
			 "id": "<username:string>",
			 "name": "<username:string>",
			 "roles": [
				 {
					 "name": "bpi_lbs_write"
				 },
			 ],
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
