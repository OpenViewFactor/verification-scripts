import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-cylinders-10451els")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/coaxial-cylinders")

def cylinders001():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-001.xml"), meshes_directory)
  return passed
  
def cylinders002():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-002.xml"), meshes_directory)
  return passed
  
def cylinders003():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-003.xml"), meshes_directory)
  return passed
  
def cylinders004():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-004.xml"), meshes_directory)
  return passed
  
def cylinders005():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-005.xml"), meshes_directory)
  return passed
  
def cylinders006():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-006.xml"), meshes_directory)
  return passed
  
def cylinders007():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-007.xml"), meshes_directory)
  return passed
  
def runAllTests():
  passed_counter = 0
  if cylinders001():
    passed_counter+=1
  if cylinders002():
    passed_counter+=1
  if cylinders003():
    passed_counter+=1
  if cylinders004():
    passed_counter+=1
  if cylinders005():
    passed_counter+=1
  if cylinders006():
    passed_counter+=1
  if cylinders007():
    passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------- CONCENTRIC CYLINDERS RESULTS ------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Concentric Cylinders Results:\t {passed_counter} / 7 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()