#include "lib.h"
extern "C" int push_3_items_to_static_vector_and_get_size();

int push_3_items_to_static_vector_and_get_size() {
    auto v = get_vector();
    v->push_back(1);
    v->push_back(1);
    v->push_back(1);
    return v->size();
}
