cc_library(
    name = "lib",
    srcs = [
        "lib.cpp",
    ],
    hdrs = [
        "lib.h",
    ],
)

cc_binary(
    name = "liba.so",
    srcs = [
        "main.cpp",
    ],
    linkshared = True,
    linkstatic = False,
    deps = [
        ":lib",
    ],
)

cc_binary(
    name = "libb.so",
    srcs = [
        "main.cpp",
    ],
    linkshared = True,
    # This `linkstatic = True` is what makes the double-init for the static field.
    linkstatic = True,
    deps = [
        ":lib",
    ],
)

py_binary(
    name = "demo",
    srcs = [
        "demo.py",
    ],
    data = [
        ":liba.so",
        ":libb.so",
    ],
)
