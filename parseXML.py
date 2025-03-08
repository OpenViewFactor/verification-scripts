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
  tolerance = float(targets.findall('TOLERANCE')[0].text)

  print("Analytic Result:\t\t", analytic_result)
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
  settings        = xml_root.findall('SETTINGS')[0]
  self_int        = settings.findall('s')[0].text
  blocking_type   = settings.findall('t')[0].text
  back_face_mode  = settings.findall('f')[0].text
  numerics        = settings.findall('n')[0].text
  precision       = settings.findall('p')[0].text
  compute         = settings.findall('c')[0].text
  matrix_out      = settings.findall('m')[0].text
  graphic_out     = settings.findall('g')[0].text
  bvh_out         = settings.findall('b')[0].text
  log_out         = settings.findall('l')[0].text

  print("Self-Intersection:\t\t", self_int)
  print("Blocking Mode:\t\t\t", blocking_type)
  print("Back-face Culling Mode:\t", back_face_mode)
  print("Numerical Method:\t\t", numerics)
  print("Floating-Point Precision:\t", precision)
  print("Compute Back-End:\t\t", compute)

  test_data = { "analytic" : analytic_result, "tolerance" : tolerance }
  filepaths = { "emitter" : emitter, "receiver" : receiver, "blockers" : blockers }
  solver_settings = { "self-int" : self_int,
                      "blocking type" : blocking_type,
                      "back-face cull mode" : back_face_mode,
                      "numerics" : numerics,
                      "precision" : precision,
                      "compute" : compute,
                      "matrix output" : matrix_out,
                      "graphic output" : graphic_out,
                      "bvh output" : bvh_out,
                      "log output" : log_out}

  return { "test data" : test_data, "filepaths" : filepaths, "solver settings" : solver_settings }