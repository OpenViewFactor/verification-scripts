import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-discs")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/coaxial-discs")

def parDiscs001():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-001.xml"), meshes_directory)

def parDiscs002():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-002.xml"), meshes_directory)

def parDiscs003():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-003.xml"), meshes_directory)
  
def parDiscs004():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-004.xml"), meshes_directory)
  
def parDiscs005():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-005.xml"), meshes_directory)
  
def parDiscs006():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-006.xml"), meshes_directory)
  
def parDiscs007():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-007.xml"), meshes_directory)
  
def parDiscs008():
  runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-008.xml"), meshes_directory)
  
def runAllTests():
  passed_counter = 0
  if parDiscs001():
    passed_counter+=1
  if parDiscs002():
    passed_counter+=1
  if parDiscs003():
    passed_counter+=1
  if parDiscs004():
    passed_counter+=1
  if parDiscs005():
    passed_counter+=1
  if parDiscs006():
    passed_counter+=1
  if parDiscs007():
    passed_counter+=1
  if parDiscs008():
    passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------------- PARALLEL DISCS RESULTS ---------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Discs Results:\t\t {passed_counter} / 8 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()