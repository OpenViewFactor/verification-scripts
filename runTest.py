import os, sys

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, 'submodules/pyOpenViewFactor'))
import RunOVF
import parseXML

def runTest(xml_filepath, meshes_directory):
  xml_specifications = parseXML.parseXML(xml_filepath)

  print("\n<><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------- Solver Output --------- ||")
  print("<><><><><><><><><><><><><><><><><><><><>\n")

  proc = RunOVF.RunOVF(
    OVF_EXE_PATH = os.path.join(os.getenv("MY_BINARY_DIR"),"Debug","openviewfactor"),
    INPUT_MESHES = [ os.path.join(meshes_directory, xml_specifications["filepaths"]["emitter"]), os.path.join(meshes_directory, xml_specifications["filepaths"]["receiver"]) ],
    # BLOCKING_MESHES = [ os.path.join(meshes_directory, xml_specifications["filepaths"]["blockers"]) ],
    INTERSECTION_OPTION = xml_specifications["solver-settings"]["self-int"],
    NUMERICAL_METHOD = xml_specifications["solver-settings"]["numerics"],
    COMPUTE_OPTION = xml_specifications["solver-settings"]["compute"],
    PRECISION = xml_specifications["solver-settings"]["precision"]
  )

  result = float(proc.stdout.split("[RESULT] ")[1].split("[LOG]")[0].split(':')[1])

  print(f"Surface-Surface View Factor:\t {result}")

  analytic_result = xml_specifications["test"]["analytic"]
  tolerance = xml_specifications["test"]["tolerance"]
  absolute_error = abs(result - analytic_result)
  print(f"Absolute Error:\t\t\t {absolute_error:E}")
  normalized_absolute_error = absolute_error / analytic_result
  print(f"Normalized Absolute Error:\t\t {normalized_absolute_error:E}")
  passed = normalized_absolute_error < tolerance
  test_result = "PASSED" if passed else "FAILED"
  print(f"Test Result:\t\t\t {test_result}")

  return passed