#include <algorithm>
#include <fstream>
#include <numeric>
#include <sstream>
#include <cmath>
#include "puzzle.hpp"

Puzzle::Puzzle() {
}

Puzzle::Puzzle(std::string filename) {
    std::vector<std::vector<uint32_t>> rows, cols, dom_r, dom_c;
    this->constraints.push_back(rows);
    this->constraints.push_back(cols);
    this->domains.push_back(dom_r);
    this->domains.push_back(dom_c);
    this->read_file(filename);
}

void Puzzle::read_file(std::string filename) {

    std::ifstream file_handler(filename, std::ios::in);

    if(!file_handler.is_open()) {
        std::cout << "Couldn't open file\n";
        exit(1);
    }

    this->fill_constraints(this->constraints, file_handler, ' ', ',');

    file_handler.close();

    for(const auto &v : this->constraints) {
        this->check(v);
    }

    if(this->constraints.size() != 2 && this->constraints.size() != this->constraints.size()) {
        std::cerr << "Invalid rows and/or columns size\n";
        exit(1);
    }

    this->size = this->constraints.at(0).size();
    this->calculate_domains();

}

void Puzzle::print() {

    std::cout << "Size: " << (int)this->size << "\n\n";

    std::cout << "Matrix:\n";

    std::cout << "\nRows:\n";

    this->print(this->constraints.at(0));

    std::cout << "\nCols:\n";

    this->print(this->constraints.at(1));

    std::cout << "\nRow domains:\n";

    this->print(this->domains.at(0));

    std::cout << "\nCols domains:\n";

    this->print(this->domains.at(1));

    std::cout << "\n";
}

void Puzzle::fill_constraints(std::vector<std::vector<std::vector<uint32_t>>> &m, std::ifstream &file_handler, char dlm_outer, char dlm_inner) {

    std::string line;

    for(auto &v : m) {

        getline(file_handler, line);
        this->fill_vector(v, line, dlm_outer, dlm_inner);
    }

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

    std::vector<uint32_t> new_domain = this->get_domain(domain, squares_vec, 0, this->size, 0);

    domain.insert(domain.end(), new_domain.begin(), new_domain.end());

    return domain;

}

std::vector<uint32_t> Puzzle::get_domain(std::vector<uint32_t> domain, std::vector<uint32_t> squares, uint16_t idx, uint16_t left_pos, uint32_t acc) {

    if(idx == squares.size())
        return domain;

    // Make this function use recursivity to get all possible bit combinations such as
    // 0 0 0 0 0 1 1 0 1 1
    // 0 0 0 0 1 1 0 0 1 1
    // 0 0 0 0 1 1 0 1 1 0
    // 0 0 0 1 1 0 0 0 1 1
    // 0 0 0 1 1 0 0 1 1 0
    // 0 0 0 1 1 0 1 1 0 0
    // 0 0 1 1 0 0 0 0 1 1
    // 0 0 1 1 0 0 0 1 1 0
    // 0 0 1 1 0 0 1 1 0 0
    // 0 0 1 1 0 1 1 0 0 0
    // 0 1 1 0 0 0 0 0 1 1
    // 0 1 1 0 0 0 0 1 1 0
    // 0 1 1 0 0 0 1 1 0 0
    // 0 1 1 0 0 1 1 0 0 0
    // 0 1 1 0 1 1 0 0 0 0
    // 1 1 0 0 0 0 0 0 1 1
    // 1 1 0 0 0 0 0 1 1 0
    // 1 1 0 0 0 0 1 1 0 0
    // 1 1 0 0 0 1 1 0 0 0
    // 1 1 0 0 1 1 0 0 0 0
    // 1 1 0 1 1 0 0 0 0 0

    const uint32_t squares_value = squares[idx];
    const uint16_t squares_size = log2(squares_value) + 1;

    const uint32_t max_value = (uint32_t)(1 << (int)this->size);

    uint32_t value = 0;

    for(uint16_t i = 0; i < squares_size; i++) {
        value <<= 2;
        value += 1;
    }

    if(left_pos < squares_size)
        return domain;

    uint32_t curr_value = (acc << (int)squares_size) + value;

    if(curr_value < max_value) {
        domain.push_back(curr_value);
        domain = this->get_domain(domain, squares, idx + 1, left_pos - squares_size, curr_value);
    }

    if(left_pos > squares_size) {
        domain = this->get_domain(domain, squares, idx, left_pos - 1, acc);
    }

    return domain;


}

void Puzzle::calculate_domains() {

    for(uint32_t i = 0; i < this->constraints.size(); i++)
        for(const auto &v : this->constraints.at(i))
            this->domains.at(i).push_back(this->get_domain(v));

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
