import xml.etree.ElementTree as ET

def parseXML(filepath):
  xml_root = ET.parse(filepath).getroot()

  print("\n<><><><><><><><><><><><><><><><><><><><>")
  print("|| ---------- Test Metadata --------- ||")
  print("<><><><><><><><><><><><><><><><><><><><>\n")

  information = xml_root.findall('TEST-DESCRIPTION')[0]
  configuration = information.findall('TEST-CONFIGURATION')[0].text
  author = information.findall('AUTHOR')[0].text
  date_created = information.findall('DATE-CREATED')[0].text

  print("Test:\t\t\t\t", configuration)
  print("Author:\t\t\t\t", author)
  print("Date Created:\t\t\t", date_created)

  print("< -------- Numerical Targets -------- >")

  targets = xml_root.findall('TARGETS')[0]
  analytic_result = float(targets.findall('ANALYTIC-RESULT')[0].text)
  expect_numerical_result = float(targets.findall('EXPECTED-NUMERICAL-RESULT')[0].text)
  tolerance = float(targets.findall('TOLERANCE')[0].text)

  print("Analytic Result:\t\t", analytic_result)
  print("Expected Numerical Result:\t", expect_numerical_result)
  print("Test Tolerance:\t\t\t", tolerance)

  print("< ------------- Meshes -------------- >")

  meshes = xml_root.findall('MESHES')[0]
  emitter = meshes.findall('EMITTER')[0].text
  receiver = meshes.findall('RECEIVER')[0].text
  blockers = [ mesh.text for mesh in meshes.findall('BLOCKER') ]

  print("Emitter Mesh:\t\t\t", emitter)
  print("Receiver Mesh:\t\t\t", receiver)
  print("Blockers:\t\t\t", blockers)

  print("< --------- Solver Settings --------- >")
  settings = xml_root.findall('SETTINGS')[0]
  intersection_option = settings.findall('SELF-INT')[0].text
  numerical_method = settings.findall('METHOD')[0].text
  compute_option = settings.findall('COMPUTE')[0].text
  precision = settings.findall('PRECISION')[0].text

  print("Self-Intersection:\t\t", intersection_option)
  print("Numerical Method:\t\t", numerical_method)
  print("Compute Back-End:\t\t", compute_option)
  print("Floating-Point Precision:\t", precision)

  test_checks = { "analytic" : analytic_result, "tolerance" : tolerance }
  filepaths = { "emitter" : emitter, "receiver" : receiver, "blockers" : blockers }
  solver_settings = { "self-int" : intersection_option, "numerics" : numerical_method, "compute" : compute_option, "precision" : precision }

  return { "test" : test_checks, "filepaths" : filepaths, "solver-settings" : solver_settings }