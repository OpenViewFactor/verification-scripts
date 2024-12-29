import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-discs")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/coaxial-discs")

def parDiscs001():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-001.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs002():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-002.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs003():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-003.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs004():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-004.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs005():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-005.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs006():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-006.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs007():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-007.xml"), meshes_directory)
  print(proc.stdout)

def parDiscs008():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-discs-008.xml"), meshes_directory)
  print(proc.stdout)



def runAllTests():
  parDiscs001()
  parDiscs002()
  parDiscs003()
  parDiscs004()
  parDiscs005()
  parDiscs006()
  parDiscs007()
  parDiscs008()

if __name__ == "__main__":
  runAllTests()