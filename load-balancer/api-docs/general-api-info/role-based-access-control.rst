.. _rbac:

=========================
Role Based Access Control
=========================

Role Based Access Control (RBAC) restricts access to the capabilities of
Rackspace API services, including the |apiservice| API, to authorized
users only. RBAC enables Rackspace customers to specify which account
users have access to which  |apiservice| capabilities,
based on roles defined by Rackspace.

The permissions to perform certain operations in |apiservice| (create, read,
update, delete) are assigned to specific roles, and these roles can be
assigned by the Rackspace account administrator.

.. _rbac-available:

Roles available for |product name|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table describes the roles that can be used to access the
|product name| API.

.. list-table:: **Product roles and capabilities**
   :widths: 20 50
   :header-rows: 1

   * - Role name
     - Role permissions
   * - bpi_lbs_read
     - This role provides Read permissions
       in |product name|, where access is granted.
   * - bpi_lbs_write
     - This role provides Create, Read, and Update permissions in
       |product name|, where access is granted.

.. _rbac-assigning:

Assigning roles to account users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Account administrators can assign roles to Rackspace Dedicated Hosting account
users by using the MyRackspace portal.

.. _MyRackspace portal: https://myrackspace.com
