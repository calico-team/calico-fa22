![CALICO Logo](https://calico.berkeley.edu/images/banner/blocks.png)

# calico-fa22
***Note**: This repo is under construction. Check back occasionally for updates! Last Updated: 2/1*

## Editorial Progress
**Published**: 
- [Problem 1 (bookshelf): she shells book shelves by the she shelf](https://calico.berkeley.edu/files/calico-fa22/editorials/bookshelf-editorial.pdf)
- [Problem 2 (rso): Office of Business Contracts and Brand Protection](https://calico.berkeley.edu/files/calico-fa22/editorials/rso-editorial.pdf)
- [Problem 3 (paint): This problem was not brought to you by jane street](https://calico.berkeley.edu/files/calico-fa22/editorials/paint-editorial.pdf)
- [Problem 4 (bottles): Water Bottles](https://calico.berkeley.edu/files/calico-fa22/editorials/bottles-editorial.pdf)
- [Problem 5 (bread): Let's Get This Bread](https://calico.berkeley.edu/files/calico-fa22/editorials/bread-editorial.pdf)
- [Problem 7 (toki): nasin kalama pi toki pona](https://calico.berkeley.edu/files/calico-fa22/editorials/toki-editorial.pdf)
- [Problem 8 (tower): your a wizard harry](https://calico.berkeley.edu/files/calico-fa22/editorials/tower-editorial.pdf)
- [Problem 9 (extrusion): SOLIDWORKS is not responding](https://calico.berkeley.edu/files/calico-fa22/editorials/extrusion-editorial.pdf)
- [Problem 10 (warden): Steve was obliterated by a sonically-charged shriek](https://calico.berkeley.edu/files/calico-fa22/editorials/warden-editorial.pdf)
- [Problem 11 (tetris): 'Tiger’s *Tetris* Tournament](https://calico.berkeley.edu/files/calico-fa22/editorials/tetris-editorial.pdf)

**Drafted**: sausages, warden, warden2

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

### Backend Files (Partial Coverage)
For the problems written by Jeffrey (`bottles` and `tetris`), all backend files created during the process of preparation are also included. We currently think backend files for the other problems are too confusing to be accessible, but they may be published later.

All of these files are heavily documented with comments. They are intended to be useful as one example of how to replicate test data or set up your own judging system; you may choose to instead use more popular systems like [CodeForces](https://codeforces.com/) and/or [Polygon](https://polygon.codeforces.com/).

#### Submissions (All Problems)
|File|Description|
|---|---|
|`submissions/accepted/*`|These are identical to the respective programs in `solutions/*`. For each problem, one of the Python models is used by the generators to generate the reference outputs.|
|`submissions/runtime_error/*`<br>`submissions/time_limit_exceeded/*`<br>`submissions/wrong_answer/*`|These are implementations (generally written by organizers pre-contest) that seem perfect at first glance but have small bugs that cause the respective issues when judged. We predicted that most failed in-contest submissions would be categorized under one of these bugs.|

#### Generators (All Problems)
|File|Description|
|---|---|
|`jewato_gen.py`|Jeffrey's personal generator utilities, custom-built for CALICO but used for all his problems, are in this script. It implements many routine functions, including test set generators, test file objects, and file system I/O. All of the generator scripts listed below use it as a base; it is identical between different problems.|
|`[problem name]_utils.py`|Each problem has a custom-built random seed and collection of helper utilities in this file, enabling easy creation of customized tests by specifying parameters. Using `bottles` as an example, the `Bottles` class generalizes all test cases for that problem, while `BottlesMain` and `BottlesBonus` add further parameters to their corresponding subtasks.|
|`delete.py`|This is an optional helper script for deleting ZIP archives created by `generate_data.py` if desired; the other scripts will still run correctly if this is not used.|
|`generate_data.py`|Read this to see examples of using the generator utilties to make your own tests. It runs specific commands from the utilities file to create the test data in `./data`, along with container directories if absent.|
|`generate_zips.py`|This program runs `generate_data.py` and additionally packages the data into a separate ZIP archive, one for each subtask. These archives follow the DOMJudge package format.|

#### Checkers (`bottles` Only)
|File|Description|
|---|---|
|`executables/compare/compare.py`|For problems with multiple correct answers, this file contains the bulk of the problem-specific code for the checker (backend program that enforces criteria listed in the statement).|
|`executables/compare/build`<br>`executables/compare/run`|These are the other files in `executables/compare` and are generic shell scripts that use `compare.py`.|
|`make_executables`|This shell script packages the `executables/compare/` directory into a ZIP archive following the DOMJudge package format.|

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