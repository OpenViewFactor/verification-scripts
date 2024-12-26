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
    OVF_EXE_PATH = os.path.join(current_file_directory, "submodules/ovf/build/ovf/cli/openviewfactor"),
    INPUT_MESHES = [ os.path.join(meshes_directory, xml_specifications["filepaths"]["emitter"]), os.path.join(meshes_directory, xml_specifications["filepaths"]["receiver"]) ],
    # BLOCKING_MESHES = [ os.path.join(meshes_directory, xml_specifications["filepaths"]["blockers"]) ],
    INTERSECTION_OPTION = xml_specifications["solver-settings"]["self-int"],
    NUMERICAL_METHOD = xml_specifications["solver-settings"]["numerics"],
    COMPUTE_OPTION = xml_specifications["solver-settings"]["compute"],
    PRECISION = xml_specifications["solver-settings"]["precision"]
  )

  return proc