.. _service-access-endpoints:

========================
Service access
========================

The |apiservice| is a regionalized service. The user of the service is therefore 
responsible for appropriate replication, caching, and overall maintenance of 
|product name| across regional boundaries to other Cloud Servers.

The endpoints to use for your |product name| API calls are summarized in the following table.

To help you decide which regionalized endpoint to use, read `About regions`_ about special 
considerations for choosing a data center.

**Regionalized service endpoints**

+-------------------------+--------------------------------------------------------------+
|         Region          |                          Endpoint                            |
+=========================+==============================================================+
| Chicago (ORD)           | \ |ORD|                                                      |
+-------------------------+--------------------------------------------------------------+
| Dallas/Ft. Worth (DFW)  | \ |DFW|                                                      |
+-------------------------+--------------------------------------------------------------+
| Northern Virginia (IAD) | \|IAD|                                                       |
+-------------------------+--------------------------------------------------------------+
| London (LON)            | \|LON|                                                       |
+-------------------------+--------------------------------------------------------------+

Replace the ``yourAccountID`` placeholder with your actual account number, which is returned as 
part of the authentication service response, after the final **/** in the ``publicURL`` field.

.. _About regions: http://www.rackspace.com/knowledge_center/article/about-regions