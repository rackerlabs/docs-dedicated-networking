.. _index:

===============================================
Rackspace |product name| API |contract version|
===============================================

*Last updated:* |today|

.. warning::

   This API will be deprecated soon. We recommend that you use the new
   `LOAD BALANCER API 3.0 <https://docs.rackspace.com/docs/dedicated-load-balancer-v3/>`_
   that enables seamless access across Rackspace products and services. If you
   face any issues, contact your account administrator, or `Rackspace Support <https://support.rackspace.com/>`_.


The |product name| service enables developers to programmatically view and
manage their existing dedicated hardware load balancer resources such as
virtual IPs (vips), nodes and health checks. You cannot use the API to
provision dedicated hardware load balancers.

You can use the |apiservice| to manage the following load balancer models.

 - |F5Product|

     - |F5Version|

 - |ADXProduct|

     - |ADXVersion|

For details about using these load balancer models for hybrid hosting, see
:how-to:`Using dedicated load balancers with RackConnect v2.0\
<using-dedicated-load-balancers-with-rackconnect-v20>`.

.. warning::

   The |product name| provides direct access to the |F5Product| and
   |ADXProduct| device hardware. When you submit an API request
   to add, update, or remove configuration settings the changes are applied
   to the device as soon as the request completes successfully.
   Make sure you understand the impact of an API request before you submit it.


About this guide
~~~~~~~~~~~~~~~~

This guide is intended to assist software developers who want to manage
dedicated hardware load balancer resources by using the REST application
programming interface (API) for the Rackspace |product name| service.

To use the information provided here, you should have a general understanding of
the service and have access to an installation of it. You should
also be familiar with the following technologies:

- RESTful web services
- HTTP/1.1
- JSON serialization formats

Use the following links to jump direct to user and reference information for
using the |product name| service REST API:

* :ref:`Getting started<getting-started-intro>`
* :ref:`F5 Big-IP load balancer API Reference<f5-api-reference>`
* :ref:`Brocade ADX load balancer API Reference<adx-api-reference>`


.. toctree:: :hidden:
   :maxdepth: 3

   Load Balancers API 2.0 <self>
   getting-started/index
   general-api-info/index
   f5-api-reference/index
   adx-api-reference/index
   service-updates
   additional-resources
   copyright
   LOAD BALANCERS API 3.0 <https://docs.rackspace.com/docs/dedicated-load-balancer-v3/>
