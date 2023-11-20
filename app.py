import mlflow
import warnings
warnings.filterwarnings("ignore")

def calculate(x,y):
    return (x*y)

if __name__ == "__main__":
    with mlflow.start_run():
        x,y = 5,990
        result = calculate(x,y)
        print(f"Here is my Result {result}")
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        mlflow.log_param("result",result)