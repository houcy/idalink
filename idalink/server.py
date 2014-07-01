#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2013- Yan Shoshitaishvili aka. zardus
#                     Ruoyu Wang aka. fish
#                     Andrew Dutcher aka. rhelmot
#                     Kevin Borgolte aka. cao
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

# idc is just within IDA, so make pylint stop complaining
import idc      # pylint: disable=F0401

# pylint: disable=W0403
# :note: Those should be relative imports, but IDA doesn't like them.
from rpyc.core import SlaveService
from rpyc.utils.server import OneShotServer

if __name__ == "__main__":
    print "Received arguments: {}".format(idc.ARGV)

    if idc.ARGV[1:]:
        port = int(idc.ARGV[1])
    else:
        port = 18861

    idc.Wait()
    OneShotServer(SlaveService, port=port).start()
    idc.Exit(0)
