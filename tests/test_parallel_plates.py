import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/aligned-parallel-rectangles")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/par-plates")

def parPlates001():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-001.xml"), meshes_directory)
  return passed
  
def parPlates002():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-002.xml"), meshes_directory)
  return passed

def parPlates003():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-003.xml"), meshes_directory)
  return passed
  
def parPlates004():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-004.xml"), meshes_directory)
  return passed
  
def parPlates005():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-005.xml"), meshes_directory)
  return passed
  
def parPlates006():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-006.xml"), meshes_directory)
  return passed
  
def parPlates007():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-007.xml"), meshes_directory)
  return passed
  
def parPlates008():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-008.xml"), meshes_directory)
  return passed
  
def runAllTests():
  passed_counter = 0
  if parPlates001():
    passed_counter+=1
  if parPlates002():
    passed_counter+=1
  if parPlates003():
    passed_counter+=1
  if parPlates004():
    passed_counter+=1
  if parPlates005():
    passed_counter+=1
  if parPlates006():
    passed_counter+=1
  if parPlates007():
    passed_counter+=1
  if parPlates008():
    passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| --------------- PARALLEL PLATES RESULTS ---------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Plates Results:\t {passed_counter} / 8 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()