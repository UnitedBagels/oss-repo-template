# Lab 9 - Databases - CSCI 4470
### Thomas Arturi

## Checkpoint 1

Pop-up showing TensorFlow working:

![](check1/ch1.PNG)

## Checkpoint 2

Showing images 9000 - 9014 instead of images 0 - 15:
![](check2/ch2.PNG)

## Checkpoint 3

### Image 1: Coat

![](check3/coat.PNG)

Result: Correct match!

![](check3/coat_out.PNG)

### Image 2: Sweater (Shirt)

![](check3/sweater.jpg)

Result: Despite there being no label for Sweater, the model correctly identified this as a shirt, which is what I was hoping.

![](check3/shirt_out.PNG)

### Image 3: Boot

![](check3/boot.jpg)

Result: This was the only one the model did not correctly identify. The expectation would be for the label 'Ankle boot' or even 'Sneaker', but not terrible results overall.   

![](check3/shoes_out.PNG)
