import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/perpendicular-plates")
non_sharing_xmls_directory = os.path.join(current_file_directory, "../test-xmls/per-plates")
test_log_directory = os.path.join(current_file_directory, "../test_outputs/logs/per-plates")

def perPlatesNonsharing001():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-001.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing002():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-002.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing003():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-003.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing004():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-004.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing005():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-005.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing006():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-006.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing007():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-007.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing008():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-008.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed

def perPlatesNonsharing009():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-009.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing010():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-010.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing011():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-011.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing012():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-012.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing013():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-013.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing014():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-014.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing015():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-015.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def perPlatesNonsharing016():
  passed = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-016.xml"), test_log_directory = test_log_directory, all_mesh_dir=meshes_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if perPlatesNonsharing001():
      dai_passed_counter+=1
    if perPlatesNonsharing002():
      dai_passed_counter+=1
    if perPlatesNonsharing003():
      dai_passed_counter+=1
    if perPlatesNonsharing004():
      dai_passed_counter+=1
    if perPlatesNonsharing005():
      dai_passed_counter+=1
    if perPlatesNonsharing006():
      dai_passed_counter+=1
    if perPlatesNonsharing007():
      dai_passed_counter+=1
    if perPlatesNonsharing008():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if perPlatesNonsharing009():
      sai_passed_counter+=1
    if perPlatesNonsharing010():
      sai_passed_counter+=1
    if perPlatesNonsharing011():
      sai_passed_counter+=1
    if perPlatesNonsharing012():
      sai_passed_counter+=1
    if perPlatesNonsharing013():
      sai_passed_counter+=1
    if perPlatesNonsharing014():
      sai_passed_counter+=1
    if perPlatesNonsharing015():
      sai_passed_counter+=1
    if perPlatesNonsharing016():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| -------- PERPENDICULAR PLATES (NONSHARING) RESULTS -------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Perpendicular Plates (Nonsharing) Results (DAI):\t {dai_passed_counter} / 8 PASSED")
  print(f"Perpendicular Plates (Nonsharing) Results (SAI):\t {sai_passed_counter} / 8 PASSED")

  return dai_passed_counter, sai_passed_counter

if __name__ == "__main__":
  runAllTests()