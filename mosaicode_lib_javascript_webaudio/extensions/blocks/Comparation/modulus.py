#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Modulus class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Modulus(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "Modulus Operation (%)"
        self.label = "Modulus"
        self.color = "50:50:50:150"
        self.group = "Comparation"

        self.out_types = ["mosaicode_lib_javascript_webaudio.extensions.ports.string",
                          "mosaicode_lib_javascript_webaudio.extensions.ports.string"]

        self.ports = [
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.string",
             "conn_type": "Output",
             "name": "true_value",
             "label": "True Value"},
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.string",
             "conn_type": "Output",
             "name": "false_value",
             "label": "False Falue"},
            {"type":"mosaicode_lib_javascript_webaudio.extensions.ports.float",
             "name": "dividend",
             "label":"Dividend",
             "conn_type":"Input"},
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
             "name": "divisor",
             "label": "Divisor",
             "conn_type": "Input"},
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
             "name": "rest",
             "label": "Rest",
             "conn_type": "Input"},
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.string",
             "name": "default_value_if_true",
             "label": "Default Value If True",
             "conn_type": "Input"},
            {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.string",
             "name": "default_value_if_false",
             "label": "Default Value If False",
             "conn_type": "Input"},
        ]

        self.codes["onload"] = """
"""

        self.codes["declaration"] = """
var dividend$id$ = 0.0;
var divisor$id$ = 1.0;
var rest$id$ = 0.0;
var default_value_if_true$id$ = "OK";
var default_value_if_false$id$ = "NOK";
        
var $port[true_value]$ = [];
var $port[false_value]$ = [];

function modulus$id$() {
    if (divisor$id$ === 0.0) {
        divisor$id$ = 1.0;
    }
    
    if (dividend$id$ % divisor$id$ === rest$id$) {
        for (var i = 0; i < $port[true_value]$.length ; i++){
            $port[true_value]$[i]('' + default_value_if_true$id$ + '');
        }
        for (var i = 0; i < $port[false_value]$.length ; i++){
            $port[false_value]$[i]('');
        }
    } else { 
        for (var i = 0; i < $port[true_value]$.length ; i++){
            $port[true_value]$[i]('');
        }      
        for (var i = 0; i < $port[false_value]$.length ; i++){
            $port[false_value]$[i]('' + default_value_if_false$id$ + '');
        }       
    }
}

var $port[dividend]$ = function(value){
    dividend$id$ = Math.round(value);
    modulus$id$();
    return true;
};

var $port[divisor]$ = function(value){
    divisor$id$ = Math.round(value);
    modulus$id$();
    return true;
};

var $port[rest]$ = function(value){
    rest$id$ = Math.round(value);
    modulus$id$();
    return true;
};

var $port[default_value_if_true]$ = function(value){
    default_value_if_true$id$  = value;
    modulus$id$();
    return true;
};

var $port[default_value_if_false]$ = function(value){
    default_value_if_false$id$  = value;
    modulus$id$();
    return true;
};
"""

        self.codes["execution"] = """
"""