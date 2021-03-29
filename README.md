# Augmented Data MNIST experiment

Experiment with simple data augmentation for MNIST dataset


## Results

### Baseline
60k provided training examples
10k provided test examples

```
batch_size = 128
epochs = 3

Epoch 1/3
422/422 [==============================] - 7s 16ms/step - loss: 0.7645 - accuracy: 0.7626 - val_loss: 0.0872 - val_accuracy: 0.9757
Epoch 2/3
422/422 [==============================] - 7s 15ms/step - loss: 0.1220 - accuracy: 0.9634 - val_loss: 0.0599 - val_accuracy: 0.9830
Epoch 3/3
422/422 [==============================] - 6s 15ms/step - loss: 0.0864 - accuracy: 0.9729 - val_loss: 0.0453 - val_accuracy: 0.9883

Test loss: 0.04668140038847923
Test accuracy: 0.9848999977111816
```

### Small Augmented
5k provided training examples
15k augmented training examples
10k provided test examples

```
batch_size = 128
epochs = 3

```

10k provided training examples
30k augmented training examples
10k provided test examples

```
batch_size = 128
epochs = 3

```

### Large augmented
60k provided training examples  
180k augmented training examples  
10k provided test examples  

```
batch_size = 128
epochs = 3

```

## Conclusion
