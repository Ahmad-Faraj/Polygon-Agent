#include "testlib.h"
using namespace std;

int main(int argc, char *argv[]) {
    registerValidation(argc, argv);

    int n = inf.readInt(1, 100000, "n");
    inf.readSpace();
    inf.readLong(-1000000000LL, 1000000000LL, "target");
    inf.readEoln();

    inf.readInts(n, -1000000000, 1000000000, "a");
    inf.readEoln();

    inf.readEof();
    return 0;
}
