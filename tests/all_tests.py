import test_cylinders
import test_parallel_discs
import test_parallel_plates
import test_perpendicular_plates_sharing
import test_perpendicular_plates_nonsharing
import test_spheres
import test_blocking

def runAllTests():
  parallel_plates_passed_dai, parallel_plates_passed_sai = test_parallel_plates.runAllTests()
  perpendicular_sharing_passed_dai, perpendicular_sharing_passed_sai = test_perpendicular_plates_sharing.runAllTests()
  # perpendicular_nonsharing_passed_dai, perpendicular_nonsharing_passed_sai = test_perpendicular_plates_nonsharing.runAllTests()
  parallel_discs_passed_dai, parallel_discs_passed_sai = test_parallel_discs.runAllTests()
  cylinders_passed_dai, cylinders_passed_sai = test_cylinders.runAllTests()
  spheres_passed_dai, spheres_passed_sai = test_spheres.runAllTests()
  blocked_passed_dai, blocked_passed_sai = test_blocking.runAllTests()

  print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
  print("|| ------------------- ALL TESTS RESULTS ------------------ ||")
  print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")

  print(f"Parallel Plates Results (DAI):\t\t\t{parallel_plates_passed_dai} / 8 PASSED")
  print(f"Parallel Plates Results (SAI):\t\t\t{parallel_plates_passed_sai} / 8 PASSED")
  print(f"Parallel Plates Results:\t\t\t{parallel_plates_passed_dai + parallel_plates_passed_sai} / 16 PASSED")

  print(f"Perpendicular Plates (Sharing) Results (DAI):\t{perpendicular_sharing_passed_dai} / 8 PASSED")
  print(f"Perpendicular Plates (Sharing) Results (SAI):\t{perpendicular_sharing_passed_sai} / 8 PASSED")
  print(f"Perpendicular Plates (Sharing) Results:\t\t{perpendicular_sharing_passed_dai + perpendicular_sharing_passed_sai} / 16 PASSED")

  # print(f"Perpendicular Plates (Nonsharing) Results (DAI):\t {perpendicular_nonsharing_passed_dai} / 8 PASSED")
  # print(f"Perpendicular Plates (Nonsharing) Results (SAI):\t {perpendicular_nonsharing_passed_sai} / 8 PASSED")
  # print(f"Perpendicular Plates (Nonsharing) Results:\t {perpendicular_nonsharing_passed_dai + perpendicular_nonsharing_passed_sai} / 16 PASSED")

  print(f"Parallel Discs Results (DAI):\t\t\t{parallel_discs_passed_dai} / 8 PASSED")
  print(f"Parallel Discs Results (SAI):\t\t\t{parallel_discs_passed_sai} / 8 PASSED")
  print(f"Parallel Discs Results:\t\t\t\t{parallel_discs_passed_dai + parallel_discs_passed_sai} / 16 PASSED")
  
  print(f"Concentric Cylinders Results (DAI):\t\t{cylinders_passed_dai} / 7 PASSED")
  print(f"Concentric Cylinders Results (SAI):\t\t{cylinders_passed_sai} / 7 PASSED")
  print(f"Concentric Cylinders Results:\t\t\t{cylinders_passed_dai + cylinders_passed_sai} / 14 PASSED")
  
  print(f"Concentric Spheres Results (DAI):\t\t{spheres_passed_dai} / 6 PASSED")
  print(f"Concentric Spheres Results (SAI):\t\t{spheres_passed_sai} / 6 PASSED")
  print(f"Concentric Spheres Results:\t\t\t{spheres_passed_dai + spheres_passed_sai} / 12 PASSED")
  
  print(f"Blocking Tests Results (DAI):\t\t\t{blocked_passed_dai} / 4 PASSED")
  print(f"Blocking Tests Results (SAI):\t\t\t{blocked_passed_sai} / 4 PASSED")
  print(f"Blocking Tests Results:\t\t\t\t{blocked_passed_dai + blocked_passed_sai} / 8 PASSED")

if __name__ == "__main__":
  runAllTests()