import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/perpendicular-rectangles")
non_sharing_xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/per-plates")

def perPlates001():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-001.xml"), meshes_directory)
  return passed
  
def perPlates002():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-002.xml"), meshes_directory)
  return passed
  
def perPlates003():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-003.xml"), meshes_directory)
  return passed
  
def perPlates004():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-004.xml"), meshes_directory)
  return passed
  
def perPlates005():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-005.xml"), meshes_directory)
  return passed
  
def perPlates006():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-006.xml"), meshes_directory)
  return passed
  
def perPlates007():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-007.xml"), meshes_directory)
  return passed
  
def perPlates008():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-008.xml"), meshes_directory)
  return passed
  
def runAllTests():
  passed_counter = 0
  if perPlates001():
    passed_counter+=1
  if perPlates002():
    passed_counter+=1
  if perPlates003():
    passed_counter+=1
  if perPlates004():
    passed_counter+=1
  if perPlates005():
    passed_counter+=1
  if perPlates006():
    passed_counter+=1
  if perPlates007():
    passed_counter+=1
  if perPlates008():
    passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------- PERPENDICULAR PLATES (NONSHARING) RESULTS ------ ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Perpendicular Plates Results:\t {passed_counter} / 16 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()