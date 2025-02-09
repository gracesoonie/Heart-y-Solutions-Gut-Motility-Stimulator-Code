import xarm

arm = xarm.Controller('USB')

arm.setPosition([[3, 91], [4, 733], [5, 453], [6, 476]], 4000, wait=True)  # 1
arm.setPosition([[3, 51], [4, 728], [5, 488], [6, 476]], 4000, wait=True)  # 2
arm.setPosition([[3, 56], [4, 801], [5, 567], [6, 475]], 4000, wait=True)  # 3
arm.setPosition([[3, 93], [4, 907], [5, 653], [6, 461]], 4000, wait=True)  # 4
arm.setPosition([[3, 118], [4, 950], [5, 714], [6, 511]], 4000, wait=True) # 5
arm.setPosition([[3, 94], [4, 790], [5, 506], [6, 552]], 4000, wait=True)  # 6
arm.setPosition([[3, 64], [4, 682], [5, 413], [6, 508]], 4000, wait=True)  # 7
arm.setPosition([[3, 108], [4, 722], [5, 418], [6, 471]], 4000, wait=True) # 8
