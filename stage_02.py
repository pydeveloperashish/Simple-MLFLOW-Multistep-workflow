import mlflow

with open('artifacts01.txt', 'r') as f:
    text = f.read()
        
print(text)
print("end of stage2")
mlflow.log_param("text", text)