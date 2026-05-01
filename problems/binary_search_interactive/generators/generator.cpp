#ifdef _MSC_VER
#pragma warning(disable: 4459 4100 4244 4996)
#endif
#include "testlib.h"
#include <numeric>
#include <tuple>
#include <type_traits>
using namespace std;

#define ll long long
#define sz(x) int(x.size())

const ll INF = 1LL << 60;

namespace gen_numbers {
    template <typename T = long long>
    T random(T l, T r) {
        if constexpr (std::is_integral_v<T> && std::is_signed_v<T>)
            return static_cast<T>(rnd.next((long long)l, (long long)r));
        else
            return static_cast<T>(rnd.next((double)l, (double)r));
    }
}

using namespace gen_numbers;

// Generator usage (ECPC requires usage instructions):
//   Compile: g++ -std=c++17 -O2 -o generator generators/generator.cpp
//   Run:     ./generator --n=1000000000 --secret=42 <seed> > test.txt
//   n = upper bound, secret = hidden value (-1 for random), seed = last arg

void Generate_tests() {
    int n      = opt<int>("n",      1000000000);
    int secret = opt<int>("secret", -1);
    if (secret == -1) secret = rnd.next(1, n);
    cout << n << ' ' << secret << '\n';
}

int main(int argc, char *argv[]) {
    registerGen(argc, argv, 1);
    Generate_tests();
    return 0;
}
