import xarm

arm = xarm.Controller('USB')

arm.setPosition([[3, 156], [4, 863], [5, 580], [6, 548]], 4000, wait=True)  # 1
arm.setPosition([[3, 217], [4, 872], [5, 542], [6, 526]], 4000, wait=True)  # 2
arm.setPosition([[3, 212], [4, 820], [5, 480], [6, 502]], 4000, wait=True)  # 3
arm.setPosition([[3, 200], [4, 797], [5, 457], [6, 469]], 4000, wait=True)  # 4
arm.setPosition([[3, 166], [4, 810], [5, 509], [6, 468]], 4000, wait=True)  # 5
arm.setPosition([[3, 129], [4, 810], [5, 550], [6, 468]], 4000, wait=True)  # 6
arm.setPosition([[3, 107], [4, 820], [5, 578], [6, 468]], 4000, wait=True)  # 7
arm.setPosition([[3, 75], [4, 836], [5, 606], [6, 468]], 4000, wait=True)   # 8
arm.setPosition([[3, 66], [4, 846], [5, 622], [6, 456]], 4000, wait=True)   # 9
arm.setPosition([[3, 96], [4, 918], [5, 655], [6, 440]], 4000, wait=True)   # 10
arm.setPosition([[3, 96], [4, 904], [5, 667], [6, 474]], 4000, wait=True)   # 11
arm.setPosition([[3, 132], [4, 904], [5, 659], [6, 529]], 4000, wait=True)  # 12
arm.setPosition([[3, 175], [4, 905], [5, 622], [6, 552]], 4000, wait=True)  # 13