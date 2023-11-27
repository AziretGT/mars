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
# STEP5
            if total_weight == 713:
                print("Congratulations! You have found all the boxes!")
                break
# STEP6
            else:
                for i in range(3):
                # New kilometer and weight for the box if it moves
                    new_kilometer = boxes[i][0] + 5  # Example new kilometer (can be modified)
                    new_weight = boxes[i][1] + 10    # Example new weight (can be modified)
                    boxes[i] = [new_kilometer, new_weight]
# STEP7
            print(boxes)

find_cargo()