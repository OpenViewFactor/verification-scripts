import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '../submodules/pyOpenViewFactor'))
import RunOVF

sys.path.append(os.path.join(current_file_directory, '..'))
import parseXML

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/aligned-parallel-rectangles")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/par-plates")

def parPlates001():
  xml_file = os.path.join(xmls_directory, "par-plate-001.xml")
  RunOVF.RunOVF(HELP_TOGGLE = True)
  parseXML.parseXML(xml_file)

def parPlates002():
  xml_file = os.path.join(xmls_directory, "par-plate-002.xml") 

def parPlates003():
  xml_file = os.path.join(xmls_directory, "par-plate-003.xml")

def parPlates004():
  xml_file = os.path.join(xmls_directory, "par-plate-004.xml")

def parPlates005():
  xml_file = os.path.join(xmls_directory, "par-plate-005.xml")

def parPlates006():
  xml_file = os.path.join(xmls_directory, "par-plate-006.xml")

def parPlates007():
  xml_file = os.path.join(xmls_directory, "par-plate-007.xml")

def parPlates008():
  xml_file = os.path.join(xmls_directory, "par-plate-008.xml")




def runAllTests():
  parPlates001()
  parPlates002()
  parPlates003()
  parPlates004()
  parPlates005()
  parPlates006()
  parPlates007()
  parPlates008()

if __name__ == "__main__":
  runAllTests()