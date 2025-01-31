import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/algnd-par-rect-10034els")
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

def parPlates009():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-009.xml"), meshes_directory)
  return passed

def parPlates010():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-010.xml"), meshes_directory)
  return passed

def parPlates011():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-011.xml"), meshes_directory)
  return passed

def parPlates012():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-012.xml"), meshes_directory)
  return passed

def parPlates013():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-013.xml"), meshes_directory)
  return passed

def parPlates014():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-014.xml"), meshes_directory)
  return passed

def parPlates015():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-015.xml"), meshes_directory)
  return passed

def parPlates016():
  passed = runTest.runTest(os.path.join(xmls_directory, "par-plate-016.xml"), meshes_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if parPlates001():
      dai_passed_counter+=1
    if parPlates002():
      dai_passed_counter+=1
    if parPlates003():
      dai_passed_counter+=1
    if parPlates004():
      dai_passed_counter+=1
    if parPlates005():
      dai_passed_counter+=1
    if parPlates006():
      dai_passed_counter+=1
    if parPlates007():
      dai_passed_counter+=1
    if parPlates008():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if parPlates009():
      sai_passed_counter+=1
    if parPlates010():
      sai_passed_counter+=1
    if parPlates011():
      sai_passed_counter+=1
    if parPlates012():
      sai_passed_counter+=1
    if parPlates013():
      sai_passed_counter+=1
    if parPlates014():
      sai_passed_counter+=1
    if parPlates015():
      sai_passed_counter+=1
    if parPlates016():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------------- PARALLEL PLATES RESULTS --------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Plates Results (DAI):\t {dai_passed_counter} / 8 PASSED")
  print(f"Parallel Plates Results (SAI):\t {sai_passed_counter} / 8 PASSED")

  return dai_passed_counter + sai_passed_counter

if __name__ == "__main__":
  runAllTests()