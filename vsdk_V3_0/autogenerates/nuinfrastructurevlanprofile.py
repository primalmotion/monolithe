# -*- coding: utf-8 -*-
"""

NUInfrastructureVlanProfile
This file has been autogenerated by Swagger  and should not be modified.

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from bambou import NURESTObject



class NUInfrastructureVlanProfile(NURESTObject):
    """ Represents a InfrastructureVlanProfile object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUInfrastructureVlanProfile instance """

        super(NUInfrastructureVlanProfile, self).__init__()

        # Read/Write Attributes
        self.qos_profile = None  #  QoS Profile :  Name of the QoS associated with this VLAN ID. - int
        self.vlan = None  #  Vlan - int
        self.description = None  #  A description of the Profile instance created. - int
        self.enterprise_id = None  #  Name of the enterprise/organisation associated with this Profile instance.  This is a read only attribute - int
        self.name = None  #  Name of the Infrastructure Profile - int
        
        self.expose_attribute(local_name=u"qos_profile", remote_name=u"qosProfile", attribute_type=int)
        self.expose_attribute(local_name=u"vlan", remote_name=u"vlan", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        
        # Fetchers
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"infrastructurevlanprofile"

