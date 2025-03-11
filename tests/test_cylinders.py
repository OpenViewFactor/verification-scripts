import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-cylinders")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/coaxial-cylinders")
test_log_directory = os.path.join(current_file_directory, "../test_outputs/logs/coaxial-cylinders")

def cylinders001():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-001.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders002():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-002.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders003():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-003.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders004():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-004.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders005():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-005.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders006():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-006.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders007():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-007.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed

def cylinders008():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-008.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders009():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-009.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders010():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-010.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders011():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-011.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders012():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-012.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders013():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-013.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def cylinders014():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-014.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if cylinders001():
      dai_passed_counter+=1
    if cylinders002():
      dai_passed_counter+=1
    if cylinders003():
      dai_passed_counter+=1
    if cylinders004():
      dai_passed_counter+=1
    if cylinders005():
      dai_passed_counter+=1
    if cylinders006():
      dai_passed_counter+=1
    if cylinders007():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if cylinders008():
      sai_passed_counter+=1
    if cylinders009():
      sai_passed_counter+=1
    if cylinders010():
      sai_passed_counter+=1
    if cylinders011():
      sai_passed_counter+=1
    if cylinders012():
      sai_passed_counter+=1
    if cylinders013():
      sai_passed_counter+=1
    if cylinders014():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------- CONCENTRIC CYLINDERS RESULTS ------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Concentric Cylinders Results (DAI):\t {dai_passed_counter} / 7 PASSED")
  print(f"Concentric Cylinders Results (SAI):\t {sai_passed_counter} / 7 PASSED")

  return dai_passed_counter, sai_passed_counter

if __name__ == "__main__":
  runAllTests()