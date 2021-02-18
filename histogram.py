from random import randint
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    nb_bins = len(bins)
    bins_count = {"bins_name": [], "bins_height": []}
    for i in range(nb_bins - 1):
        bin_count = 0
        bin_i1 = bins[i]
        bin_i2 = bins[i + 1]

        for d in data:
            if bin_i1 <= d < bin_i2:
                bin_count += 1
        bins_count["bins_name"].append(f"{bin_i1}-{bin_i2}")
        bins_count["bins_height"].append(bin_count)


    # add count of numebrs above bins[-1]
    last_bin = bins[-1]
    bin_count = 0
    for d in data:
        if last_bin <= d:
            bin_count += 1
    bins_count["bins_name"].append(f"{last_bin}-+")
    bins_count["bins_height"].append(bin_count)

    return bins_count

def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    #plt.hist(bins_count.keys(), weights=bins_count.values(), bins = list(bins_count.keys()))

    plt.bar(bins_count["bins_name"], bins_count["bins_height"])
    plt.xlabel("Categories")
    plt.ylabel("Count")
    plt.title("Histogram")
    plt.show()

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
