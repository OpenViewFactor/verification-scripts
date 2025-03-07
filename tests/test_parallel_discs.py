import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-discs")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/coaxial-discs")

def parDiscs001():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-001.xml"), meshes_directory)
  return passed

def parDiscs002():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-002.xml"), meshes_directory)
  return passed

def parDiscs003():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-003.xml"), meshes_directory)
  return passed
  
def parDiscs004():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-004.xml"), meshes_directory)
  return passed
  
def parDiscs005():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-005.xml"), meshes_directory)
  return passed
  
def parDiscs006():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-006.xml"), meshes_directory)
  return passed
  
def parDiscs007():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-007.xml"), meshes_directory)
  return passed
  
def parDiscs008():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-008.xml"), meshes_directory)
  return passed

def parDiscs009():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-009.xml"), meshes_directory)
  return passed

def parDiscs010():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-010.xml"), meshes_directory)
  return passed

def parDiscs011():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-011.xml"), meshes_directory)
  return passed
  
def parDiscs012():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-012.xml"), meshes_directory)
  return passed
  
def parDiscs013():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-013.xml"), meshes_directory)
  return passed
  
def parDiscs014():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-014.xml"), meshes_directory)
  return passed
  
def parDiscs015():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-015.xml"), meshes_directory)
  return passed
  
def parDiscs016():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-016.xml"), meshes_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if parDiscs001():
      dai_passed_counter+=1
    if parDiscs002():
      dai_passed_counter+=1
    if parDiscs003():
      dai_passed_counter+=1
    if parDiscs004():
      dai_passed_counter+=1
    if parDiscs005():
      dai_passed_counter+=1
    if parDiscs006():
      dai_passed_counter+=1
    if parDiscs007():
      dai_passed_counter+=1
    if parDiscs008():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if parDiscs009():
      sai_passed_counter+=1
    if parDiscs010():
      sai_passed_counter+=1
    if parDiscs011():
      sai_passed_counter+=1
    if parDiscs012():
      sai_passed_counter+=1
    if parDiscs013():
      sai_passed_counter+=1
    if parDiscs014():
      sai_passed_counter+=1
    if parDiscs015():
      sai_passed_counter+=1
    if parDiscs016():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------------- PARALLEL DISCS RESULTS ---------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Discs Results (DAI):\t {dai_passed_counter} / 8 PASSED")
  print(f"Parallel Discs Results (SAI):\t {sai_passed_counter} / 8 PASSED")

  return dai_passed_counter + sai_passed_counter
if __name__ == "__main__":
  runAllTests()