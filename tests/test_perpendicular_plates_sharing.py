import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/prp-rect-approx10000els")
sharing_xmls_directory = os.path.join(current_file_directory, '../test-xmls/per-plates')

def perPlatesSharing001():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-001.xml"), meshes_directory)
  return passed
  
def perPlatesSharing002():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-002.xml"), meshes_directory)
  return passed
  
def perPlatesSharing003():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-003.xml"), meshes_directory)
  return passed
  
def perPlatesSharing004():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-004.xml"), meshes_directory)
  return passed
  
def perPlatesSharing005():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-005.xml"), meshes_directory)
  return passed
  
def perPlatesSharing006():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-006.xml"), meshes_directory)
  return passed
  
def perPlatesSharing007():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-007.xml"), meshes_directory)
  return passed
  
def perPlatesSharing008():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-008.xml"), meshes_directory)
  return passed
  
def perPlatesSharing009():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-009.xml"), meshes_directory)
  return passed
  
def perPlatesSharing010():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-010.xml"), meshes_directory)
  return passed
  
def perPlatesSharing011():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-011.xml"), meshes_directory)
  return passed
  
def perPlatesSharing012():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-012.xml"), meshes_directory)
  return passed
  
def perPlatesSharing013():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-013.xml"), meshes_directory)
  return passed
  
def perPlatesSharing014():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-014.xml"), meshes_directory)
  return passed
  
def perPlatesSharing015():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-015.xml"), meshes_directory)
  return passed
  
def perPlatesSharing016():
  passed = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-016.xml"), meshes_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if perPlatesSharing001():
      dai_passed_counter+=1
    if perPlatesSharing002():
      dai_passed_counter+=1
    if perPlatesSharing003():
      dai_passed_counter+=1
    if perPlatesSharing004():
      dai_passed_counter+=1
    if perPlatesSharing005():
      dai_passed_counter+=1
    if perPlatesSharing006():
      dai_passed_counter+=1
    if perPlatesSharing007():
      dai_passed_counter+=1
    if perPlatesSharing008():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if perPlatesSharing009():
      sai_passed_counter+=1
    if perPlatesSharing010():
      sai_passed_counter+=1
    if perPlatesSharing011():
      sai_passed_counter+=1
    if perPlatesSharing012():
      sai_passed_counter+=1
    if perPlatesSharing013():
      sai_passed_counter+=1
    if perPlatesSharing014():
      sai_passed_counter+=1
    if perPlatesSharing015():
      sai_passed_counter+=1
    if perPlatesSharing016():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| -------- PERPENDICULAR PLATES (SHARING) RESULTS -------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Perpendicular Plates (Sharing) Results (DAI):\t {dai_passed_counter} / 8 PASSED")
  print(f"Perpendicular Plates (Sharing) Results (SAI):\t {sai_passed_counter} / 8 PASSED")

  return dai_passed_counter + sai_passed_counter

if __name__ == "__main__":
  runAllTests()