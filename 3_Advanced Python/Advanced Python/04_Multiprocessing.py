import multiprocessing
import time 

def square_number():
  for i in range(5):
    time.sleep(1)
    print(f"Square {i*i}")

def cube_number():
  for i in range(5):
    time.sleep(1.5)
    print(f"Cube {i*i*i}")
    
## Create two process
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    ## Start the process 
    p1.start()
    p2.start()

    ## Wait for the process to complet 

    p1.join()
    p2.join()
    
    print("Both processes completed")
    