.. _ general-api-info:

=======================
General API Information
=======================

TEMPLATE NOTE:  Adapt the intro and included topics in the General API Information as 
needed for your API service.

The |product name| API is implemented using a RESTful web service interface. 
|product name| shares a common token-based authentication system with other products in 
the Rackspace Cloud suite. This system enables seamless access between Rackspace products a
nd services.

.. note::
    All requests to authenticate against and operate the service are performed using 
    SSL over HTTP (HTTPS) on TCP port 443.
    
.. toctree:: :hidden:
   :maxdepth: 3
    
   authentication
   service-access-endpoints
   request-and-response-types
   date-time-format
   faults
   limits
   pagination
   role-based-access-control
   data-node-instances