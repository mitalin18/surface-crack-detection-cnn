import mlflow
import mlflow.tensorflow


def start_experiment(experiment_name):
    mlflow.set_experiment(experiment_name)
    mlflow.start_run()


def log_params(
    image_size,
    batch_size,
    epochs
):
    mlflow.log_param("image_size", image_size)
    mlflow.log_param("batch_size", batch_size)
    mlflow.log_param("epochs", epochs)
    mlflow.log_param("optimizer", "adam")


def log_training_metrics(history):

    mlflow.log_metric(
        "best_train_accuracy",
        max(history.history["accuracy"])
    )

    mlflow.log_metric(
        "best_val_accuracy",
        max(history.history["val_accuracy"])
    )

    mlflow.log_metric(
        "best_train_loss",
        min(history.history["loss"])
    )

    mlflow.log_metric(
        "best_val_loss",
        min(history.history["val_loss"])
    )

    if "precision" in history.history:
        mlflow.log_metric(
            "best_train_precision",
            max(history.history["precision"])
        )

    if "val_precision" in history.history:
        mlflow.log_metric(
            "best_val_precision",
            max(history.history["val_precision"])
        )

    if "recall" in history.history:
        mlflow.log_metric(
            "best_train_recall",
            max(history.history["recall"])
        )

    if "val_recall" in history.history:
        mlflow.log_metric(
            "best_val_recall",
            max(history.history["val_recall"])
        )

    if "auc" in history.history:
        mlflow.log_metric(
            "best_train_auc",
            max(history.history["auc"])
        )

    if "val_auc" in history.history:
        mlflow.log_metric(
            "best_val_auc",
            max(history.history["val_auc"])
        )


def log_test_metrics(
    test_loss,
    test_accuracy,
    test_precision,
    test_recall,
    test_auc
):

    mlflow.log_metric(
        "test_loss",
        float(test_loss)
    )

    mlflow.log_metric(
        "test_accuracy",
        float(test_accuracy)
    )

    mlflow.log_metric(
        "test_precision",
        float(test_precision)
    )

    mlflow.log_metric(
        "test_recall",
        float(test_recall)
    )

    mlflow.log_metric(
        "test_auc",
        float(test_auc)
    )


def log_model(model):
    mlflow.tensorflow.log_model(
        model,
        artifact_path="crack_detection_model"
    )


def end_experiment():
    mlflow.end_run()