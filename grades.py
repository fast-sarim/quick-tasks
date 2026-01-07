while True:
    marks = input("Enter marks (or type exit): ")

    if marks.lower() == "exit":
        print("Program stopped.")
        break

    marks = int(marks)

    if marks >= 90 and marks <= 100:
        print("A")
    elif marks >= 80 and marks < 90:
        print("B")
    elif marks >= 70 and marks < 80:
        print("C")
    elif marks >= 50 and marks < 70 and marks >= 0 :
        print("D")
    elif marks > 100 or marks < 0:
        print("Invalid marks")
    else:
        print("F")
