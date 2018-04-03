#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the AddFloat class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.plugin import Plugin

class AddFloat(Plugin):

    # -------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Add Float"
        self.label = "Add Float"
        self.color = "200:200:25:150"
        self.in_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "name":"first_number",
                "label":"First Number"},
                {"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "name":"second_number",
                "label":"Second Number"}
                ]
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.float",
                "label":"Result",
                "name":"result"}
            ]
        self.group = "Arithmetics"

        self.codes[1] = """
// block_$id$ = Add Float
var block_$id$_arg1 = 0;
var block_$id$_arg2 = 0;
var $out_ports[result]$ = [];

var $in_ports[first_number]$ = function(value){
    block_$id$_arg1 = parseFloat(value);
    result = parseFloat(block_$id$_arg1) + parseFloat(block_$id$_arg2);
    for (var i = 0; i < $out_ports[result]$.length ; i++){
        $out_ports[result]$[i](result);
    }
    return true;
    };

var $in_ports[second_number]$ = function(value){
    block_$id$_arg2 = parseFloat(value);
    result = parseFloat(block_$id$_arg1) + parseFloat(block_$id$_arg2);
    for (var i = 0; i < $out_ports[result]$.length ; i++){
        $out_ports[result]$[i](result);
    }
    return true;
    };
"""
