import test_cylinders
import test_parallel_discs
import test_parallel_plates
import test_perpendicular_plates

def runAllTests():
  parallel_plates_passed = test_parallel_plates.runAllTests()
  perpendicular_passed = test_perpendicular_plates.runAllTests()
  parallel_discs_passed = test_parallel_discs.runAllTests()
  # cylinders_passed = test_cylinders.runAllTests()

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------------- ALL TESTS RESULTS ------------------ ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Plates Results:\t {parallel_plates_passed} / 8 PASSED")
  print(f"Perpendicular Plates Results:\t {perpendicular_passed} / 16 PASSED")
  print(f"Parallel Discs Results:\t\t {parallel_discs_passed} / 8 PASSED")
  # print(f"Concentric Cylinders Results:\t {cylinders_passed} / 7 PASSED")