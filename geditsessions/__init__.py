# -*- coding: utf-8 -*-
#  Simple save current editing session
# 
#  Copyright (C) 2008 Andrew Gryaznov
#  email any feedback or suggestions to: realgrandrew@gmail.com
#   
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#   
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#   
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330,
#  Boston, MA 02111-1307, USA.

import gedit
from session import SessionPluginInstance

class SessionPlugin(gedit.Plugin):
    DATA_TAG = "SessionPluginInstance"
    
    def __init__(self):
        gedit.Plugin.__init__(self)

    def _get_instance(self, window):
        return window.get_data(self.DATA_TAG)
    
    def _set_instance(self, window, instance):
        window.set_data(self.DATA_TAG, instance)
    
    def activate(self, window):
        self._set_instance(window, SessionPluginInstance(self, window))
        self._get_instance(window).on_restore()
    
    def deactivate(self, window):
        self._get_instance(window).stop()
        self._set_instance(window, None)
        
    def update_ui(self, window):
        self._get_instance(window).update()
