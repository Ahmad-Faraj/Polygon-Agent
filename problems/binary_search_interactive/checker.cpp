#include "testlib.h"
using namespace std;

int main(int argc, char *argv[]) {
    setName("check that interactor accepted");
    registerTestlibCmd(argc, argv);
    // For interactive problems the interactor handles correctness.
    // This checker simply confirms the interactor said OK.
    quitf(_ok, "accepted by interactor");
}
