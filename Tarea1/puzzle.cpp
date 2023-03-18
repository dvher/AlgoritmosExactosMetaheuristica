#include <algorithm>
#include <fstream>
#include <numeric>
#include <sstream>
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

}

void Puzzle::print() {

    std::cout << "Matrix:\n";

    std::cout << "\nRows:\n";

    this->print(this->rows_constraints);

    std::cout << "\nCols:\n";

    this->print(this->cols_constraints);

    std::cout << "\n";
}

void Puzzle::fill_vector(std::vector<uint32_t> &v, std::string line, char dlm) {

    std::stringstream stream(line);
    std::string s;

    while(std::getline(stream, s, dlm)) {
        int val = std::stoi(s);
        v.push_back(val);
    }

}

void Puzzle::fill_vector(std::vector<std::vector<uint32_t>> &v, std::string line, char dlm_outer, char dlm_inner) {

    std::stringstream stream(line);
    std::string s;

    while(std::getline(stream, s, dlm_outer)) {
        std::vector<uint32_t> numbers;

        this->fill_vector(numbers, s, dlm_inner);

        v.push_back(numbers);
    }

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
        uint32_t size = std::accumulate(rw.begin(), rw.end(), 0) + rw.size() - 1;

        if(size > MAX_SIZE) {
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
        uint32_t value = c.at(0);
        uint32_t squares = this->value_to_squares(value);

        while(squares < 1 << this->size) {
            domain.push_back(squares);
            squares <<= 1;
        }

        return domain;
    }

    return domain;

}

void Puzzle::calculate_domains() {



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