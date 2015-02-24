from lxml import etree
from collections import OrderedDict
###########################################################
###
class gwElement:
    def __init__(self, symbol="", z=0, a=0):
        self.symbol	= symbol
        self.z		= z
        self.a		= a

    def output(self):
        print "Element:", self.symbol, " z:", self.z, " a:", self.a
###
class gwMaterial:
    def __init__(self, name="", density=0.0):
        self.name	= name
        self.density	= density

    def output(self):
        print "Material:", self.name, " density:", self.density


###
class gwMaterialManager:
    def __init__(self):
        self.elements	= OrderedDict()
        self.materials	= OrderedDict()

    def add_material(self, material):
        self.materials[material.name] = material

    def add_element(self, element):
        self.elements[element.symbol] = element
        
    def output_materials(self):
        for name in self.materials.keys():
            m = self.materials[name]
            print "Material:", name, " density:", m.density
        
    def output_elements(self):
        for symbol in self.elements.keys():
            e = self.elements[symbol]
            print "Element:", symbol, " z:", e.z, " a:", e.a
        
    def parse_XML(self, xml_source="StandardMaterials.xml"):
        t = etree.parse(xml_source)
        r = t.getroot()

        for entry in r:
            if entry.tag == 'element':
                element = entry
                symbol = element.attrib['symbol']
                atom=element[0]
                e = gwElement(symbol, atom.attrib['zeff'], atom.attrib['aweight'])
                self.add_element(e)



        
#            print etree.tostring(element_content)
#    print etree.tostring(c)
#    x = c.getparent()
#    print x.tag
#print "-----------------------------------"
#for name, value in sorted(r.items()):
#    print('%s = %r' % (name, value))

#a = r.attrib
#print a
