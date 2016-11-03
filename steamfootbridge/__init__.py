# SteamFootBridge
# Copyright (c) 2016 Bryan DeGrendel

from . import config, download, execute, setup

import pkg_resources

__app_name__ = "SteamFootBridge"
__version__ = pkg_resources.get_distribution('steamfootbridge').version
