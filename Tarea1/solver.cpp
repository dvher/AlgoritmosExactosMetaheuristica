#include <algorithm>
#include <fstream>
#include <numeric>
#include <sstream>
#include <vector>
#include "solver.hpp"

Solver::Solver() {
}

Solver::Solver(std::string filename) {
    this->read_file(filename);
}

void Solver::read_file(std::string filename) {

    std::ifstream file_handler(filename, std::ios::in);

    if(!file_handler.is_open()) {
        std::cout << "Couldn't open file\n";
        exit(1);
    }

    std::string line;

    getline(file_handler, line);

    this->fill_vector(this->rows, line, ' ', ',');

    getline(file_handler, line);

    this->fill_vector(this->cols, line, ' ', ',');

    file_handler.close();

    this->check(this->rows);
    this->check(this->cols);

    if(this->rows.size() != this->cols.size()) {
        std::cerr << "Invalid rows and/or columns size\n";
        exit(1);
    }

    const uint32_t SIZE = this->rows.size();

    this->matrix.resize(SIZE);
    std::fill(this->matrix.begin(), this->matrix.end(), std::vector<bool>(SIZE, false));

}

void Solver::print() {

    std::cout << "Matrix:\n";

    for(const auto &x : this->matrix) {
        for(const auto &y : x)
            std::cout << (y ? "true" : "false") << " ";
        std::cout << "\n";
    }

    std::cout << "\nRows:\n";

    this->print(this->rows);

    std::cout << "\nCols:\n";

    this->print(this->cols);

    std::cout << "\n";
}

void Solver::fill_vector(std::vector<uint32_t> &v, std::string line, char dlm) {

    std::stringstream stream(line);
    std::string s;

    while(getline(stream, s, dlm)) {
        int val = std::stoi(s);
        v.push_back(val);
    }

}

void Solver::fill_vector(std::vector<std::vector<uint32_t>> &v, std::string line, char dlm_outer, char dlm_inner) {

    std::stringstream stream(line);
    std::string s;

    while(getline(stream, s, dlm_outer)) {
        std::vector<uint32_t> numbers;

        this->fill_vector(numbers, s, dlm_inner);

        v.push_back(numbers);
    }

}

void Solver::print(std::vector<std::vector<uint32_t>> v) {

    for(const auto &rw : v) {
        for(const auto &cl : rw) {
            std::cout << cl << " ";
        }
        std::cout << "\n";
    }

}

void Solver::check(std::vector<std::vector<uint32_t>> v) {

    const uint32_t MAX_SIZE = v.size();

    for(const auto &rw : v) {
        uint32_t size = std::accumulate(rw.begin(), rw.end(), 0) + rw.size() - 1;

        if(size > MAX_SIZE) {
            std::cerr << "Sum of squares exceeds maximum capacity\n";
            exit(1);
        }
    }

}
