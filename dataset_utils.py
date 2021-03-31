import numpy as np
import matplotlib.pyplot as plt

def view_images(dataset, size):
    """ View all the images in the dataset, on a 3 by X grid size.

    Parameters:
        dataset (images, labels) - Dataset to visualise.
        size (int, int) - width and height of each image.
    """
    images, labels = dataset
    assert images.shape[0] == labels.shape[0]

    num_images = images.shape[0]
    num_cols = 3
    num_rows = np.ceil(num_images / num_cols).astype("int")
    plt.figure(figsize=size)
    for i in range(num_images):
        image = images[i]
        label = labels[i]
        ax = plt.subplot(num_rows, num_cols, i + 1)
        plt.imshow(np.array(image, dtype="float"))
        plt.title("Number: " + str(label))
        plt.axis("off")


def normalise(dataset):
    """ Normalises and reshapes the images in the dataset.

    Parameters:
        dataset (images, labels) - Dataset to normalise.
    
    Returns:
        The normalised dataset.
    """
    # Scale images to the [0, 1] range
    dataset = dataset.astype("float32") / 255
    # Make sure images have shape (28, 28, 1)
    return np.expand_dims(dataset, -1)


def choice(dataset, size):
    """ Randomly chooses some data from the dataset.

    Parameters:
        dataset (images, labels) - Dataset to choose from.
        size (int) - Number of data-points to select.
    
    Returns:
        A new dataset of size `size`.
    """
    x, y = dataset
    assert x.shape[0] == y.shape[0]

    num_datapoints = x.shape[0]
    mask = np.zeros(num_datapoints).astype("bool")
    mask[:size] = True
    np.random.default_rng().shuffle(mask)
    return x.compress(mask, axis=0), y.compress(mask, axis=0)


def print_dataset_summary(name, dataset):
    print("{} shape: {} {}".format(name, dataset.shape, type(dataset)))
