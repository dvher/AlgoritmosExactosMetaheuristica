#ifndef _PUZZLE_HPP
#define _PUZZLE_HPP

#include <cstdint>
#include <iostream>
#include <vector>

class Puzzle {

    private:

        uint8_t size;
        std::vector<std::vector<bool>> matrix;
        std::vector<std::vector<std::vector<uint32_t>>> domains;
        std::vector<std::vector<std::vector<uint32_t>>> constraints;

        void fill_vector(std::vector<uint32_t> &v, std::string line, char dlm);
        void fill_vector(std::vector<std::vector<uint32_t>> &v, std::string line, char dlm_outer, char dlm_inner);
        void fill_constraints(std::vector<std::vector<std::vector<uint32_t>>> &m, std::ifstream &file_handler, char dlm_outer, char dlm_inner);
        void print(std::vector<std::vector<uint32_t>> v);
        void check(std::vector<std::vector<uint32_t>> v);
        void calculate_domains();
        uint32_t value_to_squares(uint32_t v);
        std::vector<uint32_t> get_domain(std::vector<uint32_t> c);
        std::vector<uint32_t> get_domain(std::vector<uint32_t> domain, std::vector<uint32_t> squares, uint16_t idx, uint16_t left_pos, uint32_t acc);
        std::vector<bool> bit_representation(uint32_t n);

    public:

        Puzzle();
        Puzzle(std::string filename);
        void read_file(std::string filename);
        void print();

};

#endif /* _PUZZLE_HPP */
