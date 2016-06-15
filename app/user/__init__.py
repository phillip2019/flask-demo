# -*- coding: utf-8 -*-

from flask import Blueprint
from app.common.conf import conf

module_name = __name__.spit('.')[-1]
url_prefix = ''.join([conf.URL_PREFIX, '/', str(conf.API_VERSION), '/', module_name])
mod = Blueprint(module_name, __name__, url_prefix=url_prefix)
