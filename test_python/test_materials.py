#!/usr/bin/python

import gwMaterials
from gwMaterials import *

gmm = gwMaterialManager()
gmm.parse_XML("../gwMaterials/StandardMaterials.xml")
gmm.output_elements()
