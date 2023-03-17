#ifndef _SOLVER_HPP
#define _SOLVER_HPP

#include <cstdint>
#include <iostream>
#include <vector>

class Solver {

    private:

        std::vector<std::vector<bool>> matrix;
        std::vector<std::vector<uint32_t>> rows;
        std::vector<std::vector<uint32_t>> cols;

        void fill_vector(std::vector<uint32_t> &v, std::string line, char dlm);
        void fill_vector(std::vector<std::vector<uint32_t>> &v, std::string line, char dlm_outer, char dlm_inner);
        void print(std::vector<std::vector<uint32_t>> v);
        void check(std::vector<std::vector<uint32_t>> v);

    public:

        Solver();
        Solver(std::string filename);
        void read_file(std::string filename);
        void print();

};

#endif /* _SOLVER_HPP */
