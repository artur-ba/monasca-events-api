# Copyright 2017 FUJITSU LIMITED
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_log import log

from monasca_events_api import conf
from monasca_events_api import version

CONF = conf.CONF
LOG = log.getLogger(__name__)

_CONF_LOADED = False


def parse_args():
    """Parse configuration arguments.

    Note:
        This method ensures that configuration will be loaded
        only once within single python interpreter.

    """
    global _CONF_LOADED
    if _CONF_LOADED:
        LOG.debug('Configuration has been already loaded')
        return

    log.set_defaults()
    log.register_options(CONF)

    CONF(prog='events-api',
         project='monasca',
         version=version.version_str,
         description='RESTful API to collect events from cloud')

    log.setup(CONF,
              product_name='monasca-events-api',
              version=version.version_str)

    conf.register_opts()

    _CONF_LOADED = True
