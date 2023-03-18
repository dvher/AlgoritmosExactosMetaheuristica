#include <iostream>
#include <vector>
#include <getopt.h>
#include "puzzle.hpp"

int main(int argc, char **argv) {

    int opt;
    std::string filename = "";

    while((opt = getopt(argc, argv, ":f:")) != -1) {

        switch(opt) {

            case 'f':
                filename = optarg;
                break;
            case ':':
                std::cerr << "Filename to read needed.\n";
                return 1;
            case '?':
                std::cerr << "Unknown option -" << (char)optopt << "\n";
                return 1;

        }

    }

    if(filename == "") {
        std::cerr << "Filename to read needed" << "\n";
        return 1;
    }

    Puzzle puzzle = Puzzle(filename);

    puzzle.print();

    return 0;

}
