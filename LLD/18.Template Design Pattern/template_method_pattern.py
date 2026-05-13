from abc import ABC, abstractmethod

# 1. Base class defining the template method
class ModelTrainer(ABC):
    # The template method — defines the skeleton of the algorithm
    def train_pipeline(self, data_path: str):
        self._load_data(data_path)
        self._preprocess_data()
        self._train_model()      # subclass-specific
        self._evaluate_model()   # subclass-specific
        self._save_model()       # subclass-specific or default

    def _load_data(self, path: str):
        print(f"[Common] Loading dataset from {path}")
        # e.g., read CSV, images, etc.

    def _preprocess_data(self):
        print("[Common] Splitting into train/test and normalizing")

    @abstractmethod
    def _train_model(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def _evaluate_model(self):
        """Must be implemented by subclasses"""
        pass

    # Provide a default save, but subclasses can override if needed
    def _save_model(self):
        print("[Common] Saving model to disk as default format")


# 2. Concrete subclass: Neural Network
class NeuralNetworkTrainer(ModelTrainer):
    def _train_model(self):
        print("[NeuralNet] Training Neural Network for 100 epochs")
        # pseudo-code: forward/backward passes, gradient descent...

    def _evaluate_model(self):
        print("[NeuralNet] Evaluating accuracy and loss on validation set")

    def _save_model(self):
        print("[NeuralNet] Serializing network weights to .h5 file")


# 3. Concrete subclass: Decision Tree
class DecisionTreeTrainer(ModelTrainer):
    # Uses the default _preprocess_data() (train/test split + normalize)

    def _train_model(self):
        print("[DecisionTree] Building decision tree with max_depth=5")
        # pseudo-code: recursive splitting on features...

    def _evaluate_model(self):
        print("[DecisionTree] Computing classification report (precision/recall)")

    # Uses the default _save_model()


# 4. Usage
def main():
    print("=== Neural Network Training ===")
    nn_trainer = NeuralNetworkTrainer()
    nn_trainer.train_pipeline("data/images/")

    print("\n=== Decision Tree Training ===")
    dt_trainer = DecisionTreeTrainer()
    dt_trainer.train_pipeline("data/iris.csv")


if __name__ == "__main__":
    main()
