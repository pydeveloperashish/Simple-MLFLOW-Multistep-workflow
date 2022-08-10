import mlflow

with open('artifacts01.txt', 'r') as f:
    text = f.read()
    
with open('artifacts02.txt', 'w') as f:
    f.write(text + "added lines")
        
        
mlflow.log_metric("last_text", text)        
print("end of stage3")