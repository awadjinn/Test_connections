from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """
        connection_durations = []
        for p in self.peer_pool:
            connection_durations.append(self.peer_pool[p])
        return connection_durations


class SimulationQ2(Simulation):

    def generate_network(self):
        self.network = [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """

        # Every connection, peer1 <--> peer2 for example, is present twice.
        # Once in the the peer1 peer_pool and second in the peer2 peer_pool.
        # therefore we must divide the count by 2
        data = [i for l in self.backend_database for i in l]
        bins_count = compute_histogram_bins(data, BINS)
        counts = [i/2 for i in bins_count["bins_height"]]

        return counts

if __name__ == "__main__":


    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()


    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
