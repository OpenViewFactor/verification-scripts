import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/perpendicular-rectangles")
non_sharing_xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/per-plates")
sharing_xmls_directory = os.path.join(current_file_directory, '../test-xmls/after-asher/per-plates')

def perPlates001():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-001.xml"), meshes_directory)
  
def perPlates002():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-002.xml"), meshes_directory)
  
def perPlates003():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-003.xml"), meshes_directory)
  
def perPlates004():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-004.xml"), meshes_directory)
  
def perPlates005():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-005.xml"), meshes_directory)
  
def perPlates006():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-006.xml"), meshes_directory)
  
def perPlates007():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-007.xml"), meshes_directory)
  
def perPlates008():
  runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-008.xml"), meshes_directory)
  
def perPlates009():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-001.xml"), meshes_directory)
  
def perPlates010():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-002.xml"), meshes_directory)
  
def perPlates011():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-003.xml"), meshes_directory)
  
def perPlates012():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-004.xml"), meshes_directory)
  
def perPlates013():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-005.xml"), meshes_directory)
  
def perPlates014():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-006.xml"), meshes_directory)
  
def perPlates015():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-007.xml"), meshes_directory)
  
def perPlates016():
  runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-008.xml"), meshes_directory)
  
def runAllTests():
  # perPlates001()
  # perPlates002()
  # perPlates003()
  # perPlates004()
  # perPlates005()
  # perPlates006()
  # perPlates007()
  # perPlates008()
  perPlates009()
  perPlates010()
  perPlates011()
  perPlates012()
  perPlates013()
  perPlates014()
  perPlates015()
  perPlates016()

  passed_counter = 0
  # if perPlates001():
  #   passed_counter+=1
  # if perPlates002():
  #   passed_counter+=1
  # if perPlates003():
  #   passed_counter+=1
  # if perPlates004():
  #   passed_counter+=1
  # if perPlates005():
  #   passed_counter+=1
  # if perPlates006():
  #   passed_counter+=1
  # if perPlates007():
  #   passed_counter+=1
  # if perPlates008():
  #   passed_counter+=1
  if perPlates009():
    passed_counter+=1
  if perPlates010():
    passed_counter+=1
  if perPlates011():
    passed_counter+=1
  if perPlates012():
    passed_counter+=1
  if perPlates013():
    passed_counter+=1
  if perPlates014():
    passed_counter+=1
  if perPlates015():
    passed_counter+=1
  if perPlates016():
    passed_counter+=1

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------- PERPENDICULAR PLATES RESULTS ------------- ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Perpendicular Plates Results:\t {passed_counter} / 16 PASSED")

  return passed_counter

if __name__ == "__main__":
  runAllTests()