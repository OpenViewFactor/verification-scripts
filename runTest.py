import os, sys, pdb
from pathlib import Path
import platform

current_file_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_file_directory, 'submodules/pyOpenViewFactor'))
import RunOVF
import parseXML

def runTest(xml_filepath, test_log_directory, all_mesh_dir = None, emit_mesh_dir = None, rec_mesh_dir = None, blocking_mesh_dir = None):
  xml_specifications = parseXML.parseXML(xml_filepath)

  print("\n<><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------- Solver Output --------- ||")
  print("<><><><><><><><><><><><><><><><><><><><>\n")

  system = platform.system()

  if system == "Windows":
    path_split_character = "\\"
  elif system == "Linux":
    path_split_character = "/"

  xml_filepath_without_extension = xml_filepath.split(".")[-2]
  xml_filename_without_path = xml_filepath_without_extension.split(path_split_character)[-1]
  log_filepath = os.path.join(test_log_directory, xml_filename_without_path)

  if not all_mesh_dir == None:
    emit_mesh_dir = all_mesh_dir
    rec_mesh_dir = all_mesh_dir
    blocking_mesh_dir = all_mesh_dir
  
  if xml_specifications["filepaths"]["blockers"][0] == "NONE":
    obstructions = None
  else:
    obstructions = [ os.path.join(blocking_mesh_dir, blocker) for blocker in xml_specifications["filepaths"]["blockers"] ]

  RunOVF.RunOVF(
    OVF_EXE_PATH = os.path.join(os.getenv("MY_BINARY_DIR"),"ovf"),
    inputs = [ os.path.join(emit_mesh_dir, xml_specifications["filepaths"]["emitter"]), os.path.join(rec_mesh_dir, xml_specifications["filepaths"]["receiver"]) ],
    obstructions = obstructions,
    selfint = xml_specifications["solver settings"]["self-int"],
    numerics = xml_specifications["solver settings"]["numerics"],
    compute = xml_specifications["solver settings"]["compute"],
    precision = xml_specifications["solver settings"]["precision"],
    backfacecull = xml_specifications["solver settings"]["back-face cull mode"],
    blockingtype = xml_specifications["solver settings"]["blocking type"],
    matrixout = xml_specifications["solver settings"]["matrix output"],
    graphicout = xml_specifications["solver settings"]["graphic output"],
    bvhout = xml_specifications["solver settings"]["bvh output"],
    logfile = log_filepath
  )

  log_contents = Path(log_filepath+".txt").read_text()

  result = float(log_contents.split("[RESULT] ")[1].split("[LOG]")[0].split(':')[1])

  print(f"Surface-Surface View Factor:\t {result}")

  analytic_result = xml_specifications["test data"]["analytic"]
  tolerance = xml_specifications["test data"]["tolerance"]
  absolute_error = abs(result - analytic_result)
  print(f"Absolute Error:\t\t\t {absolute_error:E}")
  passed = absolute_error < tolerance
  test_result = "PASSED" if passed else "FAILED"
  print(f"Test Result:\t\t\t {test_result}")

  return passed