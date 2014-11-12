# -*- coding: utf-8 -*-
"""

NUAutoDiscGateway
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

from ..fetchers import NUWANServicesFetcher
from ..fetchers import NUPortsFetcher
from ..fetchers import NUEventLogsFetcher


class NUAutoDiscGateway(NURESTObject):
    """ Represents a AutoDiscGateway object in Nuage VSD solution
        IMPORTANT: Do not override this object.
    """

    def __init__(self, **kwargs):
        """ Initialize a NUAutoDiscGateway instance """

        super(NUAutoDiscGateway, self).__init__()

        # Read/Write Attributes
        self.controllers = None  #  Controllers to which this gateway instance is associated with. - int
        self.gateway_id = None  #  The Gateway associated with this  Auto Discovered Gateway  . This is a read only attribute - int
        self.related_ports = None  #  List of ports to which this auto discovered gateway is related to. - int
        self.system_id = None  #  Identifier of the Gateway - int
        self.description = None  #  A description of the Gateway - int
        self.infrastructure_profile_id = None  #  The ID of the infrastructure gateway profile this instance of a Gateway is associated with. - int
        self.name = None  #  Name of the Gateway - int
        self.personality = None  #  Personality of the Gateway - VSG,VRSG,NSG,NONE,OTHER, cannot be changed after creation. - int
        
        self.expose_attribute(local_name=u"controllers", remote_name=u"controllers", attribute_type=int)
        self.expose_attribute(local_name=u"gateway_id", remote_name=u"gatewayID", attribute_type=int)
        self.expose_attribute(local_name=u"related_ports", remote_name=u"relatedPorts", attribute_type=int)
        self.expose_attribute(local_name=u"system_id", remote_name=u"systemID", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=int)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=int)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=int)
        
        # Fetchers
        self.wan_services = []
        self.wan_services_fetcher = NUWANServicesFetcher.fetcher_with_object(nurest_object=self, local_name=u"wan_services")
        self.ports = []
        self.ports_fetcher = NUPortsFetcher.fetcher_with_object(nurest_object=self, local_name=u"ports")
        self.event_logs = []
        self.event_logs_fetcher = NUEventLogsFetcher.fetcher_with_object(nurest_object=self, local_name=u"event_logs")
        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)



    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"autodiscgateway"

