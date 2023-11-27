# STEP1
def find_cargo():
    boxes = [[0, 0], [0, 0], [0, 0]]
# STEP2
    while True:
            total_weight = 0
# STEP3
            for i in range(3):
                kilometer = int(input(f"Enter the kilometer for box {i + 1}: "))
                weight = int(input(f"Enter the weight for box {i + 1}: "))

                boxes[i][0] += kilometer
                boxes[i][1] += weight
# STEP4         
                total_weight += boxes[i][1]
