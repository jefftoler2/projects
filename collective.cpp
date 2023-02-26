#include "collective.h"
#include "utils.h"

const int COLLECTIVE_DEBUG = 0;

/*************************** DECLARE YOUR HELPER FUNCTIONS HERE ************************/



/*************************** collective.h functions ************************/


 void HPC_Bcast(void* buffer, int count, MPI_Datatype datatype, int root, MPI_Comm comm) {
    // TODO: Implement this function using only sends and receives for communication instead of MPI_Bcast.
    int rank;
	int size;
	int flip, mask;

	MPI_Request req;
	MPI_Status stat;
	MPI_Comm_rank(comm, &rank);
	MPI_Comm_size(comm, &size);
	int d = log2(size);
	
	flip = (1 << (d-1));
	mask = flip - 1;
	
	for(int i = (d-1); i >= 0; i--){
		if(((rank ^ root) & mask) == 0){
            if(((rank ^ root) & flip) ==0){
                MPI_Send(buffer, count, datatype, (rank ^ flip), i, comm);
            }
			else{
                MPI_Recv(buffer, count, datatype, (rank ^ flip), i, comm, &stat);
            }
        }
	mask = (mask >> 1);
	flip = (flip >> 1);	
	}
}


void HPC_Prefix(const HPC_Prefix_func* prefix_func, const void *sendbuf, void *recvbuf, int count,
                MPI_Datatype datatype, MPI_Comm comm, void* wb1, void* wb2, void* wb3) {
    if (count <= 0) return;
    /* Step 1. Run user function on local data with a NULL previous prefix. */
    const void* local_last_prefix = prefix_func(NULL, sendbuf, recvbuf, count); // recvbuf gets local pp from send values
    int rank, size;
    MPI_Comm_size(comm, &size);
    MPI_Comm_rank(comm, &rank);
    int d = ceil(log2(size));
    const void* prefix;
    const void* total = local_last_prefix;
    void* rec_total;
    MPI_Request req;
    MPI_Status stat;
    int x = 0;
    for (int j=0;j<d;j++){ // for all j rounds of parallel prefix
        int rank_send = (rank ^ (int) pow(2,j)); // exchange with rank XOR 2^j
        if(rank_send > size-1){
            continue;
        }
        MPI_Isend(total, 1, datatype, rank_send, j, comm, &req); // sends total, 1 unsigned, to rank_send, uses tag j
        MPI_Recv(wb3, 1, datatype, rank_send, j, comm, &stat); // receives corresponding total
        rec_total = wb3;
        int source = stat.MPI_SOURCE;
        if(source < rank){ // if it is coming from lower rank
            if(x == 0){
                prefix = prefix_func(NULL,rec_total,wb2,1); // if it's first time receiving it does identity operation to initialize prefix
                x++;
            }
            else{
                prefix = prefix_func(rec_total,prefix,wb2,1); // prefix = f(incoming total, current prefix)
            }
            total = prefix_func(rec_total,total,wb1,1); // total = f(incoming total,current total)
        }
        if(source > rank){ // if it is coming from higher rank
            total = prefix_func(total,rec_total,wb1,1); // total = f(current total, incoming total)
        }
        MPI_Wait(&req, &stat); // waits for outgoing message to be received to move on to next round
    }
    if (d > 0 && rank > 0){
        local_last_prefix = prefix_func(prefix, sendbuf, recvbuf, count); // do local prefix function starting with the prefix value found
    }
    // TODO: Implement the rest of this function using sends and receives for communication.
}


/*************************** DEFINE YOUR HELPER FUNCTIONS HERE ************************/

