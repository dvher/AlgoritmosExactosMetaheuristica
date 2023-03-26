#include <algorithm>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cmath>
#include "puzzle.hpp"

Puzzle::Puzzle() {
}

Puzzle::Puzzle(std::string filename) {
    this->read_file(filename);
}

void Puzzle::read_file(std::string filename) {

    std::ifstream file_handler(filename, std::ios::in);

    if(!file_handler.is_open()) {
        std::cout << "Couldn't open file\n";
        exit(1);
    }

    std::string line;

    std::getline(file_handler, line);

    this->fill_vector(this->rows_constraints, line, ' ', ',');

    std::getline(file_handler, line);

    this->fill_vector(this->cols_constraints, line, ' ', ',');

    file_handler.close();

    this->check(this->rows_constraints);
    this->check(this->cols_constraints);

    if(this->rows_constraints.size() != this->cols_constraints.size()) {
        std::cerr << "Invalid rows and/or columns size\n";
        exit(1);
    }

    this->size = this->rows_constraints.size();
    this->calculate_domains();

}

void Puzzle::print() {

    std::cout << "Size: " << (int)this->size << "\n\n";

    std::cout << "Matrix:\n";

    std::cout << "\nRows:\n";

    this->print(this->rows_constraints);

    std::cout << "\nCols:\n";

    this->print(this->cols_constraints);

    std::cout << "\nRow domains:\n";

    this->print(this->rows_domain);

    std::cout << "\nCols domains:\n";

    this->print(this->cols_domain);

    std::cout << "\n";
}

void Puzzle::fill_vector(std::vector<uint32_t> &v, std::string line, char dlm) {

    std::stringstream stream(line);
    std::string s;

    while(std::getline(stream, s, dlm)) {
        int val = std::stoi(s);
        v.push_back(val);
    }

    v.shrink_to_fit();

}

void Puzzle::fill_vector(std::vector<std::vector<uint32_t>> &v, std::string line, char dlm_outer, char dlm_inner) {

    std::stringstream stream(line);
    std::string s;

    while(std::getline(stream, s, dlm_outer)) {
        std::vector<uint32_t> numbers;

        this->fill_vector(numbers, s, dlm_inner);

        v.push_back(numbers);
    }

    v.shrink_to_fit();

}

void Puzzle::print(std::vector<std::vector<uint32_t>> v) {

    for(const auto &rw : v) {
        for(const auto &cl : rw) {
            std::cout << cl << " ";
        }
        std::cout << "\n";
    }

}

void Puzzle::check(std::vector<std::vector<uint32_t>> v) {

    const uint32_t MAX_SIZE = v.size();

    for(const auto &rw : v) {
        uint32_t size_vec = std::accumulate(rw.begin(), rw.end(), 0) + rw.size() - 1;

        if(size_vec > MAX_SIZE) {
            std::cerr << "Sum of squares exceeds maximum capacity\n";
            exit(1);
        }
    }

}

uint32_t Puzzle::value_to_squares(uint32_t v) {

    uint32_t squares = 0;

    for(uint32_t i = 0; i < v; i++) {
        squares += (1 << i);
    }

    return squares;

}

std::vector<uint32_t> Puzzle::get_domain(std::vector<uint32_t> c) {

    std::vector<uint32_t> domain;

    if(c.size() == 1) {

        const uint32_t value = c.at(0);
        uint32_t squares = this->value_to_squares(value);
        const uint32_t max_value = (uint32_t)(1 << (int)this->size);

        while(squares < max_value) {
            domain.push_back(squares);
            squares <<= 1;
        }

        domain.shrink_to_fit();
        return domain;
    }

    if(std::accumulate(c.begin(), c.end(), 0) + c.size() - 1 == this->size) {
        uint32_t value = 0;

        for(const auto &v : c) {

            const uint32_t squares = this->value_to_squares(v);
            value <<= (int)log2(squares) + 2;
            value += squares;

        }

        domain.push_back(value);
        domain.shrink_to_fit();

        return domain;
    }

    std::vector<uint32_t> squares_vec(c.size());

    for(uint32_t i = 0; i < c.size(); i++) {
        squares_vec[i] = this->value_to_squares(c[i]);
    }

    squares_vec.shrink_to_fit();

    uint32_t min_value = 0;

    for(const auto &v : c) {

        const uint32_t squares = this->value_to_squares(v);
        min_value <<= (int)log2(squares) + 2;
        min_value += squares;

    }

    domain.push_back(min_value);

    return domain;

}

std::vector<uint32_t> Puzzle::get_domain(std::vector<uint32_t> d, std::vector<uint32_t> s, uint16_t idx, uint16_t left_pos, uint32_t acc) {

    if(idx == s.size())
        return d;

    for(uint32_t i = 1; (acc << i) < (uint32_t)(1 << this->size); i++) {

    }

    return d;

}

void Puzzle::calculate_domains() {

    for(const auto &c : this->cols_constraints)
        this->cols_domain.push_back(this->get_domain(c));

    for(const auto &r : this->rows_constraints)
        this->rows_domain.push_back(this->get_domain(r));

}

std::vector<bool> Puzzle::bit_representation(uint32_t n) {

    std::vector<bool> v;

    while(n) {
        v.push_back(n & 1);
        n >>= 1;
    }

    while(v.size() < this->size)
        v.push_back(false);

    std::reverse(v.begin(), v.end());

    return v;

}
