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
| Not Found                | 404        | The back-end services did not find      |
|                          |            | anything matching the request URI.      |
+--------------------------+------------+-----------------------------------------+
| Conflict                 | 409        | The requested resource cannot currently |
|                          |            | be operated on.                         |
+--------------------------+------------+-----------------------------------------+
| Not implemented          | 501        | Retrieving a specific monitor is not    |
|                          |            | implemented.                            |
+--------------------------+------------+-----------------------------------------+
| Not extended             | 510        | An unexpected error occurred            |
+--------------------------+------------+-----------------------------------------+
