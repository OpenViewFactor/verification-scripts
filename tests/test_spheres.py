import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/concentric-spheres")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/concentric-spheres")
test_log_directory = os.path.join(current_file_directory, "../test_outputs/logs/concentric-spheres")

def spheres001():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-001.xml"), meshes_directory, test_log_directory)
  return passed

def spheres002():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-002.xml"), meshes_directory, test_log_directory)
  return passed

def spheres003():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-003.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres004():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-004.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres005():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-005.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres006():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-006.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres007():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-007.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres008():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-008.xml"), meshes_directory, test_log_directory)
  return passed

def spheres009():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-009.xml"), meshes_directory, test_log_directory)
  return passed

def spheres010():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-010.xml"), meshes_directory, test_log_directory)
  return passed

def spheres011():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-011.xml"), meshes_directory, test_log_directory)
  return passed
  
def spheres012():
  passed = runTest.runTest(os.path.join(xmls_directory, "concentric-spheres-012.xml"), meshes_directory, test_log_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if spheres001():
      dai_passed_counter+=1
    if spheres002():
      dai_passed_counter+=1
    if spheres003():
      dai_passed_counter+=1
    if spheres004():
      dai_passed_counter+=1
    if spheres005():
      dai_passed_counter+=1
    if spheres006():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if spheres007():
      sai_passed_counter+=1
    if spheres008():
      sai_passed_counter+=1
    if spheres009():
      sai_passed_counter+=1
    if spheres010():
      sai_passed_counter+=1
    if spheres011():
      sai_passed_counter+=1
    if spheres012():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| -------------- CONCENTRIC SPHERES RESULTS -------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Concentric Spheres Results (DAI):\t {dai_passed_counter} / 6 PASSED")
  print(f"Concentric Spheres Results (SAI):\t {sai_passed_counter} / 6 PASSED")

  return dai_passed_counter + sai_passed_counter
if __name__ == "__main__":
  runAllTests()