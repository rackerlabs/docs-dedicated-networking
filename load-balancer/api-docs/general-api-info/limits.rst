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

If you send too many requests, the device is overloaded and the API operations
fail with an error. You can resolve the problem by waiting for an
open connection and submitting the request again.
