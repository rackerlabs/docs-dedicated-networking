.. _service-access-endpoints:

==============
Service access
==============

Use the following global endpoint to submit requests to the |apiservice|.

``https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_id}``

Use the following URIs to submit requests to manage load balancers of a
specific type:

|F5|
~~~~

    ``https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_id}/f5loadbalancers/``

|ADX|
~~~~~

    ``https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_id}/loadbalancers/``

.. note::

    You must :ref:`authenticate <authenticate-to-identity-service>` before you
    can submit requests.
