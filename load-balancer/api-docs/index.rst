.. _index:

=====================================
Dedicated Load Balancers API
=====================================

*Last updated:* |today|

The |apiservice| service enables software developers to programmatically view
and configure their existing dedicated hardware load balancer resources such as
VIPs, nodes and health checks. The API does NOT allow programmers to provision
dedicated hardware load balancers.

This guide is intended to assist software developers who want to manage
dedicated hardware load balancer resources by using the REST application
programming interface (API) for the Rackspace |product name| service.

To use the information provided here, you should have a general understanding of
the |product name| and have access to an installation of the service. You should
also be familiar with the following technologies:

- RESTful web services
- HTTP/1.1
- JSON and/or XML serialization formats

For additional information about the API, see the following topics:

.. contents::
   :local:
   :depth: 1

.. _dedicated-load-balancers-early-access-program:

Early Access Program
~~~~~~~~~~~~~~~~~~~~

The |product name| is now available to customers through an
Early Access program. As the service progresses towards General
Availability, additional features and event notifications will be added,
and it is possible that existing implementations and formats might
change.

The Early Access program is an opportunity for customers to work
in partnership with Rackspace to ensure that the implemented features
align with business needs and can be used with maximum efficiency.
Existing Rackspace Dedicated customers with Brocade Load Balancers are eligible
to participate in the Dedicated Load Balancer API EA Program.

To obtain access to the |product name| API or to provide
feedback, please contact your account team or Product manager,
|product support email|.
The |product name| Early Access program is provided to
customers subject to the Test Terms located at
https://www.rackspace.com/information/legal/testterms.

.. _pricing-service-level:

Pricing and terms of service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|product name| is included for customers who have Load Balancing as part of
their Hosting Configuration. There is no additional `cost for API usage` beyond
the hosting services charged for the hardware device.

There is no additional service level agreement (SLA) for this service during the
Early Access period.

The Early Access terms of service are part of the `Rackspace Test Terms`.
Periodically review these terms because they can be updated any time.

.. _cost for API usage: http://www.rackspace.com/cloud/big-data/pricing/
.. _Rackspace Cloud SLA: http://www.rackspace.com/information/legal/cloud/sla
.. _Rackspace Cloud Terms of Service: http://www.rackspace.com/information/legal/cloud/tos

.. _api-contract-changes:

API contract changes
~~~~~~~~~~~~~~~~~~~~

The API contract is not locked and might change. If the contract changes,
Rackspace will notify customers in release notes.

Service updates
~~~~~~~~~~~~~~~

Rackspace provides service updates to introduce backward-compatible updates and
modifications to |apiservice| |contract version|. These changes are not intended to break
any existing code that relies on the API (SDK, web applications, scripts, and so on).
However, you might want to update or extend your code to use new features and enhancements.

To learn about updates and changes included in this and other releases, see the
:ref:`Release Notes <release-notes>`.

.. toctree:: :hidden:
   :maxdepth: 3

   Load Balancers API 2.0 <self>
   getting-started/index
   api-reference/index
   additional-resources
   copyright
