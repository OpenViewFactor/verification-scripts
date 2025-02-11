import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-cylinders-10844els")
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

def cylinders008():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-008.xml"), meshes_directory)
  return passed
  
def cylinders009():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-009.xml"), meshes_directory)
  return passed
  
def cylinders010():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-010.xml"), meshes_directory)
  return passed
  
def cylinders011():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-011.xml"), meshes_directory)
  return passed
  
def cylinders012():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-012.xml"), meshes_directory)
  return passed
  
def cylinders013():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-013.xml"), meshes_directory)
  return passed
  
def cylinders014():
  passed = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-014.xml"), meshes_directory)
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
  # if cylinders005():
  #   passed_counter+=1
  # if cylinders006():
  #   passed_counter+=1
  # if cylinders007():
  #   passed_counter+=1
  if cylinders008():
    passed_counter+=1
  if cylinders009():
    passed_counter+=1
  if cylinders010():
    passed_counter+=1
  if cylinders011():
    passed_counter+=1
  # if cylinders012():
  #   passed_counter+=1
  # if cylinders013():
  #   passed_counter+=1
  # if cylinders014():
  #   passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------- CONCENTRIC CYLINDERS RESULTS ------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Concentric Cylinders Results:\t {passed_counter} / 14 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()