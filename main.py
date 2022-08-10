import mlflow
import argparse

def main(training = False):
    with mlflow.start_run() as run:
        if training:
            print("######### TRAINING #################")
            mlflow.run(".", "stage_01", use_conda = False)
            mlflow.run(".", "stage_02", use_conda = False)
        else:
            print("######### PREDICTING #################")
            mlflow.run(".", "stage_03", use_conda = False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--training", "-t", type = int, default = 0)
    parsed_args = args.parse_args()
    main(training = bool(parsed_args.training))
