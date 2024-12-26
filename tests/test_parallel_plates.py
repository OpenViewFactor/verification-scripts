import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/aligned-parallel-rectangles")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/par-plates")

def parPlates001():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-001.xml"), meshes_directory)
  print(proc.stdout)

def parPlates002():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-002.xml"), meshes_directory)
  print(proc.stdout)

def parPlates003():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-003.xml"), meshes_directory)
  print(proc.stdout)

def parPlates004():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-004.xml"), meshes_directory)
  print(proc.stdout)

def parPlates005():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-005.xml"), meshes_directory)
  print(proc.stdout)

def parPlates006():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-006.xml"), meshes_directory)
  print(proc.stdout)

def parPlates007():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-007.xml"), meshes_directory)
  print(proc.stdout)

def parPlates008():
  proc = runTest.runTest(os.path.join(xmls_directory, "par-plate-008.xml"), meshes_directory)
  print(proc.stdout)



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