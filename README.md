# Static LinkStatic Fiasco

If we mix `dlopen` of 2 libraries that share a dependency, but one of the libraries uses `linkstatic = True` we hit a bug:

Not very surprisingly we double-initialize static field

```cpp
// This vector will be initialized twice
static std::vector<int> v;
```

Repro `bazelisk run //:demo`

Result:

```
Opened library a. Pushing 3 elements to static vector and calling the size of the vector
Address of v: 0x7fb9023a6030
3
And second time on the same library a
Address of v: 0x7fb9023a6030
6
Opened library b. Pushing 3 elements to static vector and calling the size of the vector
Address of v: 0x7fb900b42030
3
```
