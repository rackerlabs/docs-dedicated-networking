.. _limits:

======
Limits
======

The |product name| provides direct access to the |F5Product| and
|ADXProduct| device hardware. When you submit an API request
to add, update, or remove configuration settings the changes are applied
to the device as soon as the request completes successfully.

The number of requests that can be processed is determined by the number
of concurrent connections a device can accept. This value is configurable in
the device settings.

If you send to many requests at the same time, the operations fail because
the device is overloaded. You can resolve the issue by waiting for an
open connection and submitting the request again.  
