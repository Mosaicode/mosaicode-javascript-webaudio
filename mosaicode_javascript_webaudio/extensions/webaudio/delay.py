#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Delay class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.plugin import Plugin

class Delay(Plugin):

    # --------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Delay"
        self.label = "Delay"
        self.color = "150:150:250:150"
        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.sound",
                "label":"Sound",
                "name":"sound"}
                ]
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.sound",
                "label":"Sound",
                "name":"sound"}
            ]

        self.group = "Sound"

        self.properties = [{"name": "time",
                            "label": "Time",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            }
                           ]

        self.codes[1] = """
// block_$id$ = Delay
var block_$id$ = context.createDelay();
var $out_ports[sound]$ = null;
var $in_ports[sound]$ = null;
"""

        self.codes[2] = "$in_ports[sound]$ = block_$id$;\n" + \
            "var block_$id$.delayTime.value = $prop[time]$\n;" + \
            "$out_ports[sound]$ = block_$id$;\n"

