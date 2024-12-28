import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/perpendicular-rectangles")
non_sharing_xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/per-plates")
sharing_xmls_directory = os.path.join(current_file_directory, '../test-xmls/after-asher/per-plates')

def perPlates001():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-001.xml"), meshes_directory)
  print(proc.stdout)

def perPlates002():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-002.xml"), meshes_directory)
  print(proc.stdout)

def perPlates003():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-003.xml"), meshes_directory)
  print(proc.stdout)

def perPlates004():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-004.xml"), meshes_directory)
  print(proc.stdout)

def perPlates005():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-005.xml"), meshes_directory)
  print(proc.stdout)

def perPlates006():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-006.xml"), meshes_directory)
  print(proc.stdout)

def perPlates007():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-007.xml"), meshes_directory)
  print(proc.stdout)

def perPlates008():
  proc = runTest.runTest(os.path.join(non_sharing_xmls_directory, "per-plate-nonsharing-008.xml"), meshes_directory)
  print(proc.stdout)

def perPlates009():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-001.xml"), meshes_directory)
  print(proc.stdout)

def perPlates010():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-002.xml"), meshes_directory)
  print(proc.stdout)

def perPlates011():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-003.xml"), meshes_directory)
  print(proc.stdout)

def perPlates012():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-004.xml"), meshes_directory)
  print(proc.stdout)

def perPlates013():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-005.xml"), meshes_directory)
  print(proc.stdout)

def perPlates014():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-006.xml"), meshes_directory)
  print(proc.stdout)

def perPlates015():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-007.xml"), meshes_directory)
  print(proc.stdout)

def perPlates016():
  proc = runTest.runTest(os.path.join(sharing_xmls_directory, "per-plate-sharing-008.xml"), meshes_directory)
  print(proc.stdout)



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

if __name__ == "__main__":
  runAllTests()