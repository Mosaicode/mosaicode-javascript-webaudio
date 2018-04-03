#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ADSR class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.plugin import Plugin

class ADSR(Plugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "ADSR"
        self.label = "ADSR"
        self.color = "50:150:250:150"

        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.sound",
                "label":"Sound",
                "name":"sound"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Event Play",
                "name":"play"}
                ]
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.sound",
                "label":"Sound",
                "name":"sound"}
            ]

        self.group = "Sound"

        self.properties = [
            {"name": "a",
             "label": "Attack",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 10000,
             "step": 1,
             "value": 5
             },
            {"name": "d",
             "label": "Delay",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 10000,
             "step": 1,
             "value": 2
             },
            {"name": "s",
             "label": "Sustain",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 10000,
             "step": 1,
             "value": 100
             },
            {"name": "r",
             "label": "Release",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 10000,
             "step": 1,
             "value": 50
             },
            {"name": "g",
             "label": "Gain",
             "type": MOSAICODE_FLOAT,
             "lower": 0,
             "upper": 10000,
             "step": 1,
             "value": 0.5
             }
        ]
        
        self.codes[0] = """
Envelope = function(context, a, d, s, r, g) {
this.node = context.createGain()
this.context = context;
this.node.gain.value = 0;
this.a = a / 1000.0;
this.d = d / 1000.0;
this.s = s / 1000.0;
this.r = r / 1000.0;
this.g = g;
}

Envelope.prototype.play = function(e) {
var time = this.context.currentTime;
// Zero
this.node.gain.linearRampToValueAtTime(0, time);
// Attack time
time += this.a;
this.node.gain.linearRampToValueAtTime(1, time);
// Decay time
time += this.d;
this.node.gain.linearRampToValueAtTime(0.5, time);
// Sustain time (do nothing)
time += this.s;
// Release time
time += this.r;
this.node.gain.linearRampToValueAtTime(0, time);
}
"""
        self.codes[1] = """
// block_$id$ = $label$
var block_$id$_obj = new Envelope(context, $prop[a]$, $prop[d]$, $prop[s]$, $prop[r]$, $prop[g]$);
var $out_ports[sound]$ = block_$id$_obj.node;
var $in_ports[sound]$ = block_$id$_obj.node;

var $in_ports[play]$ = function(value){
    block_$id$_obj.play();
};
"""

