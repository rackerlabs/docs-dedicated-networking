.. _faults:

======
Faults
======

When an error occurs, the |apiservice| returns a fault object that contains 
an HTTP error response code that denotes the type of error. In the body of the response, 
the system will return additional information about the fault.

The following table lists possible fault types with their associated error codes and 
descriptions.

+--------------------------+------------+-----------------------------------------+
|     Fault type           | Associated | Description                             |
|                          | error code |                                         |
+==========================+============+=========================================+
| Bad Request              | 400        | The user-provided request contained an  |
|                          |            | error.                                  |
+--------------------------+------------+-----------------------------------------+
| Unauthorized             | 401        | The supplied token is not authorized to |
|                          |            | access the resources. The token is      |
|                          |            | either expired or invalid.              |
+--------------------------+------------+-----------------------------------------+
| Forbidden                | 403        | Access to the requested resource was    |
|                          |            | denied.                                 |
+--------------------------+------------+-----------------------------------------+
| Not Found                | 404        | The back-end services did not find      |
|                          |            | anything matching the request URI.      |
+--------------------------+------------+-----------------------------------------+
| Conflict                 | 409        | The requested resource cannot currently |
|                          |            | be operated on.                         |
+--------------------------+------------+-----------------------------------------+
| Request Entity Too Large | 413        | The resource quota was exceeded.        |
+--------------------------+------------+-----------------------------------------+
| Lava Fault               | 500        | An unknown exception occurred.          |
+--------------------------+------------+-----------------------------------------+
| Service Unavailable      | 503        | The service is currently unavailable.   |
+--------------------------+------------+-----------------------------------------+
