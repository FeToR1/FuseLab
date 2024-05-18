#define FUSE_USE_VERSION 31

#include <fuse/fuse.h>

#include <iostream>

static void show_help(const char *progname) {
    std::cerr << "usage: " << progname << " <mountpoint> [options]" << std::endl;
}


static const struct fuse_operations my_fuse_oper = {};  

int main(int argc, char *argv[]) {
    if (argc < 2) {
        show_help(argv[0]);
        return 1;
    }

    struct fuse_args args = FUSE_ARGS_INIT(argc, argv);
    int ret = fuse_main(args.argc, args.argv, &my_fuse_oper, NULL);
    fuse_opt_free_args(&args);

    return ret;
}