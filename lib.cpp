#include "lib.h"
#include <iostream>
#include <sstream>

using namespace std;

vector<int>* get_vector() {
    // We re-init this static.
    static std::vector<int> v;

    std::cout << "Address of v: " << &v << "\n";
    return &v;
}
