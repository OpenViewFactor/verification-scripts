import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, '..'))
import runTest

meshes_directory = os.path.join(current_file_directory, "../submodules/verification-meshes/coaxial-cylinders")
xmls_directory = os.path.join(current_file_directory, "../test-xmls/asher-cases/coaxial-cylinders")

def cylinders001():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-001.xml"), meshes_directory)
  print(proc.stdout)

def cylinders002():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-002.xml"), meshes_directory)
  print(proc.stdout)

def cylinders003():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-003.xml"), meshes_directory)
  print(proc.stdout)

def cylinders004():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-004.xml"), meshes_directory)
  print(proc.stdout)

def cylinders005():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-005.xml"), meshes_directory)
  print(proc.stdout)

def cylinders006():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-006.xml"), meshes_directory)
  print(proc.stdout)

def cylinders007():
  proc = runTest.runTest(os.path.join(xmls_directory, "coaxial-cylinders-007.xml"), meshes_directory)
  print(proc.stdout)


def runAllTests():
  cylinders001()
  cylinders002()
  cylinders003()
  cylinders004()
  cylinders005()
  cylinders006()
  cylinders007()

if __name__ == "__main__":
  runAllTests()