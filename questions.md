### Questions

#### Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to `histogram_example.png` as a minimum result.

#### Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns an _array_ of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

#### Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
`question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> Since we're sending all the data to the backend, the process_backend_data function have a complexity of O(number_of_peers * max_peer_pool_size) which explain the increasing of the simulation time with the increasing of number_of_peers and max_peer_pool_size

number_of_peers | max_peer_pool_size | number_of_peers * max_peer_pool_size | Backend processing time (s)
--- | --- | ---| ---
10|2 |20 |  00.000041
1 000|10 |10 000 | 00.011293
 1 000|100 | 100 000 | 00.124924
 10 000|10 | 100 000 | 00.130215
1000|1000 |1 000 000 | 00.753385
 10 000|100 | 1 000 000 | 02.008373

#### Question 4

Go to the file `question4.py`:
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.
>> Since the BINS list is constant and known for all peers, an alternative is to calculate locally an histogram and send it to the backend server that will just sum up all the histograms. This will improve the complexity of the process_backend_data function,
>> from O(number_of_peers * max_peer_pool_size) to O(number_of_peers).
>>
>> The simulation confirm that since the backend processing time is much lower than the previous implementation and the processing time doesn't increase with the max_peer_pool_size

number_of_peers | max_peer_pool_size | number_of_peers * max_peer_pool_size | Backend processing time (s)
--- | --- | ---| ---
10|2 |20 |  00.000013
1 000|10 |10 000 | 00.000068
 1 000|100 | 100 000 | 00.000071
1 000|1000 |1 000 000 | 00.000107
 10 000|10 | 100 000 | 00.000726
  10 000|100 | 1 000 000 | 00.000806