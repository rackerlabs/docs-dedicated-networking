.. _using-cloud-load-balancers:

==========================================
Create and manage dedicated load balancers
==========================================

TO DO:  Update headings to reflect common dedicated LB use cases


You can use the examples in the following sections to create and manage load
balancers by using |apiservice| operations.

.. contents::
   :local:
   :depth: 1


Before running the examples, review the dedicated load balancer
:ref:`concepts<concepts>`.


.. note::
     These examples use the ``$ENDPOINT``, ``$AUTH_TOKEN``, and
     ``$TENANT_ID`` environment variables to specify the API endpoint,
     authentication token, and project ID values for accessing the service.
     Make sure you :ref:`configure these
     variables<configure-environment-variables>` before running the code
     samples.


.. include:: examples/create-cloud-servers-to-lb.rst
.. include:: examples/create-load-balancer.rst
.. include:: examples/list-load-balancer-details.rst
.. include:: examples/add-node.rst
.. include:: examples/update-load-balancer-attributes.rst
