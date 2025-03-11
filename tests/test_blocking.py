import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

cylinder_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-cylinders")
sphere_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/concentric-spheres")
plates_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/parallel-plates")

xmls_directory = os.path.join(current_file_directory, "../test-xmls/blocking")
test_log_directory = os.path.join(current_file_directory, "../test_outputs/logs/blocking")

def blocking001():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-001.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed
  
def blocking002():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-002.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed

def blocking003():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-003.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed
  
def blocking004():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-004.xml"), test_log_directory=test_log_directory, all_mesh_dir=plates_directory)
  return passed
  
def blocking005():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-005.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed
  
def blocking006():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-006.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed
  
def blocking007():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-007.xml"), test_log_directory=test_log_directory, emit_mesh_dir=cylinder_directory, rec_mesh_dir=sphere_directory, blocking_mesh_dir=cylinder_directory)
  return passed
  
def blocking008():
  passed = runTest.runTest(os.path.join(xmls_directory, "blocking-008.xml"), test_log_directory=test_log_directory, all_mesh_dir=plates_directory)
  return passed
  
def runAllTests(mode = "ALL"):
  dai_passed_counter = 0
  if mode == "ALL" or mode == "DAI":
    if blocking001():
      dai_passed_counter+=1
    if blocking002():
      dai_passed_counter+=1
    if blocking003():
      dai_passed_counter+=1
    if blocking004():
      dai_passed_counter+=1
  sai_passed_counter = 0
  if mode == "ALL" or mode == "SAI":
    if blocking005():
      sai_passed_counter+=1
    if blocking006():
      sai_passed_counter+=1
    if blocking007():
      sai_passed_counter+=1
    if blocking008():
      sai_passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------------- PARALLEL PLATES RESULTS --------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Blocking Tests Results (DAI):\t {dai_passed_counter} / 4 PASSED")
  print(f"Blocking Tests Results (SAI):\t {sai_passed_counter} / 4 PASSED")

  return dai_passed_counter, sai_passed_counter

if __name__ == "__main__":
  runAllTests()