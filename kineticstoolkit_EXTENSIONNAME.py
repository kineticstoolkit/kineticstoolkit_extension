#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 AUTHOR_NAME

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# =======================================================================
# PLEASE CHANGE AUTHOR_NAME AND AUTHOR_EMAIL FOR YOUR AUTHOR INFORMATION.
# =======================================================================

"""
Provide a short description of your extension.
"""

__author__ = "AUTHOR_NAME"
__copyright__ = "Copyright (C) 2022 AUTHOR_NAME"
__email__ = "AUTHOR_EMAIL"
__license__ = "Apache 2.0"


import kineticstoolkit


# Print something to know that the extension is loaded. Delete this before the true release.
print("Nice, I was imported. PLEASE DELETE THIS TEST PRINT LINE.")

def some_function():
    """
    This function will be available as ktk.ext.EXTENSIONNAME.some_function().
    
    You can delete it.
    """
    print("Called some_function().")
    
def some_other_function():
    """This function will be available as ktk.ext.EXTENSIONNAME.some_other_function(), etc."""
    pass

