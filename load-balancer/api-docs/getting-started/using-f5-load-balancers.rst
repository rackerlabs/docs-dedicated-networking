.. _using-f5-load-balancers:

======================
Create and manage |F5|
======================

You can use the examples in the following sections to create and manage load
balancers by using |apiservice| operations.

.. contents::
   :local:
   :depth: 1

Before running the examples, review the dedicated load balancer
:ref:`concepts<concepts>`.


.. note::
     These examples use the ``$TOKEN``, and
     ``$TENANT_ID`` environment variables to specify the
     authentication token and tenant ID values for accessing the service.
     Make sure you :ref:`configure these
     variables<configure-environment-variables>` before running the code
     samples.


.. _baseurlf5:

Base URL
~~~~~~~~

Submit API requests for |F5| to the following URL:

``https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_ID}/f5loadbalancers/{device_id}``

To make it easier to run the cURL requests, export this URL to
an environment variable. Replace the tenant and device ID with the values for
your account.

.. code:: console

   export BASE_URL="https://lb.dedicated.api.rackspacecloud.com/2.0/$tenant_id/f5loadbalancers/$device_id"

.. include:: examples/retrieve-lb-info.rst
.. include:: examples/manage-nodes.rst
.. include:: examples/manage-pools.rst
.. include:: examples/virtuals.rst
.. include:: examples/manage-monitors.rst
.. include:: examples/retrieve-event-data.rst
