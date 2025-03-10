import test_cylinders
import test_parallel_discs
import test_parallel_plates
import test_perpendicular_plates_sharing
import test_perpendicular_plates_nonsharing
import test_spheres

def runAllTests():
  parallel_plates_passed = test_parallel_plates.runAllTests()
  perpendicular_sharing_passed = test_perpendicular_plates_sharing.runAllTests()
  # perpendicular_nonsharing_passed = test_perpendicular_plates_nonsharing.runAllTests()
  parallel_discs_passed = test_parallel_discs.runAllTests()
  cylinders_passed = test_cylinders.runAllTests()
  spheres_passed = test_spheres.runAllTests()

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------------- ALL TESTS RESULTS ------------------ ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Plates Results:\t {parallel_plates_passed} / 16 PASSED")
  print(f"Perpendicular Plates (Sharing) Results:\t {perpendicular_sharing_passed} / 16 PASSED")
  # print(f"Perpendicular Plates (Nonsharing) Results:\t {perpendicular_nonsharing_passed} / 16 PASSED")
  print(f"Parallel Discs Results:\t\t {parallel_discs_passed} / 16 PASSED")
  print(f"Concentric Cylinders Results:\t {cylinders_passed} / 14 PASSED")
  print(f"Concentric Spheres Results:\t {spheres_passed} / 12 PASSED")

if __name__ == "__main__":
  runAllTests()