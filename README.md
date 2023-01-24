![CALICO Logo](https://calico.berkeley.edu/images/banner/blocks.png)

# calico-fa22
***Note**: This repo is under construction. Check back occasionally for updates! Last Updated: 1/24*

## Editorial Progress
**Published**: 
- [Problem 1 (bookshelf): she shells book shelves by the she shelf](https://calico.berkeley.edu/files/calico-fa22/editorials/bookshelf-editorial.pdf)
- [Problem 2 (rso): Office of Business Contracts and Brand Protection](https://calico.berkeley.edu/files/calico-fa22/editorials/rso-editorial.pdf)
- [Problem 3 (paint): This problem was not brought to you by jane street](https://calico.berkeley.edu/files/calico-fa22/editorials/paint-editorial.pdf)
- [Problem 4 (bottles): Water Bottles](https://calico.berkeley.edu/files/calico-fa22/editorials/bottles-editorial.pdf)
- [Problem 11 (tetris): 'Tiger’s *Tetris* Tournament](https://calico.berkeley.edu/files/calico-fa22/editorials/tetris-editorial.pdf)

**Drafted**: toki, tower, extrusion

**In Progress**: bread, sausages, warden, warden2

## Quick Start
This repository contains all contest materials for CALICO Fall '22, including solutions, editorials, tests, templates, and problem statements.

You can explore this repository using GitHub in your browser or download an [archive of all the files](https://github.com/calico-team/calico-fa22/archive/refs/heads/main.zip). If you'd like to see what files participants were given during the contest, you can download the [contest.zip](https://calico.berkeley.edu/files/calico-fa22/contest.zip)!

Although the contest is over, you can still submit solutions to the [judge platform](https://calicojudge.com) under the `calico-fa22-archive` contest. Sign in or register if you don't have an account already. Then change the selected contest to `calico-fa22-archive` on the right side of the navigation bar.

This is our first time publishing solutions and editorials for a CALICO contest! We highly encourage you to take a look as we're very happy how they turned out; we hope you find this to be a useful and interesting educational resource!

## Repository Structure
The root of the repository has `calico-fa22.pdf`, which contains all problem statements, and `calico-fa22-editorial.pdf`, which contains all editorials. Subdirectories are named after each problem and contain their solutions, editorials, tests, templates, and problem statements.

### Solutions
Solutions are programs written by us that implement different approaches of varying efficiency in multiple programming languages to solve each problem. As a result, some solutions may pass more test sets than others. Solution files are named `[problem name]_[solution name].[extension]`, where `[solution_name]` is a keyword that describes the solution, and `[extension]` is the extension used by that language's source files (for example, `.cpp`, `.java`, or `.py`).

### Editorials
Editorials describe and thoroughly explain several approaches of varying efficiency to solve each problem. They are named `[problem_name]-editorial.pdf`.

### Tests
These are the inputs and outputs we use to test your program for correctness. Input files have the `.in` extension and corresponding output files have the `.ans` extension with the same file name. Test files are categorized as sample (visible to contestants during the contest) and secret (everything else) under the data folder in each problem subdirectory.

### Templates
Templates provide starter code that handle parsing input in multiple languages, so contestants can jump right into problem solving. They are named `[problem name]_template.[extension]`.

Note that these templates are only guaranteed to apply to the main test set of each problem; completing bonus test sets may require modifying the templates.

### Problem Statements
Problem statements describe the problem contestants need to solve, as well as their input and output format. They are named `[problem name].pdf`.

### Directory Tree
```
[contest name]
├── [contest name].pdf
├── [contest name]-editorial.pdf
├── [problem name]
│   ├── [problem name].pdf
│   ├── [problem name]-editorial.pdf
│   ├── solutions
│   │   ├── [problem name]_[solution name].[extension]
│   │   └── ...
│   ├── templates
│   │   ├── [problem name]_template.[extension]
│   │   └── ...
│   └── tests
│       ├── sample
│       │   ├── [test name].in
│       │   ├── [test name].ans
│       │   └── ...
│       └── secret
│           ├── [test name].in
│           ├── [test name].ans
│           └── ...
├── [problem name]
│   └── ...
└── ...
```

## Credits

Under construction!